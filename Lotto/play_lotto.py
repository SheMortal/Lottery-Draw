# Sinothando Bacela
# Class 1
# Python Mini Project
import random


# Function to generate random Lotto numbers
def getLottoNums():
    # initialize empty list for the random lotto numbers
    lott_numbers = []
    # generate 6 random numbers and append to the empty list
    for i in range(0, 6):
        num = random.randint(1, 49)
        while num in lott_numbers:
            num = random.randint(1, 49)
        lott_numbers.append(num)
    # sort numbers in ascending order
    lott_numbers.sort()
    # doctest
    '''
    >>> lotto = getLottoNums()
    >>> print(lotto)
    [11, 14, 16, 32, 36, 47]
    >>> lotto = getLottoNums()
    >>> print(lotto)
    [6, 11, 22, 27, 30, 42]
    '''
    #return lotto numbers
    return lott_numbers


def getUserSelection():
    # initialize empty list for the user's numbers
    selection_num = []

    # while user numbers are less than 6
    while len(selection_num) < 6:
        # ask for user input
        selection = int(input("Please enter a number between 1 and 49: "))
        # input validation
        try:
            # check if number is an integer
            selection = int(selection)
            # if number is between 1 and 49
            if 1 <= selection <= 49:
                # if number is not in the user's list
                if selection not in selection_num:
                    # append number to the user's list
                    selection_num.append(selection)
                else:
                    # if it's already in the list
                    print("Error! Pick a unique number: ")
            else:
                #otherwise if number is not 1 <= selection <= 49
                print(" Sorry! Your number was not in range!")
        except ValueError:
            print("Number must be an integer!Please enter a number between 1 and 49: ")

    # sort the user's numbers in ascending order
    selection_num.sort()
    # doctest
    '''
    >>> user_selection = getUserSelection()
    Please enter a number between 1 and 49: 21
    Please enter a number between 1 and 49: 3
    Please enter a number between 1 and 49: 45
    Please enter a number between 1 and 49: 23
    Please enter a number between 1 and 49: 47
    Please enter a number between 1 and 49: 32
    >>> print(user_selection)
    [3, 21, 23, 32, 45, 47]
    >>> user_selection = getUserSelection()
    Please enter a number between 1 and 49: 12
    Please enter a number between 1 and 49: 12
    Error! Pick a unique number: 
    Please enter a number between 1 and 49: 79
    Sorry! Your number was not in range!
    Please enter a number between 1 and 49: 54
    Sorry! Your number was not in range!
    Please enter a number between 1 and 49: 12
    Error! Pick a unique number: 
    Please enter a number between 1 and 49: 32
    Please enter a number between 1 and 49: 11
    Please enter a number between 1 and 49: 15
    Please enter a number between 1 and 49: 63
    Sorry! Your number was not in range!
    Please enter a number between 1 and 49: 31
    Please enter a number between 1 and 49: 20
    >>> print(user_selection)
    [11, 12, 15, 20, 31, 32]
    '''
    # return the user's predictions
    return selection_num


def correct_guess(selection_num, lott_numbers):
    correct_guesses = 0
    # for each number in user's predictions
    for number in selection_num:
        # if number is in both lotto list
        if number in lott_numbers:
            # add one to correct_guesses
            correct_guesses += 1
    # doctest
    '''
    >>> lotto = getLottoNums()
    >>> user_selection = getUserSelection()
    Please enter a number between 1 and 49: 21
    Please enter a number between 1 and 49: 3
    Please enter a number between 1 and 49: 45
    Please enter a number between 1 and 49: 23
    Please enter a number between 1 and 49: 47
    Please enter a number between 1 and 49: 32
    >>> print(lotto)
    [2, 10, 20, 32, 38, 45]
    >>> print(user_selection)
    [3, 21, 23, 32, 45, 47]
    >>> correct_predictions = correct_guess(user_selection, lotto)
    >>> print(correct_predictions)
    2
    '''
    # return the number of correct guesses
    return correct_guesses


def total_amount(correct_guesses):
    # dictionary for the prize values

    prizes = {
        0: 0,
        1: 0,
        2: 20.00,
        3: 100.50,
        4: 2384.00,
        5: 8584.00,
        6: 10000000.00
    }

    amount = prizes[correct_guesses]
    # doctest
    '''
    >>> lotto = getLottoNums()
    >>> user_selection = getUserSelection()
    Please enter a number between 1 and 49: 21
    Please enter a number between 1 and 49: 3
    Please enter a number between 1 and 49: 45
    Please enter a number between 1 and 49: 23
    Please enter a number between 1 and 49: 47
    Please enter a number between 1 and 49: 32
    >>> print(lotto)
    [2, 10, 20, 32, 38, 45]
    >>> print(user_selection)
    [3, 21, 23, 32, 45, 47]
    >>> correct_predictions = correct_guess(user_selection, lotto)
    >>> tot_amount = total_amount(correct_predictions)
    >>> print(tot_amount)
    20.0
    '''
    # return the total amount
    return amount
