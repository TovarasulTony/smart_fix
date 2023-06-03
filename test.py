
import datetime

var = datetime.datetime.now()
var = str(var)

print("-------------")
print(var)
print(type(var))

exe = var[:4] + var[5:7] + var[8:10] + '-' + var[10:]
print(exe)