import instaloader
import os
import getpass
from sys import platform


if platform == "linux" or platform == "linux2":
    windows = False
elif platform == "darwin":
    windows = False
elif platform == "win32":
    windows = True

def clear():
    if windows:
        os.system("cls")
    else:
        os.system("clear")

clear()

def pause():
    if windows:
        os.system("pause")
    else:
        getpass.getpass(prompt="Press any key to continue . . .")


if windows:
    os.system("title LOADING...")


print("Loading, please wait...")

# Get instance
L = instaloader.Instaloader()

clear()

# Set window title
if windows:
    os.system("title INSTATOOLS")


logged = False
logged_as = ""
password = ""
running = True


while running:
    clear()
    print("WELCOME TO INSTATOOLS, PLEASE SELECT WHAT YOU WISH TO DO")
    print("")
    print("")

    if logged:
        print(f"Logged in as {logged_as}")
    else:
        print(f"1. Login")
    
    print("2. Check who are you following")
    print("3. Check who are your followers")
    print("4. Check who doesn't follow you back")
    print("5. Check someone's account followers or followings (Coming soon)")
    print("6. Quit the script")
    print("")
    print("")

    choice = int(input("Enter a number : "))

    clear()

    if choice == 1:
        logged_as = str(input("Enter your username : "))
        clear()
        password = getpass.getpass(prompt="Enter your password : ")
        clear()
        logged = True
        try:
            L.login(logged_as, password)
        except : 
            print("Either your username or password is incorrect. Please try again.")
            logged = False
            pause()

    if choice == 2:
        print("Might take some seconds...")
        print("")
        print("")

        following_list = []

        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Get number of following
        following_count = profile.followees

        # Counter
        counter = 0

        # Print list of following
        for followee in profile.get_followees():
            clear()
            following_list.append(followee.username)
            counter = counter + 1
            print("Might take some seconds...")
            print("")
            print("")
            print(f"{counter} / {following_count} following")
        
        clear()
        print(", ".join(following_list))
        print("")
        print("")
        pause()
    
    if choice == 3:
        print("Might take some seconds...")

        followers_list = []

        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Get number of followers
        followers_count = profile.followers

        # Counter
        counter = 0

        # Print list of followers
        for follower in profile.get_followers():
            clear()
            followers_list.append(follower.username)
            counter = counter + 1
            print("Might take some seconds...")
            print("")
            print("")
            print(f"{counter} / {followers_count} followers")

        clear()
        print(", ".join(followers_list))
        print("")
        print("")
        pause()
    
    if choice == 4:
        print("Might take up to a minute but it's worth it ;)")

        no_follow_back = []
        
        followers_list = []

        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # All profiles count
        all_count = profile.followers + profile.followees
        
        #Counter
        counter = 0

        # Print list of followers
        for follower in profile.get_followers():
            clear()
            print("Might take up to a minute but it's worth it ;)")
            followers_list.append(follower.username)
            counter = counter + 1
            print("")
            print("")
            print(f"{counter} / {all_count} all accounts")

        following_list = []

        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Print list of following
        for followee in profile.get_followees():
            following_list.append(followee.username)
            clear()
            print("Might take up to a minute but it's worth it ;)")
            counter = counter + 1
            print("")
            print("")
            print(f"{counter} / {all_count} all accounts")

            if followee.username in followers_list:
                pass
            else:
                no_follow_back.append(followee.username)

        clear()
        print(", ".join(no_follow_back))
        print("")
        print("")
        pause()
    
    if choice == 6:
        quit()
