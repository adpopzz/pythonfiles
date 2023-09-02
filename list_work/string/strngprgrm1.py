text="one 100 and fifty 5"
#100, 5
word=text.split(" ")
print(word)
for w in word:
    if w.isdigit():
        print(w)