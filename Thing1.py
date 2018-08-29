import base64
 
with open("t.jpg", "rb") as imageFile:
	str = base64.b64encode(imageFile.read())
	print (str)
	
decode=base64.decodebytes (str)
anythingbutx = int("".join(["{:08b}".format(x) for x in decode]))
print (anythingbutx)
b = anythingbutx*anythingbutx
b = bin(b)
print (b)