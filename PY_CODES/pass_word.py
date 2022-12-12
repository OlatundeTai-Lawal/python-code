print("# ***This is a code to check for password authentication***\n")
user_password = {
"ronaldo":"lisbon",
"messi":"paris",
"mbape":"paris",
}
username = ""  #initialize the loop
password = ""
attempt = 0
#start the while loop
while attempt <= 5:
    username = input("enter username\n").lower()
    password = input("enter password\n").lower()
    attempt += 1
    if username in user_password and user_password[username]==password:
        print("access granted")
        break
    else:
        print("try again")
    if attempt >= 5:
        print("your account is locked")
        break



