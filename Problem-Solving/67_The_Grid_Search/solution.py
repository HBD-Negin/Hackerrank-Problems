def occurrences(string, sub):
    res = []
    ind = 0
    while ind < len(string) - len(sub) + 1:
        found = string.find(sub, ind)
        
        if found != -1:
            res.append(found)
            ind = found + 1
        else:
            break
    return res

def gridSearch(G, P):
    for ind_g in range(len(G) - len(P) + 1):
        all_occurrences = []
        for ind_p, s_pat in enumerate(P):
            all_occurrences.append(occurrences(G[ind_g + ind_p], s_pat))
            
        ourset = set(all_occurrences[0])
        for lst in all_occurrences:
            ourset &= set(lst)
            
        if len(ourset) >= 1:
            return 'YES'
            
    
    return 'NO'
        
t = int(input().strip())
for a0 in range(t):
    R, C = input().strip().split(' ')
    R, C = [int(R), int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r, c = input().strip().split(' ')
    r, c = [int(r), int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)
    result = gridSearch(G, P)
    print(result)