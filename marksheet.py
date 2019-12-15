english = int(input("enter the marks of english: "))
maths = int(input("enter the marks of maths:  "))
urdu = int(input("enter the marks of urdu:  "))
sindhi = int(input("enter the marks of sindhi: "))
pakstudies = int(input("enter the marks of pak studies: "))
sum = (english+maths+urdu+sindhi+pakstudies)
per = (sum / 500) * 100
if per >= 90 :
    print(per)
    print("your grade is A")
elif per >= 80 and per < 90 :
    print(per)
    print("your grade is B")
elif per >= 70 and per < 80:
    print(per)
    print("your grade is C")
elif per >= 60 and per < 70:
    print(per)
    print("your grade is D")
else:
    print("you are fail in exams")

