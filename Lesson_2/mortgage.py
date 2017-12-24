# mortgage.py 
#
# Find out how long to pay off a mortgage 
import argparse

def calc_yrs(principal=500000, payment=2684.11, rate=0.05, total_paid=0):
    while principal > 0:
        interest = (rate / 12) * principal
        principal = (principal + interest) - payment
        total_paid += payment

    yrs_to_pay = total_paid/(payment*12)
    print("It will take {0:0.1f} years to pay off your mortgage".format(yrs_to_pay))

def main():
    #principal = 500000
    #payment = 2684.11
    #rate = 0.05
    #total_paid = 0
    #calc_yrs(principal, payment, rate, total_paid)
    calc_yrs()

if __name__ == "__main__":
    main()
