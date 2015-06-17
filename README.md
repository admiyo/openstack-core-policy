# openstack-core-policy

A unified approach to build a policy file
Each of the major proejcts gets its own sub file.
Common rules are merged with the proejct specific subfiles to
produce a single policy.json file.

Update the individual files, then run build.py to reproduce the unified file.