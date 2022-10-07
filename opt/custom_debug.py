#!/usr/bin/python

try:
    import json
except ImportError:
    import simplejson as json
    
from ansible.module_utils.basic import AnsibleModule
import time
import sys

DOCUMENTATION = '''
---
module: custom_debug
short_description: A custom debug module
description:
  - print custom dabug message
version_added: 0.1
author: Mumshad Mannambeth, @mmumshad
notes:
requirements:
options:
  msg:
    description: Message to print
    required: True
'''

EXAMPLES = '''
# Example
custom_debug:
    msg: This is test message
'''

def main():
    module - AnsibleModule (
        argument_spec = dict(
            msg=dict(required=True, type='str')
        )
    )
    
    msg = module.params['msg']
    
    # Successfull Exit
    try:
#        print(json.dumps({
#            msg: '%s #%s' % (time.strftime("%c"), msg),            "changed": TRUE
#        }))
#        sys.exit(0)
        module.exit_json(changed=True, msg='%s - %s' % (time.strftime("%c"), msg))
    except:
    # Fail Exit
#        print (json.dumps({
#           "failed": TRUE,
#           "msg": "failed debugging"
#        }))
#        sys.exit(1)
        module.fail_json(msg="Error Message: failed debugging"))
if __name__ == '__main__':
    main()