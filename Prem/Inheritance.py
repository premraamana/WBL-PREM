class parent():
    def output(self):
        print("hii")

class child(parent):
    def outputc(self):
        print("bye")

class minichild(parent):
    def outputchild(self):
        print("Hello")        

obj1=child()
obj1.output()
obj1.outputc()               

obj2=minichild()
obj2.output()
obj2.outputchild()