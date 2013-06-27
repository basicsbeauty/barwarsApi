from piston.handler import BaseHandler
from piston.utils import rc
from proto import bwdo_pb2
import subprocess

import MySQLdb as db

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
  bwdo_pb2.GET_DESCRIPTION:       (bwdo_pb2.GetDescriptionRequest, bwdo_pb2.GetDescriptionResponse), \
  bwdo_pb2.GET_PROFILE:           (bwdo_pb2.GetProfileRequest, bwdo_pb2.GetProfileResponse), \
  bwdo_pb2.GET_CHALLENGES_LIST:   (bwdo_pb2.GetChallengesListRequest, bwdo_pb2.GetChallengesListResponse), \
  bwdo_pb2.POST_PROFILE:          (bwdo_pb2.CreateProfileDORequest, bwdo_pb2.CreateProfileDOResponse), \
  bwdo_pb2.POST_SUBMIT_CHALLENGE: (bwdo_pb2.SubmitChallengeDORequest, bwdo_pb2.SubmitChallengeDOResponse), \
  bwdo_pb2.POST_SOLVE_CHALLENGE:  (bwdo_pb2.SolveChallengeDORequest, bwdo_pb2.SolveChallengeDOResponse), \
}

SUCCESS = True
FAILURE = False

db_cursor = None

#########################################################################
# Log: Function
#########################################################################
def logLine( message):
    fp_log = open( "/tmp/barwars.log", "a")
    fp_log.write( message + "\n")
    fp_log.close()
    return

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
    
    logLine( "DB: Connection: Create: Success:")

  except db.error, e:
    db_cursor = None
    print "DB creation error: ", e

  return db_cursor

#########################################################################
# Parse: Request 
#########################################################################
def parseData(data):
  res = {}
  if data is None or data == '':
      res['status'] = FAILURE
      res['err_msg'] = "data field empty!"
      return res 

  raw_data = base64.b64decode(data)
  logLine( "Deco: " + str(raw_data))
  try: 
      req_msg = bwdo_pb2.Message()
      req_msg.ParseFromString(raw_data)
      logLine( "R Ms: " + str(req_msg));
  except:
      res['status'] = FAILURE
      res['err_msg'] = "Unable to decode request message!"
      return res
  
  logLine( "Type: " + str(req_msg.type))  
  req_type = req_msg.type
  if req_type not in req_types_dict.keys():
      res['status'] = FAILURE
      res['err_msg'] = "Request type invalid!"
      return res 

  try:
      logLine( "R_Pa: " + str(req_msg.payload.raw_payload))
      req_obj = req_types_dict[req_type][REQ]()
      logLine( "R Do: " + str(req_obj))
      req_obj.ParseFromString( req_msg.payload.raw_payload)
      logLine( "Req : Obj : " + str(req_obj))
  except bwdo_pb2.DecodeError, e:
      res['status'] = FAILURE
      res['err_msg'] = "Unable to decode request message!"
      return res

  res['req'] = req_obj
  res['status'] = SUCCESS
  res['type'] = req_type
  res['err_msg'] = ''
  res['req_msg_id'] = req_msg.id
  return res

#########################################################################
# Request: Profile: Get: Process:
#########################################################################
def processProfileGet( db_cursor, user_do = None, challenge_do = None):
  
  logLine( "Profile: Get: Process: BEGN: " + str(user_do))

  try:

    logLine( "UUID: " + user_do.uuid)

    # Query:
    table = 'user'
    column_list = ' uuid, profile_name, points, solved_count, submit_count'
    query  = 'select ' + column_list + ' from ' + table + ' where '
  
    if user_do.uuid:
      query += 'uuid like \'' + str(user_do.uuid) + '\' '

    logLine( query)
    db_cursor.execute( query)            
    
    db_record = db_cursor.fetchall()
    logLine( "DBRs:" + str(db_record))
    db_record = db_record[0]
    logLine( "Rs 0:" + str(db_record))

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

  return profile_response.SerializeToString()

