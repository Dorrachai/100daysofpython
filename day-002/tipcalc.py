ppl = int(
    input("This is a tip calculator, it will tell you how much each person will pay with tip included.\nState how "
          "many you are: "))
bill_tot = float(input("What is the total of the bill? "))
tip_perc = int(input("How manu percentage would you like to tip? between 5-10%?"))

while True:
    tip_perc = int(input("How many percentage would you like to tip? Please enter a number between 5-10: "))
    if tip_perc < 5 or tip_perc > 10:
        print("Please enter a valid percentage between 5-10.")
    else:
        # Calculate the tip amount and the total bill amount including the tip
        tip_amount = bill_tot * (tip_perc/100)
        total_amount = bill_tot + tip_amount

        # Calculate the amount each person needs to pay
        amount_per_person = total_amount / ppl

        # Round the amount to two decimal places
        amount_per_person = round(amount_per_person, 2)

        # Display the result
        print(f"Each person should pay: ${amount_per_person}")
        break
