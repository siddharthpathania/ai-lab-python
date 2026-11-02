# B6 Goal Stack Planning (Blocks World). Initial: B on A; A, C, D on table. Goal: C on A, B on D.
# Pop top: goal true -> drop | goal false -> push action + its preconditions | action -> do it.
on = {"A": "T", "B": "A", "C": "T", "D": "T"}     # what each block sits on (T = table, H = hand)
hand = None
goals = [("ON", "C", "A"), ("ON", "B", "D")]
ACTIONS = ("STACK", "UNSTACK", "PICKUP", "PUTDOWN")

def top_of(x):
    for b in on:
        if on[b] == x:
            return b

def holds(t, x, y):
    if t == "ON":      return on[x] == y
    if t == "ONTABLE": return on[x] == "T"
    if t == "CLEAR":   return on[x] != "H" and top_of(x) is None
    if t == "HOLDING": return hand == x
    return hand is None                                    # ARMEMPTY

def achieve(t, x, y):          # action that makes the goal true
    if t == "ON":      return ("STACK", x, y)
    if t == "ONTABLE": return ("PUTDOWN", x, None)
    if t == "CLEAR":   return ("UNSTACK", top_of(x), x)
    if t == "HOLDING": return ("PICKUP", x, None) if on[x] == "T" else ("UNSTACK", x, on[x])
    return ("PUTDOWN", hand, None)                         # ARMEMPTY

def pre(a, x, y):              # preconditions (last one is solved first)
    if a == "STACK":   return [("HOLDING", x, None), ("CLEAR", y, None)]
    if a == "UNSTACK": return [("ON", x, y), ("ARMEMPTY", None, None), ("CLEAR", x, None)]
    if a == "PICKUP":  return [("ONTABLE", x, None), ("ARMEMPTY", None, None), ("CLEAR", x, None)]
    return [("HOLDING", x, None)]                          # PUTDOWN

stack = goals[:]
while stack:
    item = stack.pop()
    if item[0] in ACTIONS:
        if all(holds(*p) for p in pre(*item)):             # do the action
            a, x, y = item
            if a == "STACK":     on[x], hand = y, None
            elif a == "PUTDOWN": on[x], hand = "T", None
            else:                on[x], hand = "H", x      # UNSTACK / PICKUP
            print(a, x, y or "")
        else:
            stack += [item] + pre(*item)
    elif not holds(*item):
        action = achieve(*item)
        stack += [action] + pre(*action)
    if not stack:                                          # re-check all goals at the end
        stack = [g for g in goals if not holds(*g)]
