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
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-principal', help="starting total mortgage balance")
    parser.add_argument('-payment', help="total mortgage pmt per month")
    parser.add_argument('-rate', help="interest rate (if 5%, input as 0.05")
    parser.add_argument('-total_paid', help="total down payment")
    args = parser.parse_args()

    #this is not working because all parameters dont have values 
    try:
        if args:
            calc_yrs(int(args.principal), float(args.payment),
            float(args.rate), float(args.total_paid))
        else:
            calc_yrs()
    except Exception:
        print("Without specifying all values, the script will run with defaults.")
        print("Running with default params...\n")
        calc_yrs()

if __name__ == "__main__":
    main()
