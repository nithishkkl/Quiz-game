
# yes to start the game
def start():
    playing=input("let's Start the game ?  (Yes or No) : ")
    if(playing.lower()=='yes'):
        print("Ok,Let's Play:) ")
    else:
        quit()
#login the game
def login():
    data = {
        'nithish': 'nithish2002',
        'vishwa': 'vish12345',
        'mukesh': 'mukesh123',
        'surya': 'surya2003',
    }
    print("*** Login your account ***")
    username = input("Please enter your username")
    password = input("Please enterr your password")
    if (username.lower(), password) in data.items():
        print("Login Successfull")
        start()
    else:
        print("Login is failed")

#creating a new account

def creating_account():
    print("Create a new account")
    FiratName = input("Enter your First Name : ")
    Last_name = input("Enter your Last Name : ")
    age=int(input("Enter your age : "))
    gender=input("Enter your Gender : ")
    phone_no = input("Enter your phone number : ")
    if len(phone_no) == 10:
        print('we will text a one-time code to verify your phone number ..')
        import random as r
        otp = ''
        for i in range(4):
            otp += str(r.randint(1, 9))
            import time as t
            t.sleep(0.1)
        print('Waiting for OTP', end='', flush=True)
        for _ in range(5):
            print('.', end='', flush=True)
            t.sleep(1)
        print('\n<#>Your verification code is:', otp)
        ot = (input('Please Enter OTP: '))
        print(ot)
        if ot == otp:
            print('Your Number has been verified....')
            t.sleep(0.1)
            start()
    else:
        print("Please Enter the phone number correctly : ")
        exit()




print("Welcome to our Quiz game ")
print("***Please login or create a new account to play the game***")
a=int(input("1.Login\n2.Create account\nEnter you option : "))
if(a==1):
    login()
elif(a==2):
    creating_account()



sum=0

print("1.What does CPU stand for? ")
print("A. Computer Processing Unit\nB. Central Processing Unit\nC. Computer Processing User\nD. Central Processing User")
answer=input("Enter your Answer : ")
if(answer.lower() =="central processing unit"):
    print("Correct!")
    sum=sum+1
else:
    print('Incorrect')

print("2.What is the full form of RAM? ")
print("A. Random Access Memory\nB. Read Access Memory\nC. Random Authorization Memory\nD. Read Authorization Memory")
answer=input("Enter your Answer : ")
if(answer.lower() =="random access memory"):
    print("Correct!")
    sum = sum + 1
else:
    print('Incorrect')

print("3.Which device is used to input data into a computer? ")
print("A. Monitor\nB. Printer\nC. Keyboard\nD. Speaker")
answer=input("Enter your Answer : ")
if(answer.lower() =="keyboard"):
    print("Correct!")
    sum = sum + 1
else:
    print('Incorrect')

print("4.Which component of a computer is responsible for storing data permanently?")
print("A. RAM\nB. CPU\nC. Hard Disk\nD. CD-ROM")
answer=input("Enter your Answer : ")
if(answer.lower() =="hard disk"):
    print("Correct!")
    sum = sum + 1
else:
    print('Incorrect')

print("5.What is the full form of USB?")
print("A. Universal Serial Bus\nB. United States of America Business\nC. User Serial Business\nD. Universal Serial Battery")
answer=input("Enter your Answer : ")
if(answer.lower() =="universal serial bus"):
    print("Correct!")
    sum = sum + 1
else:
    print('Incorrect')

print("6.What is the function of a modem in a computer?")
print("A. To connect to the Internet\nB. To print documents\nC. To store data\nD. To play music")
answer=input("Enter your Answer : ")
if(answer.lower() =="to connect to the internet"):
    print("Correct!")
    sum = sum + 1
else:
    print('Incorrect')

print("7.Which of the following is a type of software?")
print("A. Mouse\nB. Keyboard\nC. Operating System\nD. Monitor")
answer=input("Enter your Answer :  ")
if(answer.lower() =="Operating System"):
    print("Correct!")
    sum = sum + 1
else:
    print('Incorrect')

print("you got ",sum,"Question Correct")
print("Your percentage is ",((sum/7)*100),"%")



