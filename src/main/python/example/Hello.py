import os
import oci
print('Hello, world!')
print(os.environ)
print(oci.regions.REALMS)
oci.regions.REALMS[None] = 'oraclecloud.com'
print(oci.regions.REALMS)
