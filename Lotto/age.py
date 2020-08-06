 # Sinothando Bacela
# Class 1
# Python Mini Project
# Checking the age

def getUser_age():
    # initialize user's age as not verified(false)
    user_age = False
    # while user's age is not True
    while not user_age:
        # enter your age
        age = int(input("Enter your age: "))
        try:
            # check if age is an interger
            age = int(age)
            # chech if user's age is < 18
            if age < 18:
                #end programme
                print("Only players 18 years and above are allowed to play Goodbye!")
                return False
            else:
                #otherwise if age >= 18
                print("Welcome To National Lottery of South Africa")
                user_age = True
        except ValueError:
            print("Number must be a whole number!Try again.")
    '''
    >>> ager = getUser_age()
    Enter your age: 21
    Welcome To National Lottery of South Africa
    >>> ager = getUser_age()
    Enter your age: 16
    Only players 18 years and above are allowed to play Goodbye!
    '''
    # return True for verified age
    return user_age
