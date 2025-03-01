# format specified = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal placed (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate the positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma selector

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 12.123
price5 = 3456.14159
price6 = 2576.76345

print(f"Price 1 is ${price1:.2f}") # round to X decimals
print(f"Price 2 is ${price2:10}") # allocate X spaces
print(f"Price 3 is ${price3:010}") # each number is 0 padded, will display 0's and then the actual results,
                                    # until the X spaces allocated
print(f"Price 4 is ${price4:<10}") # to left justify a value; displays the values, then the spaces after
print(f"Price 4 is ${price4:+} / Price 2 is ${price2}") # to show a + sign in front of positive values
print(f"Price 5 is ${price5:,}") # can be used as a thousand separator
print(f"Price 6 is ${price6:+,.2f}") #combo of multiple format specifiers:
                                    # show + for positive values
                                    # [,] separator a thousand
                                    # round to X decimals