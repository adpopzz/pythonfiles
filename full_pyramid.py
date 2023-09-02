# for row in range(1,5):
#     for col in range (row):
#         print("*",end=" ")
#     print()



# for row in range(1,5):  
#          for col in range(row,5):
#             print("*",end=" ")
#          print()

          #create hollo full pyramid
"""
         *
      *     *
     *        *
   *           *
  *  *  *   *   * 

"""

# r=10
# for row in range(1,6):
#     for col in range(1,10):
#         if (row==5) or (row+col==6) or (col-row==4):
#            print("*",end="")
#         else:
#             print(end=" ")
    # print()



# for row in range(1,5):
#     for col in range(1,8):
#         if(row==1) or (row==col) or (row+col==8):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


#hacker rank
#full pyramid

r=5
k=0
for row in range(1,r+1):
    for col in range(1,(row-r),+1):
         print(end="  ")

         
        
    while k!=2*row-1:
          print("* ",end="")
          k += 1

    k=0
    print()




        # else:
        #     print(end=" ")
    print()
   
# r=5
# for i in range(r):
#     print(""*(i-r),'*'*(i*2+1))
