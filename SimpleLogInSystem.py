accounts = {"kenangelo100" : "kenangelosy", "ken100" : "ken"}

username = input("Enter your username: ")
password = input("Enter the password for " + username + ": ")

if (accounts.get(username) == password):
    print("Login Succesful")
    test = input(".") 
else:
    print("Login Failed")