#########################################################################
# Request: Description: Get: Process:
#########################################################################
def processDescriptionGet( user_do = None, challenge_do = None):

  upc = challenge_do.bar_code
  print "upc : ", upc
  cmdline = "curl http://www.upcdatabase.com/item/" + upc + " --silent | grep 'Description' | cut -c 38- | cut -d'<' -f 1"
  print "cmdline:: ", cmdline
  try: 
    result = subprocess.check_output(cmdline, shell=True)
  except subprocess.CalledProcessError:
    result = "";

  if result == "":
    return None
  else:
    description_response = bwdo_pb2.GetDescriptionResponse()
    
    ch_do = description_response.challenge
    
    ch_do.bar_code = upc
    ch_do.description = result
  
  return description_response.SerializeToString()

#########################################################################
# Request: Process: Global 
#########################################################################
def processRequest(req_obj, req_type):

  logLine( "Rqst: Prcs: I/p : Type: " + str(req_type) + " RQST: " + str(req_obj))

  res = {}

  cursor = getDBCursor()
  if not cursor:
     res['status'] = FAILURE
     res['err_msg'] = "DB Access: Failed"
     return res

# TODO: get response object based on request type. This involves fetching data from db and populating the proto objects
  if req_type == bwdo_pb2.GET_DESCRIPTION:
      res['r_payload'] = processDescriptionGet( challenge_do = req_obj.challenge)
  if req_type == bwdo_pb2.GET_PROFILE:
      logLine("Profile: Get: Switch:" + str(req_obj))
      res['r_payload'] = processProfileGet( cursor, user_do = req_obj.user)
  if req_type == bwdo_pb2.GET_CHALLENGES_LIST:
      res['user'] = req_obj.user
      res['filter'] = req_obj.filter
  if req_type == bwdo_pb2.POST_PROFILE:
      res['user'] = req_obj.user
  if req_type == bwdo_pb2.POST_SUBMIT_CHALLENGE:
      res['user'] = req_obj.user
      res['challenge'] = req_obj.challenge
  if req_type == bwdo_pb2.POST_SOLVE_CHALLENGE:
      res['user'] = req_obj.user
      res['challenge'] = req_obj.challenge
 
  res['status'] = SUCCESS
  return res
  

def generateResponse(raw_data, msg_id, req_type):
  
  message = bwdo_pb2.Message()
  message.version = 1
  message.id = msg_id
  message.type = req_type
  message.status_code = 0
  message.payload.raw_payload = raw_data
  return message    

def sendErrResp( err_msg):
    resp = rc.BAD_REQUEST
    resp['Content-Type'] = 'text/json'
    respDict = {"message": err_msg}
    resp.content = respDict
    return resp

class RequestHandler(BaseHandler):
  def read(self, request, test=None):
    data = request.GET.get('data', '')
    logLine( "B 64: " + str( data))
    parsed_data = parseData(data)
    logLine( "Pars: " + str(parsed_data))
    if parsed_data['status'] == FAILURE:
        return sendErrResp(parsed_data['err_msg'])
    
    ##############################################
    # Process: Request
    ##############################################    	
    resp_raw = processRequest(parsed_data['req'], parsed_data['type'])
    logLine( "RaRs: " + str(resp_raw))
    if resp_raw['status'] == FAILURE:
        return sendErrResp(resp_raw['err_msg'])  

    ##############################################
    # Response: Construct
    ##############################################	   
    logLine( "Pars: " + str(resp_raw))
    resp_msg = generateResponse( resp_raw['r_payload'], parsed_data['req_msg_id'], parsed_data['type'])
    
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
    resp_raw = processRequest(parsed_data['req'])
    if resp_raw['status'] == FAILURE:
        return sendErrResp(resp_raw['err_msg'])  
   
    resp_msg = generateResponse(resp_raw['req'], parsed_data['req_msg_id'], parsed_data['type'])
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"data": base64.b64encode(resp_msg.SerializeToString())}
    resp.content = respDict
    return resp

