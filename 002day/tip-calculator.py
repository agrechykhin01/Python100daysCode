print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? "))
percentageTip = float("1." + input("What percentage tip would you like to give? 10, 12 or 15? "))
peopleCount = int(input("How many people to split the bill? "))
billWithTip = totalBill * percentageTip
shouldPay = "{:.2f}".format(billWithTip / peopleCount, 2)
print(f"Each person should pay: ${shouldPay}")