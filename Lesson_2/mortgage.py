# mortgage.py 
#
# Find out how long to pay off a mortgage 
import argparse

def print_schedule(principal, payment, rate, total_paid):
    """Could have this function push a schedule to a file, it would ask for a
    filename
    """


def calc_yrs(principal=500000, payment=2684.11, rate=0.05, total_paid=0):
    print("Inputs:\nPrinicpal: {:<10.2f} Monthly Payment: {:<10.2f} Interest Rate: {:<10.2f} Down Payment: {:<10.2f} \n".format(principal, payment, rate, total_paid))

    while principal > 0:
        interest = (rate / 12) * principal
        principal = (principal + interest) - payment
        total_paid += payment

    yrs_to_pay = total_paid/(payment*12)
    print("It will take {0:0.1f} years to pay off your mortgage".format(yrs_to_pay))
    print("The total cost of the mortgage will be {0:0.1f}.".format(total_paid))

def main():
    #principal = 500000
    #payment = 2684.11
    #rate = 0.05
    #total_paid = 0
    #calc_yrs(principal, payment, rate, total_paid)
    parser = argparse.ArgumentParser(description='Input arguments for mortgage calculator')
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
