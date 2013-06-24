
from django.conf.urls.defaults import *
from piston.resource import Resource
#from v1.handlers import ProfileHandler
#from v1.handlers import ChallengeHandler
#from v1.handlers import ChallengeSolveHandler
#from v1.handlers import UpcHandler
from v1.handlers import RequestHandler 
from v1.handlers import DescriptionHandler
from v1.handlers import ChallengeListHandler
from v1.handlers import ChallengeSubmitHandler
from v1.handlers import ChallengeSolveHandler

class CsrfExemptResource( Resource ):
  def __init__( self, handler, authentication = None ):
    super( CsrfExemptResource, self ).__init__( handler, authentication )
    self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

#profile_handle = CsrfExemptResource( ProfileHandler )
#challenge_handle = CsrfExemptResource( ChallengeHandler )
#challenge_solve_handle = CsrfExemptResource( ChallengeSolveHandler )
#upc_handle = CsrfExemptResource( UpcHandler )
request_handle = CsrfExemptResource( RequestHandler )

urlpatterns = patterns( '',
  #url( r'^profile/(\d+)/$', profile_handle),
  #url( r'^challenge/$', challenge_handle),
  #url( r'^upc/(\d+)/$', upc_handle),
  #url( r'^challenge/(\d+)/solve/$', challenge_solve_handle),
  url( r'^req/$', request_handle),
)

