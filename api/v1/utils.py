import urllib
import base64
from proto import bwdo_pb2
from piston.utils import rc
import subprocess

SUCCESS = True
FAILURE = False
REQ = 0
RESP = 1
LOG_FILE="/tmp/barwars.log"

req_types_dict = {\
  bwdo_pb2.GET_DESCRIPTION:       (bwdo_pb2.GetDescriptionRequest, bwdo_pb2.GetDescriptionResponse), \
  bwdo_pb2.GET_PROFILE:           (bwdo_pb2.GetProfileRequest, bwdo_pb2.GetProfileResponse), \
  bwdo_pb2.GET_CHALLENGES_LIST:   (bwdo_pb2.GetChallengesListRequest, bwdo_pb2.GetChallengesListResponse), \
  bwdo_pb2.POST_PROFILE:          (bwdo_pb2.CreateProfileDORequest, bwdo_pb2.CreateProfileDOResponse), \
  bwdo_pb2.POST_SUBMIT_CHALLENGE: (bwdo_pb2.SubmitChallengeDORequest, bwdo_pb2.SubmitChallengeDOResponse), \
  bwdo_pb2.POST_SOLVE_CHALLENGE:  (bwdo_pb2.SolveChallengeDORequest, bwdo_pb2.SolveChallengeDOResponse), \
}



#########################################################################
# Log: Function
#########################################################################
def logLine( message):
  fp_log = open( LOG_FILE, "a")
  fp_log.write( message + "\n")
  fp_log.close()
  return


#########################################################################
# Parse: Request 
#########################################################################
def parseData( data, method = 'GET'):
  res = {}
  if data is None or data == '':
    res['status'] = FAILURE
    res['err_msg'] = "data field empty!"
    return res 

  logLine( "parseData:: raw req data: " + str(data))
  try:
    raw_data = urllib.unquote(data).decode('utf8')    
    raw_data = base64.b64decode(raw_data)
    req_msg = bwdo_pb2.Message()
    req_msg.ParseFromString(raw_data)
    logLine( "parseData:: deserialized req_msg: " + str(req_msg))
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
    req_obj.ParseFromString( req_msg.payload.raw_payload)
  except bwdo_pb2.DecodeError, e:
    res['status'] = FAILURE
    res['err_msg'] = "Unable to decode request message!"
    return res

  print "DONE"
  res['req'] = req_obj
  res['status'] = SUCCESS
  res['type'] = req_type
  res['err_msg'] = ''
  res['req_msg_id'] = req_msg.id
  return res

#########################################################################
# Util: Barcode -> Description
#########################################################################
def barcodeToDescription(upc):

  logLine("upc : " + str(upc))
  cmdline = "curl http://www.upcdatabase.com/item/" + upc + " --silent | grep 'Description' | cut -c 38- | cut -d'<' -f 1"
  logLine("cmdline:: "+ str(cmdline))
  try: 
    result = subprocess.check_output(cmdline, shell=True)
  except subprocess.CalledProcessError:
    result = None
  return result

#########################################################################
# Output: Message: Error Message
#########################################################################
def sendErrResp( err_msg):
  resp = rc.BAD_REQUEST
  resp['Content-Type'] = 'text/json'
  respDict = {"message": err_msg}
  resp.content = respDict
  return resp

#########################################################################
# Output: Message: Generate 
#########################################################################
def generateResponse(raw_data, msg_id, req_type):
  
  message = bwdo_pb2.Message()
  message.version = 1
  message.id = msg_id
  message.type = req_type
  message.status_code = 0
  message.payload.raw_payload = raw_data
  return message

