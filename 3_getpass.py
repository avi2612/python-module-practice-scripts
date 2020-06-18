import getpass

username=getpass.getuser() # get username from env
password=getpass.getpass(prompt="Enter your password ")

print(f"Your username is {username} and password is {password}")