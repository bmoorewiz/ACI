import json
import requests
import pprint
import ijson

base_url = 'https://10.192.3.11/api/'

# create credentials structure
name_pwd = {'aaaUser': {'attributes': {'name': 'KOS6670', 'pwd': 'viper1!!'}}}
json_credentials = json.dumps(name_pwd)

# log in to API
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
get_url = base_url + 'mo/uni/tn-tn-HCA.json?query-target=subtree&target-subtree-class=fvBD&query-target-filter=eq(fvBD.limitIpLearnToSubnets,"no"'
response = requests.get(get_url, cookies=cookies, verify=False)
# Turn into JSON
jdata = json.loads(response.text)
#pprint.pprint(jdata)
logFile=open('/users/bmoore/Documents/python/hca'+'.txt', 'w')
pprint.pprint(jdata, logFile)