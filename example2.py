#!python3
import json
'''
JSON (Javascript object notation) is a handy method of converting
complex data structures like lists or dictionaries to string literal
values so that they can be transferred to another program or file.

The file can then be read and decoded as necessary.

'''
x = 10
y = 3

file = open('example2.txt','w')
file.write(x)
file.write(y)
file.close()

'''
Note that if you try to run this program, it will crash because the .write()
command can only write str values, not integers!
Change 15 and 16 to 
file.write(f"{x}\n")
file.write(f"{y}\n")
to make this program run properly.  Why is the \n needed at the end of the string?
'''
exit()





z = ['Hello','world']
outputData = json.dumps(z)

print(type(z))
print(type(outputData))

file = open('example2.txt','w')
file.write(f"{outputData}")
file.close()

readfile = open('example2.txt','r')
newList = readfile.read()
jsonList = json.loads(newList)
print(type(newList))
print(type(jsonList))
print(jsonList)
print(jsonList[0])
