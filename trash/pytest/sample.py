class Counter():

    count = 0

    @staticmethod
    def static_showCount():
        print("Static_show  !!"+str(Counter.count))

    @classmethod
    def cls_showCount(cls):
        print("Class Show !!!"+str(cls.count))

    def add(self, n1, n2):
        Counter.count += 1
        return(n1+n2)

    def sub(self, n1, n2):
        return(n1-n2)

o1 = Counter()
o2 = Counter()
if o1==o2:
    print("In......")
else:
    print("Out.....")
o1.add(1,2)
o1.sub(1,2)
o1.add(3,2)

o2.add(41,50)

Counter.static_showCount()
Counter.cls_showCount()
