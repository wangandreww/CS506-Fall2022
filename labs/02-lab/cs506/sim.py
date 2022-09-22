# from scipy import spatial

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    x = set(x)
    y = set(y)
    nominator = x.symmetric_difference(y)

    #Find union of two sets
    denominator = x.union(y)

    #Take the ratio of sizes
    if len(denominator) == 0:
        return 0

    distance = len(nominator)/len(denominator)

    return distance

def cosine_sim(x, y):
    return 1 - spatial.distance.cosine(x, y)
 
# Feel free to add more