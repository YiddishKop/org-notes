class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.__next__())
print([corner_street_atm.__next__() for cash in range(5)])

hsbc.crisis = True
# print(corner_street_atm.__next__())

wall_street_atm = hsbc.create_atm()
# print(wall_street_atm.__next__)

hsbc.crisis = False
print (corner_street_atm.__next__())

brand_new_atm = hsbc.create_atm()
# for cash in brand_new_atm:
#     print ( cash )


mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)
for i in mylist:
    print(i+3)

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

for i in mygenerator:
    print(i+3)

## 四匹马赛跑的所有结果，通过 itertools 包
import itertools
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
## 下面这两句很有意思：
## 好像 list() 可以把里面的各种结果 '列' 出来
print(races)
print(list(itertools.permutations(horses)))
