
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries[0][1]) # indexing [0] groceries will print the results from collection list 0 (fruits in this case).
                       # If an item from collection list 0 must be printed, a second indexing [1] is needed
                       # EX: print = apple => it's in list [0], item [1]
# ---------------------------------------------------------------------------------------------------------------

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]
"""print(groceries[0][1])"""

for collection in groceries:
    # print(collection)
    for food in collection:
        print(food) # print(food, end=" ") => to display each list on a row
    print()