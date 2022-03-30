Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#THis is MD5 hashing example for encoding strings
import hashlib
string = "Congratulations Mathews,you passed our test!"
encoded=string.encode()
result = hashlib.md5(encoded)
print("String : ", end ="")
String : 
print(string)
Congratulations Mathews,you passed our test!
print("Hash Value : ", end ="")
Hash Value : 
print(result)
<md5 _hashlib.HASH object @ 0x00000174DF9E2C30>
print("Hexadecimal equivalent: ",result.hexdigest())
Hexadecimal equivalent:  6e28276e52c0cf21ed5e444cc342c169
