items = ["apple", "orange", "mango","apple","grapes"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate found! ",item)
        break
    else:
        unique_items.add(item)