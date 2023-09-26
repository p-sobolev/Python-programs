import json

# d contains usernames and their passwords;
# emails contains usernames and their email addresses
# text files you open should contain the information as follows:
# users_passwords.txt: {'username1': 'password', 'username2': 'password'};
# users_emails.txt: {'username1': 'email', 'username2': 'email'};


# converts string dictionary to dictionary
rhandle = open("users_passwords.txt")
for line in rhandle:
    line = line.replace("'", '"')
    d = json.loads(line)

rEmailsHandle = open("users_emails.txt")
for line in rEmailsHandle:
    line = line.replace("'", '"')
    emails = json.loads(line)

attempts = int(3)  # counts authentication attempts left



username = input("enter your username: ")
if username in d and emails:
    password = input("enter your password: ")
    while password != d[username]:
        if attempts == 0:
            print("You've run out of attempts")
            exit()
        else:
            print(f"the password is incorrect; try again; attmepts left: {attempts}")
            attempts = attempts - 1
            password = input("enter your password: ")
    else:
        print("Welcome back!", username)
        if username == "admin":
            page_navigation = input("type [delete] to delete your profile; type[announce] to print text; type[profiles] to list all accounts: ")
            if page_navigation == "delete":
                print("this action is not possible")
            elif page_navigation == "profiles":
                print(d)
                print(emails)
                remove = input("which profile do you wish to remove?: ")
                if remove in d:
                    del d[remove]
                    try:
                        del emails[remove]
                    except:
                        pass
                else:
                    print("this profile doesn't exist")
                    pass
        else:
            page_navigation = input("type [delete] to delete your profile; type[announce] to print text: ")
            if page_navigation == "delete":
                password = input("enter the password to confirm the action: ")
                if d[username] == password:
                    del d[username]
                    try:
                        del emails[username]
                    except:
                        pass
                    print("profile has been successfully deleted!")
                else:
                    print("this action is not possible")
                    pass
            else:
                print("Invalid input. Closing the page...")
else:
    print("there is no such user in the database. Do you want to sign up?")
    sign_up = input("Enter either[yes] or [no]: ")
    if sign_up == "no":
        pass
    elif sign_up == "yes":
        username = input("enter your username: ")
        while username in d:
            print("user with this name already exists")
            username = input("enter your username: ")
        else:
            mail = input("enter your email address: ")
            password1 = input("enter your password: ")
            password2 = input("confirm your password: ")
            while password1 != password2:
                print("passwords do not match; try again or enter [exit] to terminate the program")
                password1 = input("enter your password: ")
                if password1 == "exit":
                    exit()
                else:
                    password2 = input("confirm your password: ")
            d[username]=password1
            emails[username]=mail
            print("profile has been successfully created!")



whandle = open("users_passwords.txt", "w")
string = str(d)
print(string)
whandle.write(string)

wEmailsHandle = open("users_emails.txt", "w")
stringEmails = str(emails)
print(stringEmails)
wEmailsHandle.write(stringEmails)



