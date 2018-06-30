# Created by Warda

print("""Title: Khaleefa Tower
Author: Warda""")


materials = ["vA"]*3 +["uC"]*2 +["uC"]*5 +["tE"]*5+["sG"]*5 +["rI"]*4 +["qCaCaC"]+["qCaCaC"]

def construct(tower):
    for x in range(len(tower)):
        metal = tower[x].isupper()
        print(("*" if metal else ' ')*(ord(tower[x])-(64 if metal else 96)), end="")
    print()


for x in range(len(materials)):
    construct(materials[x])
print()
        
        
print("""THANKS FOR CHECKING THIS CODE OUT

    Thanks for your likes,
       You all are amazing!""") 

