bill = float(input("Total bill amount? "))
service = input("Level of service (good?, bad?, or fair?): ")


if service == "good":
    tip = bill * .20
    total = bill + tip
    print("Tip amount: {:.2f} Total amount: {:.2f}".format(tip, total))
elif service == "bad":
    tip = bill * .10
    total = bill + tip
    print("Tip amount: {:.2f} Total amount: {:.2f}".format(tip, total))
elif service == "fair":
    tip = bill * .15
    total = bill + tip
    print("Tip amount: {:.2f} Total amount: {:.2f}".format(tip, total))
