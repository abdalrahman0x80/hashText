import hashlib
class HashText:
    def __init__(self,text):
        self.text = text.encode()
    def output(self):
        #--------------------------------------md5 hash--------------------------------------#
        print(f"hash md5 : {hashlib.md5(self.text).hexdigest()}")
        #--------------------------------------shasum hash--------------------------------------#
        print(f"hash sha1 :{hashlib.sha1(self.text).hexdigest()}")
        print(f"hash sha224 :{hashlib.sha224(self.text).hexdigest()}")
        print(f"hash sha256 :{hashlib.sha256(self.text).hexdigest()}")
        print(f"hash sha512 :{hashlib.sha512(self.text).hexdigest()}")
        print(f"hash sha224 :{hashlib.sha224(self.text).hexdigest()}")

class inhertFromHashText(HashText):
    pass
inputCode = input("text for HASH test--->> ")
text = inhertFromHashText(inputCode).output()
    
        