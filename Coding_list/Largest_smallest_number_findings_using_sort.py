data = [40, 10, 20, 30, 60, 80, 50]
size = len(data)
for passes in range(0,size):
    for x in range(0,size-1-passes):
        y = x+1
        if data[x] > data[y]:
            data[x],data[y] = data[y],data[x]
print(f"Minimum value {data[0]}\nMaximum value {data[len(data)-1]}")
print(f"Second largest number is {data[len(data)-2]}")
