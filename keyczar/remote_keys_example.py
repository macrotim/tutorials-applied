"""This is a demonstration to enable keyczar with a set of keys stored on a remote site.

Step-1: Create a new key set.
$ mkdir -p /tmp/kz
$ keyczart create --location=/tmp/kz --purpose=crypt
$ keyczart addkey --location=/tmp/kz --status=primary

Step-2: Create a tarfile.
$ cd /tmp/kz
$ tar cvzf /tmp/keyczar-tutorial-key.tgz *

Step-3: Upload to S3 and make it publicly readable.

Step-4: python remote_keys_example.py
"""

import tarfile
import urllib

from keyczar import keyczar

# The keyset is stored on S3.
REMOTE_KEY_LOCATION = "https://s3-us-west-1.amazonaws.com/one-tinker/keyczar-tutorial-key.tgz"

# Download the keys and unpack.
key_location = "/tmp/keyczar-tutorial-key"
tar_name = key_location + ".tgz"
urllib.urlretrieve(REMOTE_KEY_LOCATION, tar_name)
with tarfile.open(tar_name, "r:gz") as tar:
    tar.extractall(key_location)

# Lets test it out. Encrypt and decrypt a string.
s = 'secret string'
crypter = keyczar.Crypter.Read(key_location)
s_encrypted = crypter.Encrypt(s)
s_decrypted = crypter.Decrypt(s_encrypted)
print s
print s_encrypted
print s_decrypted
