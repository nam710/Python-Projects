T = int(input())
size = []
arr = []
G = []
for item in range(T):
    size += [int(input())]
    G += [""]
    arr += [input().replace(" ", "")]
    maximum = 0
    for i in range(size[item]):
        freq = 0
        for j in range(size[item]):
            if(arr[item][i] == arr[item][j]):
                freq += 1
        if(freq > maximum):
            maximum = freq
    G[item] = size[item] - maximum
for item in range(T):
    print(G[item])
