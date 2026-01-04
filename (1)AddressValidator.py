def addressval(address):
    dot = address.find('.')
    at = address.find('@')

    if dot == -1 or at == -1:
        print("Not Valid ❌")
    else:
        print("Valid ✅")


print("This program will decide if your email address is valid or not.")
print("Your email address needs '@' and '.' to be valid.")

while True:
    x = input("\nEnter an email address (or type 'quit' to exit): ")

    if x.lower() == "quit":
        print("Goodbye! 👋")
        break

    addressval(x)
