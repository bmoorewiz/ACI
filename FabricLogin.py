import json
import urllib2
import ssl
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

postdata = json.dumps({"aaaUser": {"attributes": {"name": "KOS6670", "pwd": "viper1!!"}}})
urllib2.urlopen('https://10.192.3.11/api/aaaLogin.json', postdata,context=ctx)

header1.add("Cookie", "APIC-Cookie="+apicCookie);

response = requests.get('https://10.192.3.11/api/mo/uni/tn-tn-HCA.json?query-target=subtree&target-subtree-class=fvBD&query-target-filter=eq(fvBD.limitIpLearnToSubnets,"no"',verify=False)
todos = json.loads(response.text)
print todos
