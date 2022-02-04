import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()


def main():
    if args.type == "annuity":
        if args.principal and args.periods and args.interest:
            i = args.interest / (12 * 100)
            payment = math.ceil(args.principal * ((i * (1 + i)**args.periods)/(((1 + i)**args.periods) - 1)))
            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {(payment * args.periods) - args.principal}!")
        elif args.payment and args.periods and args.interest:
            i = args.interest / (12 * 100)
            principal = math.ceil((args.payment / ((i * (1 + i)**args.periods)/(((1 + i)**args.periods) - 1))))
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {(args.payment * args.periods) - principal}!")
        elif args.principal and args.payment and args.interest:
            i = args.interest / (12 * 100)
            x = (args.payment / (args.payment - i * args.principal))
            periods = math.ceil((math.log(x, 1+i)))
            years, months = divmod(periods, 12)
            if years == 0:
                print(f"{months} months to repay this loan!")
            elif months == 0:
                print(f"{years} years to repay this loan!")
            else:
                print(f"{years} years and {months} months to repay this loan!")
            print(f"Overpayment = {(args.payment * periods) - args.principal}!")
        else:
            print("Incorrect parameters")

    elif args.type == "diff":
        if args.principal and args.periods and args.interest:
            i = args.interest / (12 * 100)
            total_differentiated_payments = 0
            for m in range(1, args.periods + 1):
                differentiated_payments = math.ceil((args.principal / args.periods) + i * (args.principal - ((args.principal * (m - 1)) / args.periods)))
                total_differentiated_payments += differentiated_payments
                print(f"Month {m}: payment is {differentiated_payments}")
            print(f"Overpayment = {total_differentiated_payments - args.principal}")
        else:
            print("Incorrect parameters")


if __name__ == '__main__':
    main()
