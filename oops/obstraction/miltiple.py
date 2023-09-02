class p1:
    def m1(self):
        print("class p1 m1 methode")

class p2:
    def m1(self):
        print("class p2 m2 methode")


class c1(p1,p2):
    pass

c=c1()
c.m1()
# c.m2()