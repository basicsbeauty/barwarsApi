#!/usr/bin/python

from piston.handler import BaseHandler
from piston.utils import rc
from proto import bwdo_pb2
from v1 import utils

import random
import urllib 

import MySQLdb as db

import base64

#Monkey patching threading module http://stackoverflow.com/questions/13193278/understand-python-threading-bug
import threading
threading._DummyThread._Thread__stop = lambda x: 42

SUCCESS = True
FAILURE = False

db_cursor = None

#########################################################################
# DB: Cursor: 
#########################################################################
def getDBCursor():

  global db_cursor

  if db_cursor:
    return db_cursor

  try:
    # DB: Connection: Create
    host = 'localhost'
    user = 'u_barwars'
    password = 'barwars'
    database = 'db_barwars'
    db_con = db.connect( host, user, password, database)
    
    # DB: Init: Success
    db_init_flag = True
    
    # DB: Cursor:
    db_cursor = db_con.cursor()
    
    # logLine( "DB: Connection: Create: Success:")

  except db.error, e:
    db_cursor = None
    print "DB creation error: ", e

  return db_cursor

#########################################################################
# Request: Profile: Get: Process:
#########################################################################
def processProfileGet( db_cursor, user_do = None, challenge_do = None):
  
  utils.logLine( "Profile: Get: Process: BEGN: " + str(user_do))
  try:

    utils.logLine( "UUID: " + user_do.uuid)
    table = 'user'
    column_list = ' uuid, profile_name, points, solved_count, submit_count'
    query  = 'select ' + column_list + ' from ' + table + ' where '
  
    if user_do.uuid:
      query += 'uuid =\'' + str(user_do.uuid) + '\' '

    utils.logLine( query)
    db_cursor.execute( query)            
    db_record = db_cursor.fetchall()
    if not db_record:
      print "Unable to retrieve user record!!"
      return None
    utils.logLine( "DBRs:" + str(db_record))
    db_record = db_record[0]
    utils.logLine( "Rs 0:" + str(db_record))

    profile_response = bwdo_pb2.GetProfileResponse()
    user_do_res = profile_response.user
    
    user_do_res.uuid = str(db_record[0])
    user_do_res.display_name = str(db_record[1])

    user_do_res.points = int(db_record[2])
    user_do_res.solved_count = int(db_record[3])
    user_do_res.submit_count = int(db_record[4])

  except db.error, e:
    print "DB creation error: ", e
    return None

  utils.logLine( "Profile: Get: Process: DO: " + str(profile_response))
  return profile_response.SerializeToString()

#########################################################################
# Request: Profile: Post(Add): Process:
#########################################################################
def processProfilePost( db_cursor, user_do = None, challenge_do = None):
  
  utils.logLine( "Profile: Post: Process: BEGN: " + str(user_do))

  profile_names = [ 'Detective', 'Discoverer', 'Hunter'] 

  if not user_do.uuid:
    return None

  utils.logLine( "UUID: " + str(user_do.uuid))

  try:

    # Query:
    table = 'user'
    query  = 'insert into ' + table + ' values( '
    query += '\''  + str(user_do.uuid) + '\','
    query += '\''  + profile_names[ random.randint( 0, 2)] + '\','
    query += ' 128,'
    query += ' 0,'
    query += ' 0,'
    query += ' now(),'
    query += ' now())'
     
    utils.logLine( query)
    # db_cursor.execute( query)
    # db_cursor.execute( "commit")

  except db.error, e:
    print "DB creation error: ", e
    return None

  return processProfileGet( db_cursor, user_do)

#########################################################################
# Request: Description: Get: Process:
#########################################################################
def processDescriptionGet( user_do = None, challenge_do = None):

  upc = challenge_do.bar_code
  result = utils.barcodeToDescription(upc)
  if result == "":
    return None
  else:
    description_response = bwdo_pb2.GetDescriptionResponse()
    
  ch_do = description_response.challenge
  ch_do.bar_code = upc
  ch_do.description = result
  
  return description_response.SerializeToString()

#########################################################################
# Request: Challenge: Get: Process:
#########################################################################
def processChallengeListGet( db_cursor, user_do = None, filter = None):
    
  utils.logLine( "Challenge: List: Get: Process: BEGN: " + str(user_do))

  if not user_do.uuid:
    return None

  try:

    utils.logLine( "UUID: " + user_do.uuid)

    # Query:
    table = 'challenge'
    column_list = ' cid, description'
    query  = 'select ' + column_list + ' from ' + table + ' '
    query += 'where status=0 '
    
    utils.logLine("query: " + str(query))
    if user_do.uuid:
        query += 'and uuid != \'' + str(user_do.uuid) + '\' '

    if filter:
        query += 'and description like \'%' + str(filter) + '%\' '
    
    query += 'group by description'
    utils.logLine( query)
    db_cursor.execute( query)
    
    db_records = db_cursor.fetchall()
    utils.logLine( "DBRs: " + str(db_records))
    
  except db.error, e:
    print "DB creation error: ", e
    return None

  # DB Records -> GetGetChallengesListResponse
  ch_list_response = bwdo_pb2.GetChallengesListResponse()

  for challenge_row in db_records:

      ch_do = ch_list_response.challenge_list.add()
      ch_do.cid = str(challenge_row[0])
      ch_do.description = challenge_row[1]                    

  utils.logLine( "Resp: " + str(ch_list_response))
    
  return ch_list_response.SerializeToString()

