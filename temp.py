import datetime

print (datetime.datetime.now())

str = str(datetime.datetime.now())
print(type(str))
print(str.replace("-", "_").replace(":","_").replace(".","_").replace(" ","_"))

str = datetime.datetime.now().date()
print(str)
