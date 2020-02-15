
# I found help on the internet, this was too hardcore for a newbie...
import numpy as nump
import pandas as pand

def kMeans(examples, K, maxIters) :
    from copy import deepcopy
    def distance(k, j, kx = 1):
        return nump.linalg.norm(k - j, axis = kx)

    C_x = nump.random.randint(0, nump.max(examples) - 20, size = K)
    C_y = nump.random.randint(0, nump.max(examples) - 20, size = K)
    C = nump.array(list(zip(C_x, C_y)), dtype = nump.float32)
    print("Starting Center")
    print(C)

    C_old = nump.zeros(C.shape)
    clusters = nump.zeros(len(examples))
    error = distance(C, C_old, None)
    while True :
        if error == 0 or maxIters == 0:
            break

        for i in range(len(examples)) :
            distances = distance(examples[i], C)
            cluster = nump.argmin(distances)
            clusters[i] = cluster
        C_old = deepcopy(C)

        for i in range(K) :
            points = [examples[j] for j in range(len(examples)) if clusters[j] == i]
            C[i] = nump.mean(points, axis=0)

        error = distance(C, C_old, None)
        maxIters -= 1

    print("Outcome: ")
    print(C)

data = pand.read_csv('data.csv')

data.head()
f1 = data['Vector1'].values
f2 = data['Vector2'].values
data.head()

examples = nump.array( list( zip( f1, f2 ) ) )
kMeans(examples, 3, 10)