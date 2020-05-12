def main():
    while True:
        incorrect, has_lower_case, has_number, has_special_char, has_upper_case = "0", "0", "0", "0", "0"
        user_name = input("Enter user name:")
        password = input("Enter password whose length can be more than 7 and less than 16:")

        # Check if password meets the length criteria
        if ((len(password) < 8) or (len(password) > 16)):
            print("Password length should be between 8-16")
            incorrect = "1"
        
        elif ((len(password) > 7) or (len(password) < 17)): 
            # to check if password has atleast one lowercase alphabet   
            for char in password:
                if char in "abcdefghijklmnopqrstuvwxyz":
                    has_lower_case = "1"
            # to check if password has atleast one uppercase alphabet   
            for char in password:
                if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    has_upper_case = "1"
            # to check if password has atleast one number  
            for char in password:
                if char in "0123456789":
                    has_number = "1"
            # to check if password has atleast one special character  
            for char in password:
                if char in "$#@":
                    has_special_char = "1"
            if ((has_lower_case == "1") and (has_number == "1") and (has_special_char == "1") and (has_upper_case == "1")):
                print("Successfully logged in")
            else:
                incorrect = "1"
                print("Please enter valid password. It should contain atleast one uppercase alphabet, one lowercase alphabet, one among ('$#@'), and one number") 
        # if password meets the criteria then break from the loop
        if (incorrect == "0"):
            break
        

if __name__=="__main__": 
    main()