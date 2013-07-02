#!/usr/bin/python

from piston.handler import BaseHandler
from piston.utils import rc
from proto import bwdo_pb2
from v1 import utils
from v1 import dbManager
import random
import urllib 


import base64

#Monkey patching threading module http://stackoverflow.com/questions/13193278/understand-python-threading-bug
import threading
threading._DummyThread._Thread__stop = lambda x: 42

SUCCESS = True
FAILURE = False

#########################################################################
# Request: Profile: Get: Process:
#########################################################################
def processProfileGet( user_do = None, challenge_do = None):
  
  utils.logLine( "processProfileGet: BEGIN: " + str(user_do))

  if user_do is None:
    print "user DO cannot be None"
    utils.logLine( "processProfileGet: Error: user DO None")
    return None

  userProfileData = dbManager.getProfileDataDB(user_do.uuid)
  if userProfileData is None:
    print "Unable to fetch user profile"
    utils.logLine( "processProfileGet: Error: unable to fetch user profile")
    return None

  profile_response = bwdo_pb2.GetProfileResponse()
  user_do_res = profile_response.user
    
  user_do_res.uuid = str(userProfileData[dbManager.UserTblCol['uuid']])
  user_do_res.display_name = str(userProfileData[dbManager.UserTblCol['profile_name']])
  user_do_res.points = int(userProfileData[dbManager.UserTblCol['points']])
  user_do_res.solved_count = int(userProfileData[dbManager.UserTblCol['solved_count']])
  user_do_res.submit_count = int(userProfileData[dbManager.UserTblCol['submit_count']])

  utils.logLine( "processProfileGet: DONE: " + str(profile_response))
  return profile_response.SerializeToString()

#########################################################################
# Request: Profile: Post(Add): Process:
#########################################################################
def processProfilePost( user_do = None, challenge_do = None):
  
  utils.logLine( "processProfilePost: BEGN: " + str(user_do))
  if user_do is None:
    print "user DO cannot be None"
    utils.logLine( "processProfilePost: Error: user DO None")
    return None

  # Profile: Presence: Check
  userProfileData = dbManager.getProfileDataDB(user_do.uuid)
  if userProfileData:
    print "Profile: Already: Present:"
    utils.logLine( "processProfileGet: Error: Profile: Already: Present")
    return processProfileGet( user_do)

  dbResp = dbManager.postProfileDataDB(user_do.uuid)
  if not dbResp:
    print "user DO cannot be None"
    utils.logLine( "processProfilePost: Error: DB operation failed")
    return None

  utils.logLine( "processProfilePost: DONE")
  return processProfileGet(user_do)

#########################################################################
# Request: Description: Get: Process:
#########################################################################
def processDescriptionGet( user_do = None, challenge_do = None):

  utils.logLine("processDescriptionGet: BEGN: " + str(user_do))
  if user_do is None:
    print "user DO None"
    utils.logLine( "processDescriptionGet : user DO None")
  upc = challenge_do.bar_code
  result = utils.barcodeToDescription(upc)
  if result == "":
    utils.logLine("processDescriptionGet: unable to get barcode description")
    print "processDescriptionGet: unable to get barcode description"
    return None
  else:
    description_response = bwdo_pb2.GetDescriptionResponse()
    
  ch_do = description_response.challenge
  ch_do.bar_code = upc
  ch_do.description = result
  
  utils.logLine("processDescriptionGet: DONE ")
  return description_response.SerializeToString()

#########################################################################
# Request: Challenge: Get: Process:
#########################################################################
def processChallengeListGet( user_do = None, filter = None):
    
  utils.logLine( "processChallengeListGet: BEGN: " + str(user_do))
  if user_do is None:
    print "user DO cannot be None"
    utils.logLine( "processChallengeListGet Error: user DO None")
    return None

  challengeListData = dbManager.getChallengesListDB(user_do.uuid, filter = filter)
  if challengeListData is None: 
    print "No challenge list found in DB!"
    utils.logLine( "processChallengeListGet Error: No challenge list found in DB!")
    return None

  ch_list_response = bwdo_pb2.GetChallengesListResponse()
  for challenge_row in challengeListData:
      ch_do = ch_list_response.challenge_list.add()
      #ch_do.cid = str(challenge_row[dbManager.ChallengeTblCol['cid']])
      #ch_do.description = str(challenge_row[dbManager.ChallengeTblCol['description']])
      ch_do.cid = str(challenge_row['cid'])
      ch_do.description = str(challenge_row['description'])

  utils.logLine( "processChallengeListGet DONE: challenges list: " + str(ch_list_response))
  return ch_list_response.SerializeToString()