#########################################################################
# Request: Challenge: Post(Add): Process:
#########################################################################
def processChallengePost( db_cursor, user_do = None, challenge_do = None):
    
  utils.logLine( "Challenge: List: Get: Process: BEGN: " + str(challenge_do.bar_code))

  # Input: Arguments: Validation
  if not user_do.uuid:
    return None
  if not challenge_do.bar_code:
    return None

  try:  

    # Barcode -> Description
    description = utils.barcodeToDescription( challenge_do.bar_code)
    if not description:
      return None
    description = description.strip()
    
    # Challenge: Add: Query:
    table  = 'challenge'
    query  = 'insert into challenge ( barcode, description, status, uuid, time_created, time_updated)  values('
    query += '\''  + str(challenge_do.bar_code) + '\','
    query += '\''  + str(description) + '\','
    query += str( 0) + ','
    query += '\''  + str(user_do.uuid) + '\','
    query += ' now(),'
    query += ' now())'
    utils.logLine(query)
    db_cursor.execute( query)
    
    # User: Update: Submit_count: Increment
    table = 'user'
    query  = 'update ' + table + ' set submit_count=submit_count+1 where' 
    query += ' uuid=\''  + str(user_do.uuid) + '\''
    utils.logLine(query)
    db_cursor.execute( query)

    # User: Point: Count: Decrement
    table = 'user'
    query  = 'update ' + table + ' set points=points-1 where' 
    query += ' uuid=\''  + str(user_do.uuid) + '\''
    utils.logLine(query)
    db_cursor.execute(query)

    db_cursor.execute( "commit")
    
  except db.error, e:
    print "DB creation error: ", e
    return None
    
  return processProfileGet( db_cursor, user_do)

#########################################################################
# Request: Challenge: Post(Add): Process:
#########################################################################
SOLVED = 1
UNSOLVED = 0
def processChallengeSolve( db_cursor, user_do = None, challenge_do = None):
    
  utils.logLine( "Challenge: List: Get: Process: BEGN: " + str(challenge_do.bar_code))

  # Input: Arguments: Validation
  if not user_do.uuid:
    return None
  if not challenge_do.cid and challenge_do.bar_code:
    return None

  try:  

    # Challenge: Solve: Check:
    table  = 'challenge'
    print "Solve challenge==>> ", challenge_do
    column_list = 'barcode'  
    where_clause_unsolved_challenges = 'status=0'
    where_clause_not_post_by_current_user = ' uuid !=  \'' + user_do.uuid + '\''
  
    query  = 'select ' + column_list + ' from ' + table + ' where '
    query += where_clause_unsolved_challenges
    query += ' and ' + where_clause_not_post_by_current_user
    query += ' and cid = ' + challenge_do.cid
    query += ' and barcode = \'' + str(challenge_do.bar_code) + '\' '
    utils.logLine(query)
    db_cursor.execute(query)
  
    # Failure: If there no match
    if not db_cursor.fetchone():
      print "Solve challenge==>, NO match found!!!, query was :: ", query
      return processProfileGet( db_cursor, user_do)
  
    # Challenge: Solve: Mark: Solved
    table  = 'challenge'
    print "Solve challenge, going to run update==> ", challenge_do
    query  = 'update ' + table + ' set status=1 where cid=' + str(challenge_do.cid)
    utils.logLine(query)
    db_cursor.execute(query)
  
    # User: Increment: Solved: Count:
    table = 'user'
    query  = 'update ' + table + ' set solved_count=solved_count+1 where' 
    query += ' uuid=\''  + str(user_do.uuid) + '\''
    utils.logLine(query)
    db_cursor.execute(query)

    # User: Increment: Solved: Count:
    table = 'user'
    query  = 'update ' + table + ' set points=points+1 where' 
    query += ' uuid=\''  + str(user_do.uuid) + '\''
    utils.logLine(query)
    db_cursor.execute(query)

    db_cursor.execute( "commit")
    
  except db.error, e:
    print "DB creation error: ", e
    return None
    
  return processProfileGet( db_cursor, user_do)

#########################################################################
# Request: Process: Global 
#########################################################################
def processRequest(req_obj, req_type):

  utils.logLine( "Rqst: Prcs: I/p : Type: " + str(req_type) + " RQST: " + str(req_obj))

  res = {}

  cursor = getDBCursor()
  if not cursor:
     res['status'] = FAILURE
     res['err_msg'] = "DB Access: Failed"
     return res

# TODO: get response object based on request type. This involves fetching data from db and populating the proto objects
  print "00001"
  if req_type == bwdo_pb2.GET_DESCRIPTION:
      print "00002"
      res['r_payload'] = processDescriptionGet( challenge_do = req_obj.challenge)
      print "00003"
  if req_type == bwdo_pb2.GET_PROFILE:
      res['r_payload'] = processProfileGet( cursor, user_do = req_obj.user)
  if req_type == bwdo_pb2.GET_CHALLENGES_LIST:
      res['r_payload'] = processChallengeListGet( cursor, req_obj.user, req_obj.filter)
  if req_type == bwdo_pb2.POST_PROFILE:
      res['r_payload'] = processProfilePost( cursor, req_obj.user)
  if req_type == bwdo_pb2.POST_SUBMIT_CHALLENGE:
      res['r_payload'] = processChallengePost( cursor, req_obj.user, req_obj.challenge)
  if req_type == bwdo_pb2.POST_SOLVE_CHALLENGE:
      res['r_payload'] = processChallengeSolve( cursor, req_obj.user, req_obj.challenge)
 
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
    if parsed_data['status'] == FAILURE:
        return utils.sendErrResp(parsed_data['err_msg'])
    
    ##############################################
    # Request: Process
    ##############################################            
    resp_raw = processRequest(parsed_data['req'], parsed_data['type'])
    # logLine( "RaRs: " + str(resp_raw))
    if resp_raw['status'] == FAILURE:
        return utils.sendErrResp(resp_raw['err_msg'])  

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
