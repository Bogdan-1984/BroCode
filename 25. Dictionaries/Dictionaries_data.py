# dictionaries = a collection of {key.value} pairs
#                ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
           "India": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow"}

# print(dir(capital))
# print(help(capital))

# print(capitals.get("India"))

"""if capitals.get("Russia"):
    print("The capital exists")
else:
    print("That capital does not exist")"""

# --------------------------------------------------------------------------------------------------------------
# capitals.update({"Germany": "Berlin"}) => a new collection pair can be added to the existing dictionary
# capitals.update({"USA": "Detroit"})    => can be used to update an existing entry in the dictionary
# capitals.pop("China")                  => used to remove an entry in the dictionary
# capitals.popitem()                     => deletes that last entry in the dictionary
# capitals.clear()                       => clear the entire dictionary

# --------------------------------------------------------------------------------------------------------------
# keys = capitals.keys()

# for key in capitals.keys():
#    print(key)

# --------------------------------------------------------------------------------------------------------------

# values = capitals.values()

# print(values)                     => option 1

# for values in capitals.values():  => option 2
#   print(values)

# --------------------------------------------------------------------------------------------------------------

items = capitals.items()
# print(items)                => resembles a 2D list (no. 23)

# for key, value in capitals.items():
#    print(f"{key}: {value}")