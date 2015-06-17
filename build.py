#!/usr/bin/python

import json

policy = dict()

for source in ["common", "cinder", "glance", "nova", "keystone" ]:
    filename = "%s-policy.json" % source
    with open(filename, 'r') as f:
        text = f.read()
        rules = json.loads(text)
        policy.update(rules)
        print ("reading " + filename)


outfilename = "policy.json"
print ("writing " + outfilename)

with open(outfilename,'w') as outfile:
    json.dump(policy, outfile, sort_keys=True,
               indent=4, separators=(',', ': '))

        
#print (json.dumps(policy))
