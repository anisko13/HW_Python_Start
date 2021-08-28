apple, orange = 20, 30
pay = int(input("How much do you have?"))
if pay >= apple + orange:
    print("You may have an apple and orange")
elif pay >=apple:
    print("You may have an apple")
elif pay >=orange:
    print("You may have an orange")
else:
    print ("No money")