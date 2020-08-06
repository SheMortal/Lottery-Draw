# Sinothando Bacela
# Class 1
# Python Mini Project
from datetime import date as date_today

# writing in the text file
def write_file(lott_numbers, selection_num, correct_guesses, amount):
    # set today's date
    today = date_today.today()

    # open, read and write in file Lotto_Draw.txt
    with open("Lotto_Draw.txt", "w+") as file:
        # write in file
        file.write("Date: {}\n".format(today))
        file.write("Lotto numbers {}\n".format(lott_numbers))
        file.write("Your lotto selection {}\n".format(selection_num))
        file.write("Number of correct guesses: {}\n".format(correct_guesses))
        file.write("Total amount required: R{}\n".format(amount))
        # close the file
        file.close()
