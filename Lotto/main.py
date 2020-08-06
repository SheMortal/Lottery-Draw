# Sinothando Bacela
# Class 1
# Python Mini Project
# Function to play the lotto
# import all functions from other  files
from play_lotto import getUserSelection, getLottoNums, correct_guess, total_amount
from age import getUser_age
from textfile_write import write_file


def main():
    # verify the age
    if getUser_age() is True:
        # get lotto numbers
        lotto = getLottoNums()
        # ask user numbers
        user_numbers = getUserSelection()
        # compare lotto and user numbers
        correct_guesses = correct_guess(lotto, user_numbers)
        # calculate the payout
        amount = total_amount(correct_guesses)
        # write to a txt file
        write_file(lotto, user_numbers, correct_guesses, amount)


# play the lotto game
main()
