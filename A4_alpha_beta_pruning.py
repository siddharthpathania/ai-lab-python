# A4 Alpha-Beta Pruning - MAX wants big, MIN wants small.
# alpha = best MAX has so far, beta = best MIN has so far. If alpha >= beta -> stop (prune).
tree = [[3, 5], [2, 9]]          # MAX picks a bag, then MIN picks a number from that bag

def alphabeta(node, is_max, alpha, beta):
    if type(node) == int:                     # just a number -> return it
        return node
    if is_max:
        best = -999
        for child in node:
            best = max(best, alphabeta(child, False, alpha, beta))
            alpha = max(alpha, best)
            if alpha >= beta:
                print("Pruned! Skipped the rest of", node)
                break
        return best
    else:
        best = 999
        for child in node:
            best = min(best, alphabeta(child, True, alpha, beta))
            beta = min(beta, best)
            if alpha >= beta:
                print("Pruned! Skipped the rest of", node)
                break
        return best

print("Best value:", alphabeta(tree, True, -999, 999))
