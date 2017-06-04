## 在对象级别，控制循环何时停止
## 这个很厉害
class MyTrain:
    def __init__(self):
        self.condition = True
        self.passenger = range(20)
    def __getitem__(self, index):
        if not self.condition:
            raise IndexError("that's enough!")
        value = self.passenger[index]
        return value # hand control back to the block

train1 = MyTrain()
for name in train1:
    print("this is {0} passenger".format(name))
    if name == 15:
        train1.condition = False

class MyFileIterator :
    def __getitem__ (self, index):
        text = get next line from file
        if end of file:
            raise IndexError( "end of file" )
        return text

class MyFileIterator2 :
    def __iter__ (self):
        return self # use myself
    def next():
        text = get next line from file
        if end of file:
            raise StopIteration()
        return text
