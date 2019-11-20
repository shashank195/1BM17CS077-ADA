I = float('inf')
g = [[0,5, I, 10],
     [I,0,3,I],
     [I,I,0,1],
     [I,I,I,0]
    ]

def floyds(g):
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g[0])):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    
    return g

print(floyds(g))