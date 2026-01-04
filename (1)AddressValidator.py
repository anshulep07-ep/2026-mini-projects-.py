def addressval(address):
    dot = address.find('.')
at = address.find('@')
if (dot == -1):
print("Not Valid:X")
elif(at == -1):
print("Not Valid:X")
else :
print("Valid")
print("This Program will decide if your email address is valid or not: ")
while True :
print("Your email adress needs'@' and '.' to be valid: ")

x = input("Enter a valid email adrress: ")
addressval(x)