class parent:
    def property(self):
        print("2cars 5kg gold 10lack rs")

    def proposal(self):
        print("mrg with gopal")

class child(parent):
    def proposal(self):
        print("amal")

ch=child()
ch.property()
ch.proposal()