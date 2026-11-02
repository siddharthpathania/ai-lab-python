tree=[(3,5),(2,9)]

def alphabeta(node,is_max,alpha,beta):
    if type(node)==int:
        return node
    if is_max:
        best=-999
        for child in node:
            best=max(best,alphabeta(child,False,alpha,beta))
            alpha=max(best,alpha)
            if alpha>=beta:
                print("PRUNE! skip this node: ",node)
                break    
        return best

    else:
        best=999
        for child in node:
            best=min(best,alphabeta(child,True,alpha,beta))
            beta=min(best,beta)
            if alpha>=beta:
                print("PRUNE! skip this node: ",node )
                break
        return best

print("Best value: ",alphabeta(tree,True,-999,999))