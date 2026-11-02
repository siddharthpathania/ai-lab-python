loc=input("Which Room A/B?: ").upper()
dirty={"A":int(input("A Room Dirty 0/1?: ")), "B":(int(input("B Room Dirty 0/1?: ")))}

while dirty["A"] or dirty ["B"]:
    if dirty[loc]:
        print(loc,"-> DIRT FOUND CLEANING NOW")
        dirty[loc]=0
    elif loc=="A":
        print("Switching to left")
        loc = "B"

    else:
        loc = "A"
        print(loc,"Cleaned moving to right")  

print("both rooms cleaned")