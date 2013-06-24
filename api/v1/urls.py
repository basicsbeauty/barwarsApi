
from django.conf.urls.defaults import *
from piston.resource import Resource
from v1.handlers import RequestHandler 

class CsrfExemptResource( Resource ):
  def __init__( self, handler, authentication = None ):
    super( CsrfExemptResource, self ).__init__( handler, authentication )
    self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

request_handle = CsrfExemptResource( RequestHandler )

urlpatterns = patterns( '',
  url( r'^req/$', request_handle),
)

