from itertools import permutations
print(permutations([1,2,3,4,5,6]))
snapelist = ['p','w','p','f','p','b','w']
snapeAllListspermu = permutations(snapelist)
snapelists = list(snapeAllListspermu)
snapeset = set(snapelists)
def constraint(slist):
    s = []
    for l in slist:
        wcount = 0;
        if(l[0] !=  l[6] and l[0] != 'f' and l[6] != 'f' and l[1] != 'p' and l[2] != 'p' and l[1] == l[5]):
            for i in range(1,7):
                if(l[i] == 'w' and l[i-1] == 'p'):
                    wcount += 1;
                    if(wcount >1):
                        print(l)
                        s.append(l)
    return s
solution = constraint(snapeset)
print(solution)
