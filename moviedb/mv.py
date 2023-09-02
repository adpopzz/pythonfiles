from json import load
with open("C:\\Users\\silverline\\Desktop\\my_pythoncode\\moviedb\\mdb.json","r",encoding="UTF-8") as f:
    data=load(f)
    #print total number of movies
# print(len(data))

# movie_name=[m.get("title") for m in data ]
# print(movie_name)
# movie_director=[m.get("director") for m in data ]
# print(movie_director)

# runtime=max(data,key=lambda m:int(m.get("runtime")))
# print(runtime.get("title"))

# print all geners
# movie_gener=[m.get("genres")for m in data ]
# print(movie_gener)

# print movie name which contain gener comedy
comedy_movie=[m.get("title") for m in data if m.get("genres") =="Fantacy"and"Fantacy"]
print(comedy_movie)
# print movie  name which gener containe comedy and fantacy


