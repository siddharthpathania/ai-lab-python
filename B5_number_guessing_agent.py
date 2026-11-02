# B5 Guessing Agent - binary search: guess the middle, shrink range using feedback.
low, high, tries = 1, 100, 0
print("Think of a number from 1 to 100")

while low <= high:
    guess = (low + high) // 2
    tries += 1
    fb = input(f"Is it {guess}? (H = higher, L = lower, C = correct): ").upper()
    if fb == "C":
        print("Got it in", tries, "tries!")
        break
    elif fb == "H":
        low = guess + 1
    else:
        high = guess - 1
