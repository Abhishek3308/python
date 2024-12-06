user=input("user name:")
if user.isalnum() and 6 <= len(user) <=15:
    print("valid username:")
else:
    print("invalid username")