age=int(input("Enter your age"))
if age <= 10:
    print("ticket is free of cost")
elif(age > 10 and age < 15):
    print("ticket amount is 10$")
elif( age > 15 and age < 25):
    print("ticket amount is 20$")
elif( age> 25 and age< 50):
    print("ticket amount is 50$")
else:
    print("your age is above")

