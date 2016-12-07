#!/usr/bin/python
import sys
import logging 
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Photography_Proj")

from Photography_Proj import as application
application.secret_key = "ragingjellyfish"
