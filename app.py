#!/usr/bin/python
"""import os

for k, v in os.environ.items(): 
    print "%s=%s" % (k, v) 

virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
"""
import web

web.config.debug = True
        
urls = (
    '/(.*)', 'Website'
)

app = web.application(urls, globals())

class Website:
    def GET(self, other):
        return "Yummi yummi baklava."


if __name__ == "__main__":
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8888))   
    
