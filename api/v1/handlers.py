from piston.handler import BaseHandler
from piston.utils import rc
from proto import bwdo_pb2
import subprocess

import base64
#Monkey patching threading module http://stackoverflow.com/questions/13193278/understand-python-threading-bug
import threading
threading._DummyThread._Thread__stop = lambda x: 42

'''

class ProfileHandler(BaseHandler):
  def read(self, request, test=None):
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"uid": 1234, "name": "Cowboy", "solve_count": 7, "submit_count": 10, "attempts": 25}
    resp.content = respDict
    return resp

class UpcHandler(BaseHandler):
  def read(self, request, test=None):
    upc = request.path.split("/")[-2]
    
    #print "upc : ", upc
    cmdline = "curl http://www.upcdatabase.com/item/" + upc + " --silent | grep 'Description' | cut -c 38- | cut -d'<' -f 1"
    #print "cmdline:: ", cmdline
    try: 
      result = subprocess.check_output(cmdline, shell=True)
    except subprocess.CalledProcessError:
      result = "";

    if result == "":
      resp = rc.NOT_FOUND
    else:
      result = result.rstrip()
      resp = rc.ALL_OK
      resp['Content-Type'] = 'text/json'
    respDict = {"desc": result }
    resp.content = respDict

    return resp

class ChallengeHandler(BaseHandler):
  def read(self, request, test=None):
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"challenges": [{"cid": 2345, "description": "Diet Coke"}, {"cid": 3456, "description": "Coke Classic"} ]}
    resp.content = respDict
    return resp

  def create(self, request, test=None):
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"code": 0, "status": "created"}
    resp.content = respDict
    return resp


class ChallengeSolveHandler(BaseHandler):
  def create(self, request, test=None):
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"code": 0, "status": "Success"}
    resp.content = respDict
    return resp
'''
REQ = 0
RESP = 1

req_types_dict = {\
  'GET_DESCRIPTION': (bwdo_pb2.GetDescriptionRequest, bwdo_pb2.GetDescriptionReponse), \
  'GET_PROFILE': (bwdo_pb2.GetProfileRequest, bwdo_pb2.GetProfileResponse), \
  'GET_CHALLENGES_LIST': (bwdo_pb2.GetChallengesListRequest, bwdo_pb2.GetChallengesListResponse), \
  'POST_PROFILE': (bwdo_pb2.CreateProfileDORequest, bwdo_pb2.CreateProfileDOResponse), \
  'POST_SUBMIT_CHALLENGE': (bwdo_pb2.SubmitChallengeDORequest, bwdo_pb2.SubmitChallengeDOResponse), \
  'POST_SOLVE_CHALLENGE': (bwdo_pb2.SolveChallengeDORequest, bwdo_pb2.SolveChallengeDOResponse), \
}

SUCCESS = True
FAILURE = False

def parseData(data):
  res = {}
  if data is None or data == '':
      res['status'] = FAILURE
      res['err_msg'] = "data field empty!"
      return res 

  raw_data = base64.b64decode(data)
  try: 
      req_msg = bwdo_pb2.Message()
      req_msg.ParseFromString(raw_data)
  except:
      res['status'] = FAILURE
      res['err_msg'] = "Unable to decode request message!"
      return res
  
  req_type = req_msg.type
  if req_type not in req_types_dict.keys():
      res['status'] = FAILURE
      res['err_msg'] = "Request type invalid!"
      return res 

  try:
      req_obj = req_types_dict[req_type][REQ]()
      req_obj.ParseFromString(raw_data)
  except DecodeError, e:
      res['status'] = FAILURE
      res['err_msg'] = "Unable to decode request message!"
      return res

  res['req'] = req_obj
  res['status'] = SUCCESS
  res['type'] = req_type
  res['err_msg'] = ''
  res['req_msg_id'] = req_msg.id
  return res

def processRequest(req_obj):

  req_type = req_obj.type
  res = {}
# TODO: get response object based on request type. This involves fetching data from db and populating the proto objects
  if req_type == GET_DESCRIPTION:
      res['user'] = req_obj.user
      res['challenge'] = req_obj.challenge
  if req_type == GET_PROFILE:
      res['user'] = req_obj.user
  if req_type == GET_CHALLENGES_LIST:
      res['user'] = req_obj.user
      res['filter'] = req_obj.filter
  if req_type == POST_PROFILE:
      res['user'] = req_obj.user
  if req_type == POST_SUBMIT_CHALLENGE:
      res['user'] = req_obj.user
      res['challenge'] = req_obj.challenge
  if req_type == POST_SOLVE_CHALLENGE:
      res['user'] = req_obj.user
      res['challenge'] = req_obj.challenge
 
  res['status'] = SUCCESS
  return res
  

def generateResponse(raw_data, msg_id, req_type):
  
  message = bwdo_pb2.Message()
  message.id = msg_id
  message.type = req_type
  message.status_code = 0
  message.payload = raw_data
  return message    


class RequestHandler(BaseHandler):
  def read(self, request, test=None):
    data = request.GET.get('data', '')
    parsed_data = parseData(data)
    if parsed_data['status'] == FAILURE:
        return sendErrResp(parsed_data['err_msg'])  
    resp_raw_data = processRequest(parsed_data['req'])
    if resp_raw['status'] == FAILURE:
        return sendErrResp(resp_raw['err_msg'])  
   
    resp_msg = generateResponse(resp_raw['data'], parsed_data['req_msg_id'], parsed_data['type'])
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"data": base64.b64encode(resp_msg.SerializeToString())}
    resp.content = respDict
    return resp

  def create(self, request, test=None):
    data = request.POST['data']
    parsed_data = parseData(data)
    if parsed_data['status'] == FAILURE:
        return sendErrResp(parsed_data['err_msg'])  
    resp_raw_data = processRequest(parsed_data['req'])
    if resp_raw['status'] == FAILURE:
        return sendErrResp(resp_raw['err_msg'])  
   
    resp_msg = generateResponse(resp_raw['data'], parsed_data['req_msg_id'], parsed_data['type'])
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"data": base64.b64encode(resp_msg.SerializeToString())}
    resp.content = respDict
    return resp

