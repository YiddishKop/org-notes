import pickle
from Pickling_2 import Player

items = ["axe", 'sword', 'gun']

myObj = Player(1, "JEFF", 100.00, items)
print(myObj)

with open("save2.pkl", 'wb') as outfile:
    pickle.dump(myObj, outfile, pickle.HIGHEST_PROTOCOL)

print("--------------------")

newObj = None

with open("save2.pkl", 'rb') as infile:
    newObj = pickle.load(infile)

print(newObj)
