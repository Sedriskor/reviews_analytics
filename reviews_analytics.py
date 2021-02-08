data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 ==0:#如果是1000的倍數
            print(len(data))

print(len(data))

print(data[0])
print('---------------------------')
print(data[1])
