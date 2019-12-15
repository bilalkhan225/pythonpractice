name=input("enter your name ")
print(len(name))
if len(name) > 3 and len(name)< 49:
    print("name must be atleast 3 characters")

elif len(name)>50:
    print("name can be a maximum from 50 character")
else:
    print("name looks good!")