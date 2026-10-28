person_count = int(input("Enter the number of people: "))

food_price = int(input("Enter the price of food: "))

drink_price = int(input("Enter the price of drinks: "))

total_price = food_price + drink_price

tip = int(input("Enter the tip percentage: ").strip("%"))
tip_amount = total_price * tip / 100 

grand_total = total_price + tip_amount

per_person_cost = grand_total / person_count

print(
    f"Tip amount: ${tip_amount:.2f}\n"
    f"Total cost: ${grand_total:.2f}\n"
    f"Cost per person: ${per_person_cost:.2f}"
)
