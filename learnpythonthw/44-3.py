class SuperFun(Child, BadStuff):
    pass

class Child(Parent):
    def _init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()