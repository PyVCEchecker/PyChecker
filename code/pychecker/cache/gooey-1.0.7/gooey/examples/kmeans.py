
import math
import random
from functools import reduce

random.seed(0)

data = [(random.randint(0, 20),  random.randint(0, 20)) for _ in range(100)]

def vectsum(points):
    return reduce(lambda acc, val: (acc[0] + val[0], acc[1] + val[1]), points)

def vectdiv(a, b):
    return (a[0] / b[0], a[1] / b[1])

def direct_kmeans(points):
    centeroids = [random.choice(data) for _ in range(5)]

    clusters = {c: [] for c in centeroids}
    while True:
        for p1, p2 in points:
            closest = math.inf
            closest_centeroid = None
            for c1, c2 in centeroids:
                distance = math.pow(c1 - p1, 2) + math.pow(c2 - p2, 2)
                if distance < closest:
                    closest = distance
                    closest_centeroid = (c1,c2)

            clusters[closest_centeroid].append((p1,p2))
        print('before')
        print(clusters)
        clusters = {vectdiv(k, vectsum(v)) : [] for k,v in clusters.items()}
        break
    print('after')
    print(clusters)









direct_kmeans(data)
