import base64

from Crypto.Cipher import AES


def descrypt_passwd(passwd):
    passwd = base64.b64decode(passwd)
    key = "2021202220212018".encode('utf8')
    iv = "2022201920202018".encode('utf8')
    aes = AES.new(key, AES.MODE_CBC, iv)
    dpasswd = aes.decrypt(passwd)
    dpasswd=dpasswd.decode()
    return dpasswd
