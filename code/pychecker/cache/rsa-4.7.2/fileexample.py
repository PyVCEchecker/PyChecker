import rsa

pubkey, privkey = rsa.newkeys(512)

with open('bothkeys.pem', 'wb') as pemfile:
    pemfile.write(pubkey.save_pkcs1())
    pemfile.write(privkey.save_pkcs1())
