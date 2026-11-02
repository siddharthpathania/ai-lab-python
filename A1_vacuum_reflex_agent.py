# A1 Simple Reflex Agent - rules: dirty -> SUCK, in A -> RIGHT, in B -> LEFT
loc = input("Start room (A/B): ").upper()
dirty = {"A": int(input("A dirty? (1/0): ")), "B": int(input("B dirty? (1/0): "))}

while dirty["A"] or dirty["B"]:
    if dirty[loc]:
        print(loc, "Dirty -> SUCK")
        dirty[loc] = 0
    elif loc == "A":
        print("A Clean -> MOVE RIGHT")
        loc = "B"
    else:
        print("B Clean -> MOVE LEFT")
        loc = "A"
print("Both rooms clean")
