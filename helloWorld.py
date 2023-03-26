#See notes below
userName = input ("Hello! Please enter your facebook username!")
userPassword = input ("Hello! Please enter your facebook password!")
if(userName.lower() == "james" and userPassword == "MakeitEasy!"): print ("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")

#Line 2 and line 3 collect user name and password.
#Line 4 verifies desired name and password and prints welcome message.
#Lines 5 and 6 is the outcome when incorrect entries are made in lines 2 and / or 3.
