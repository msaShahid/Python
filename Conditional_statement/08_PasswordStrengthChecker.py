password = "Passw0rd11!!"
checkPass = len(password)

if checkPass < 5:
    status = "Weak"
elif checkPass < 8:
    status = "Medium"
else:
    status = "Strong"
print(status)
 