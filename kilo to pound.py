weight=int(input("enter your weight"))
select=input("select (l)bs or (k)kg")
if select=="k":
    k = weight * 0.45
    print(f"your weight in kilo:{k}")
elif select=="l":
    l= weight / 0.45
    print(f"your weight in pounds:{l}")

