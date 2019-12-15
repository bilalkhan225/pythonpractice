number=(input("Enter number plz"))
characters={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output=""
for char in number:
    output+=characters.get(char, "no") +  ""
    print(output)
