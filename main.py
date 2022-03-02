import instaloader
import os
import getpass

# Get instance
L = instaloader.Instaloader()

# Set window title
os.system("INSTATOOLS")

logged = False
logged_as = ""
password = ""
running = True



while running:
    os.system("cls")
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
    print("5. Check someone's account followers or followings")
    print("6. Quit the script")
    print("")
    print("")

    choice = int(input("Enter a number : "))

    os.system("cls")

    if choice == 1:
        logged_as = str(input("Enter your username : "))
        os.system("cls")
        password = getpass.getpass(prompt="Enter your password : ")
        os.system("cls")
        logged = True
        try:
            L.login(logged_as, password)
        except : 
            print("Either your username or password is incorrect. Please try again.")
            logged = False
            os.system("pause")

    if choice == 2:
        print("Might take some seconds...")

        following_list = []
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Print list of following
        for followee in profile.get_followees():
            following_list.append(followee.username)
        
        os.system("cls")
        print(", ".join(following_list))
        os.system("pause")
    
    if choice == 3:
        print("Might take some seconds...")

        followers_list = []
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Print list of followers
        for follower in profile.get_followers():
            followers_list.append(follower.username)
        
        os.system("cls")
        print(", ".join(followers_list))
        os.system("pause")
    
    if choice == 4:
        print("Might take up to a minute but it's worth it ;)")

        no_follow_back = []
        
        followers_list = []
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Print list of followers
        for follower in profile.get_followers():
            followers_list.append(follower.username)
        
        following_list = []
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, logged_as)

        # Print list of following
        for followee in profile.get_followees():
            following_list.append(followee.username)

            if followee.username in followers_list:
                pass
            else:
                no_follow_back.append(followee.username)

        os.system("cls")
        print(", ".join(no_follow_back))
        os.system("pause")
    
    if choice == 6:
        quit()
