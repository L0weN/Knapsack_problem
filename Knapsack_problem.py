import time
def knapSack():
    start_time = time.time()
    value = []
    weight = []
    f = open("10000.txt")
    for line in f:
        List = line.strip().split()
        value.append(int(List[0]))
        weight.append(int(List[1]))
    f.close()
    List.clear()
    capacity = weight[0]
    n = len(value)
    table = [[0 for x in range(capacity+1)] for x in range(n+1)]

    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weight[i - 1] <= j:
                table[i][j] = max(value[i - 1] + table[i - 1][j - weight[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    print(table[n][capacity])
    time_execution = time.time() - start_time
    print(time_execution)
    return

knapSack()