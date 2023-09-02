movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}
    ]

#q1 print all movies names

# for m in movies:
#     print(m.get("name"))
# movies_name=[m.get("name")  for m in movies ]
# print(movies_name)


#Q2 print filter movites with gener = mystery

# for m in movies:
#     if "mystery" in m.get("genres"):
#         print(m.get("name"))
# mystery_movies=[m.get("name") for m in movies if "mystery" in m.get("genres")]
# print(mystery_movies)   
#Q3 top rated movie names

# print(max(movies,key=lambda m:m.get("rating")))
   
# Q4 print malayalam movies names
# for m in movies:
#     if "malayalam" in m.get("language"):
#         print(m.get("name"))
# movie_lanuage=[m.get("name") for m in movies if "malayalam" in m.get("language")]
# print(movie_lanuage)
# Q5 movie names released in 2023
# released_date=[m.get("name") for m in movies if m.get("year")==2023]
# print(released_date)
# Q6 order movies wrt rating order by desc
 
print(sorted(movies,reverse=False,key=lambda m:m.get("rating")))