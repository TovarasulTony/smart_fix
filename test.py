from fix_fields import Fix

app = Fix()
msg = app.make_login()
msg = msg.replace("\x01", "|")
print(msg[:-5])

