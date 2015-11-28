"""Enable keyczar with a set of keys stored on a remote site.

   Step-1: Create a new key set.
   $ mkdir -p /tmp/kz
   $ keyczart create --location=/tmp/kz --purpose=crypt
   $ keyczart addkey --location=/tmp/kz --status=primary

   Step-2: Create a tarfile.
   $ cd /tmp/kz
   $ tar cvzf /tmp/keyczar-tutorial-key.tgz *

   Step-3: Upload to S3 and make it publicly readable.
   In a production setting, you want to allow only your account
   to read it.

   Step-4: python remote_keys.py
   """

import tarfile
import urllib

from keyczar import keyczar

# The keyset must be saved to S3.
REMOTE_KEY_LOCATION = "https://s3-us-west-1.amazonaws.com/one-tinker/keyczar-tutorial-key.tgz"

def setup_crypter():
    """Return the keyczar crypter."""

    # Download the keys and unpack.
    key_location = "/tmp/keyczar-tutorial-key"
    tar_name = key_location + ".tgz"
    urllib.urlretrieve(REMOTE_KEY_LOCATION, tar_name)
    with tarfile.open(tar_name, "r:gz") as tar:
        tar.extractall(key_location)

    return keyczar.Crypter.Read(key_location)

def demo(s):
    """Do a basic exercise with the crypter."""

    crypter = setup_crypter()
    s_encrypted = crypter.Encrypt(s)
    s_decrypted = crypter.Decrypt(s_encrypted)
    print 'Original string:', s
    print 'Encrypted string:', s_encrypted
    print 'Decrypted string:', s_decrypted
    return s_encrypted, s_decrypted

if __name__ == '__main__':
    s = 'secret string'
    demo(s)
