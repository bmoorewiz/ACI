import json
import requests
import pprint
import base64
import ijson
import sys

# Requires First Variable to be APIC IP, 2nd Variable Tenant name.

base_url = 'https://' + sys.argv[1] + '/api/'

# create credentials structure
name_pwd = {'aaaUser': {'attributes': {'name': 'KOS6670', 'pwd': base64.b64decode("dmlwZXIxISE=")}}}
json_credentials = json.dumps(name_pwd)

# log in to ACI
login_url = base_url + 'aaaLogin.json'
post_response = requests.post(login_url, data=json_credentials,verify=False)

# get token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

# create cookie array from token
cookies = {}
cookies['APIC-Cookie'] = auth_token

# perform a get, incorporating token in request
get_url = base_url + 'mo/uni/tn-' + sys.argv[2] + '.json?query-target=subtree&target-subtree-class=fvBD&rsp-subtree=full&query-target-filter=eq(fvBD.limitIpLearnToSubnets,"no"'
response = requests.get(get_url, cookies=cookies, verify=False)
# Turn into JSON
jdata = json.loads(response.text)

#Open Log File and PPRINT JSON for GREP
open('/users/bmoore/Documents/python/aci/hca/hca.txt', 'w').close()
logFile=open('/users/bmoore/Documents/python/aci/hca/hca.txt', 'w')
pprint.pprint(jdata, logFile)
logFile.close