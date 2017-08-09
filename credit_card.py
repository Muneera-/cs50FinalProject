# credit card page that will do the following:
#   accept 16 digit credit card number
#   accept 4 digits total for month(2 digits) and year(2 digits)
#   accept 3 secret code digit
#   if any if the above is enter incorrectly the kick error
#


# variables of:
#               ccn(credit card number)
#               mth(month)
#               year
#               cvc(card security code)

# add routes
### THIS IS JUST THE BASIC LOGIC OF WHAT I WANT TO DO###


def credit_card():
    cnn = input("Please enter you credit card number: ")
    if (cnn.isdigit() and len(cnn) == 16):
        mth = input("Please enter month of credit card: ")
        if (mth.isdigit() and len(mth) == 2):
            year = input("Please enter year of credit card: ")
            if (year.isdigit() and len(year) == 2):
                csc = input("Please enter your csc(\"Card Security Code\")")
                if (csc.isdigit() and len(csc) == 3):
                    # send to page render_template(i.e "success you purchase is
                    # good sort of thing")
                    return("success test")  # some render_template for failure

    return render_template("some failure")  # render_template of bad input
