#!/usr/bin/python

import json

policy = dict()

for source in ["common", "cinder", "glance", "nova" ]:
    filename = "%s-policy.json" % source
    with open(filename, 'r') as f:
        text = f.read()
        rules = json.loads(text)
        policy.update(rules)
        print (filename)
        #if source == "glance":
        #    print (rules)
        #    print (policy)
print (json.dumps(policy, sort_keys=True,  indent=4, separators=(',', ': ')))

        
#print (json.dumps(policy))
