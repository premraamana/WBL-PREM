class parent:
    def method1(self):
        print('im parent')

class child(parent):
    def method2(self):
        print('im child')

child1 = child()
child1.method2()
child1.method1()