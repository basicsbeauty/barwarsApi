from piston.handler import BaseHandler
from piston.utils import rc

class ProfileHandler(BaseHandler):
  def read(self, request, test=None):
    resp = rc.ALL_OK
    resp['Content-Type'] = 'text/json'
    respDict = {"uid": 1234, "name": "Cowboy", "solve_count": 7, "submit_count": 10, "attempts": 25}
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

