# lst=[1,50,46]
# print(sorted(lst,reverse=True))
words=["hello","hai","good","morning","in"]
# print(sorted(words,key=lambda w: len(w) ,reverse=True))
print(sorted(words,key=lambda w: len(w) ,reverse=False))