#########################################################################
# Request: Challenge: Post(Add): Process:
#########################################################################
def processChallengePost( user_do = None, challenge_do = None):
    
  utils.logLine( "processChallengePost: BEGN ")
  if user_do is None:
    print "user DO cannot be None"
    utils.logLine( "processChallengePost Error: user DO None")
    return None

  if challenge_do is None:
    print "challenge DO cannot be None"
    utils.logLine( "processChallengePost Error: challenge DO None")
    return None
  # Input: Arguments: Validation
  if not user_do.uuid:
    print "uuid cannot be None"
    utils.logLine( "processChallengePost Error: uuid None")
    return None
  if not challenge_do.bar_code:
    print "uuid cannot be None"
    utils.logLine( "processChallengePost Error: bar_code None")
    return None

  # Barcode -> Description
  description = utils.barcodeToDescription(challenge_do.bar_code)
  if not description:
    print "barcode description NOT found!"
    utils.logLine( "processChallengePost Error: barcode description NOT found!")
    return None
  description = description.strip()
    
  dbResp = dbManager.postChallengeDB(user_do.uuid, challenge_do.bar_code, description)
  if not dbResp:
    print "Unable to submit challenge into DB!"
    utils.logLine( "processChallengePost Error: Unable to submit challenge into DB!")
    return None

  utils.logLine( "processChallengePost: DONE ")
  return processProfileGet(user_do)

#########################################################################
# Request: Challenge: Post(Add): Process:
#########################################################################
def processChallengeSolve( user_do = None, challenge_do = None):
    
  utils.logLine( "processChallengeSolve: BEGN")
  if user_do is None:
    print "user DO cannot be None"
    utils.logLine( "processChallengeSolve: Error: user DO None")
    return None

  if challenge_do is None:
    print "challenge DO cannot be None"
    utils.logLine( "processChallengeSolve: Error: challenge DO None")
    return None
  # Input: Arguments: Validation
  if not user_do.uuid:
    print "uuid cannot be None"
    utils.logLine( "processChallengeSolve: Error: uuid None")
    return None
  if not challenge_do.bar_code:
    print "uuid cannot be None"
    utils.logLine( "processChallengeSolve: Error: bar_code None")
    return None

  dbResp = dbManager.solveChallengeDB(user_do.uuid, challenge_do.bar_code, challenge_do.cid)
  if not dbResp:
    print "Unable to solvechallenge into DB!"
    utils.logLine( "processChallengeSolve Error: Unable to solve challenge into DB!")
    return None
    
  return processProfileGet(user_do)

#########################################################################
# Request: Process: Global 
#########################################################################
def processRequest(req_obj, req_type):

  utils.logLine( "Rqst: Prcs: I/p : Type: " + str(req_type) + " RQST: " + str(req_obj))

  res = {}

# TODO: get response object based on request type. This involves fetching data from db and populating the proto objects
  if req_type == bwdo_pb2.GET_DESCRIPTION:
      res['r_payload'] = processDescriptionGet(challenge_do = req_obj.challenge)
  if req_type == bwdo_pb2.GET_PROFILE:
      res['r_payload'] = processProfileGet(user_do = req_obj.user)
  if req_type == bwdo_pb2.GET_CHALLENGES_LIST:
      res['r_payload'] = processChallengeListGet(req_obj.user, req_obj.filter)
  if req_type == bwdo_pb2.POST_PROFILE:
      res['r_payload'] = processProfilePost(req_obj.user)
  if req_type == bwdo_pb2.POST_SUBMIT_CHALLENGE:
      res['r_payload'] = processChallengePost(req_obj.user, req_obj.challenge)
  if req_type == bwdo_pb2.POST_SOLVE_CHALLENGE:
      res['r_payload'] = processChallengeSolve(req_obj.user, req_obj.challenge)
 
  res['status'] = SUCCESS
  return res
  
########################################################################
# Input: Message: handler
#########################################################################
class RequestHandler(BaseHandler):
  def read(self, request, test=None):
    
    # HTTP Request -> Service Data
    data = request.GET.get('data', '')
    
    ##############################################
    # Request: Parse
    ##############################################            
    parsed_data = utils.parseData(data)
    print "00"
    if parsed_data['status'] == FAILURE:
        return utils.sendErrResp(parsed_data['err_msg'])
    
    print "01"
    ##############################################
    # Request: Process
    ##############################################            
    resp_raw = processRequest(parsed_data['req'], parsed_data['type'])
    # logLine( "RaRs: " + str(resp_raw))
    if resp_raw['status'] == FAILURE:
        return utils.sendErrResp(resp_raw['err_msg'])  

    print "02"
    ##############################################
    # Response: Construct
    ##############################################	   
    # logLine( "Pars: " + str(resp_raw))
    resp_msg = utils.generateResponse( resp_raw['r_payload'], parsed_data['req_msg_id'], parsed_data['type'])

    ##############################################
    # Response: Pack & Send
    ##############################################           

    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"data": base64.b64encode(resp_msg.SerializeToString())}
    resp.content = respDict
    return resp

  def create(self, request, test=None):
    
    data = request.POST['data']    
    utils.logLine( "POST: Data: " + str(data))
    
    parsed_data = utils.parseData( data, 'POST')
    if parsed_data['status'] == FAILURE:
      return utils.sendErrResp(parsed_data['err_msg'])
    utils.logLine( "PrDa: " + str(parsed_data))
          
    resp_raw = processRequest( parsed_data['req'], parsed_data['type'])
    if resp_raw['status'] == FAILURE:
      return utils.sendErrResp(resp_raw['err_msg'])  
    if resp_raw['r_payload'] is None:
      return utils.sendErrResp("Unable to process request")
    resp_msg = utils.generateResponse( resp_raw['r_payload'], parsed_data['req_msg_id'], parsed_data['type'])
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"data": base64.b64encode(resp_msg.SerializeToString())}
    resp.content = respDict
    return resp
