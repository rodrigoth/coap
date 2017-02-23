import os
import sys
import time
import logging
import logging.handlers
import signal
from coap import coap, \
                 coapDefines as d, \
                 coapResource
IPADDRESS1 =  '2001:660:4701:6001:7116:9a6f:e92d:7f82'
RESOURCE   = 'res'
DUMMYVAL   = [0x01]


class dummyResource(coapResource.coapResource):
    
    def __init__(self):
        # initialize parent class
        coapResource.coapResource.__init__(self, path = RESOURCE,)

    #======================== parent methods ==================================
    
    def GET(self,options=[]):
        respCode        = d.COAP_RC_2_05_CONTENT
        respOptions     = []
        respPayload     = DUMMYVAL
        
        time.sleep(0.500)
        
        return (respCode,respOptions,respPayload)


    def POST(self,options=[],payload=[]):
        print "Oiiiiii"
        return (None,None,None)


coap1 = coap.coap(ipAddress=IPADDRESS1)
newResource = dummyResource()
coap1.addResource(newResource)

while True:
        input = raw_input("Done. Press q to close. ")
        if input=='q':
            print 'bye bye.'
            #c.close()
            os.kill(os.getpid(), signal.SIGTERM)