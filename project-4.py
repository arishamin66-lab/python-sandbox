cart = {
    "apple": 150,
    "milk": 250,
    "bread": 180
}

total = 0
expensive = cart["apple"]
expensive_name = "apple"
cheapest = cart["milk"]
cheapest_name = "milk"
count = 0

for key, value in cart.items():
    total += value
    count += 1
    if value > expensive:
        expensive = value
        expensive_name = key
    if value < cheapest:
        cheapest = value
        cheapest_name = key

print(total)
if total > 500:
    print("Total is more than 500")

print(f"{expensive_name}: {expensive}")
print(f"{cheapest_name}: {cheapest}")
# The "count" variable was being calculated but never used/printed - added here
print(f"Number of items: {count}")
