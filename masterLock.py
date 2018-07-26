from collections import defaultdict
import matplotlib.pyplot as plt

def masterLocksmith(k, state):
    slopeChange = defaultdict(int)
    for i in state:
        slopeChange[i] += 2 # valley
        slopeChange[(i+k/2)%k] -= 2 # peak
    print(slopeChange)
    cost = sum(min(i, k - i) for i in state)
    
    slope = sum((2*x >= k) - (2*x < k) for x in state)
    print(slope)
    lastX = 0
    best = (cost, 0)
    print(0, cost, slope)
    for x in sorted(slopeChange.keys()):
        cost += (x - lastX) * slope
        slope += slopeChange[x]

        print(x, cost, slope)

        lastX = x
        best = min(best, (cost, x))

    return best[1]

def graph(k, initialState):
    d = []
    for j in sorted(set(initialState)):
        d.append((j,[min(abs(i-j), k-abs(i-j)) for i in initialState], sum([min(abs(i-j), k-abs(i-j)) for i in initialState])))
    ss = []
    for i,j,s in d:
        #plt.plot(j, label=str(i))
        ss += [s]
    print(ss)
    plt.plot(ss, "o-")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test1 = (10, [2, 7, 1])
    test2 = (3, [2, 0, 1, 2, 0, 1, 2])
    test3 = (4, [1,3])
    test4 = (10, [7, 8, 9, 3, 3])
    test5 = (100, [97, 98, 99, 0, 1])
    test6 = (360, [178, 104, 21, 81, 330, 353, 299, 263, 221, 199, 124, 261, 66, 204, 244, 337, 224, 84, 352, 91])
    test7 = (360, [45, 103, 44, 107, 41, 182, 14, 53, 181, 140, 186, 271, 189, 110, 78, 208, 354, 350, 70, 231])
    test8 = (360, [46, 308, 85, 256, 216, 255, 289, 255, 100, 328, 138, 265, 49, 83, 320, 189, 56, 293, 326, 127])
    test9 = (3, [0, 2, 0, 0, 0, 2, 2, 2, 1, 1, 0, 2, 0, 0, 1, 2, 0, 0, 2, 1, 1, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 1, 1, 0, 1, 0, 2, 2, 1, 0, 1, 0, 2, 1, 2, 2, 0, 0, 1, 2, 0, 0, 2, 2, 0, 1, 1, 2, 2, 0, 0, 0, 0, 1, 2, 1, 0, 0, 1, 0, 2, 2, 2, 2, 2, 0, 2, 1, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0, 2, 0, 0, 2, 1, 1, 1, 2, 2, 1, 1, 1])
    test10 = (4, [3, 3, 0, 0, 2, 1, 2, 3, 0, 0, 2, 1, 2, 0, 0, 1, 3, 0, 0, 1, 1, 1, 0, 2, 0, 1, 0, 1, 3, 2, 2, 3, 1, 3, 0, 1, 0, 3, 2, 3, 2, 0, 3, 2, 0, 1, 2, 3, 0, 3, 2, 2, 3, 2, 0, 3, 0, 1, 3, 1, 2, 0, 3, 2, 1, 0, 3, 0, 0, 1, 0, 0, 3, 3, 0, 3, 3, 2, 0, 1, 3, 2, 1, 3, 0, 0, 2, 2, 2, 2, 0, 1, 2, 0, 3, 2, 2, 3, 3, 2])
    test11 = (5, [2, 0, 2, 0, 2, 0, 1, 3, 3, 3, 4, 2, 2, 4, 1, 3, 4, 4, 2, 0, 0, 0, 0, 3, 0, 2, 2, 1, 0, 0, 4, 3, 3, 1, 4, 4, 3, 4, 4, 2, 4, 0, 0, 2, 4, 0, 3, 1, 2, 0, 1, 2, 0, 3, 3, 2, 0, 1, 3, 1, 4, 3, 1, 1, 3, 4, 2, 2, 3, 3, 0, 2, 3, 3, 2, 1, 0, 3, 4, 3, 4, 3, 4, 0, 3, 3, 0, 1, 1, 0, 0, 2, 2, 1, 4, 2, 1, 0, 3, 3])

    test = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11]
    k, initialState = test10

    masterLocksmith(k, initialState)
    graph(k, initialState)







