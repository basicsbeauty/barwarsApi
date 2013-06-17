
from django.conf.urls.defaults import *
from piston.resource import Resource
from v1.handlers import ProfileHandler
from v1.handlers import ChallengeHandler
from v1.handlers import ChallengeSolveHandler

class CsrfExemptResource( Resource ):
  def __init__( self, handler, authentication = None ):
    super( CsrfExemptResource, self ).__init__( handler, authentication )
    self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

profile_handle = CsrfExemptResource( ProfileHandler )
challenge_handle = CsrfExemptResource( ChallengeHandler )
challenge_solve_handle = CsrfExemptResource( ChallengeSolveHandler )

urlpatterns = patterns( '',
  url( r'^profile/(\d+)/$', profile_handle),
  url( r'^challenge/$', challenge_handle),
  url( r'^challenge/(\d+)/solve/$', challenge_solve_handle),
)

