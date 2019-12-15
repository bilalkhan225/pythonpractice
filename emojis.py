word=input("--->")
words=word.split(' ')
emoji={
    ":)":":)",
    ":(":":("
}
output=""
for emo in words:
    output+=emoji.get(word,word) + " "
    print (output)
    break
