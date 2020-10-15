# # load OpenSSL.crypto
import OpenSSL
from OpenSSL import crypto

# open it, using password. Supply/read your own from stdin.
p12 = crypto.load_pkcs12(open("ISARA_client.p12", 'rb').read(), b'')

# get various properties of said file.
# note these are PyOpenSSL objects, not strings although you
# can convert them to PEM-encoded strings.
c = p12.get_certificate()     # (signed) certificate object
p_key = p12.get_privatekey()      # private key.
chain = p12.get_ca_certificates() # ca chain.
cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, c)
print("Private Key: ",p_key)
print("Chain: ",chain)
print("Version: ",c.get_version())
print("Signature algorithm: " ,c.get_signature_algorithm())
print("Serial Number: ", c.get_serial_number()) 
print("Has Expired: ", c.has_expired())
print("Not Before date: ", c.get_notBefore())
print("Not After date: ", c.get_notAfter())
subject = c.get_subject()
print("Subject Components: ", subject.get_components())
issuer = c.get_issuer()
print("Issuer: ", c.get_issuer())
print("Issuer Components: ", issuer.get_components())
