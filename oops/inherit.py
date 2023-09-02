class parent:
    def mobile(self):
        print("realme")

    def car(self):
        print("polo")

    def bike(self):
        print("xpulse")


class child(parent):
    pass

obj=child()
obj.mobile()
obj.car()
obj.bike()

