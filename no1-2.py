M, L = map(int, input().split())
N = int(input())
Name, Price, Level = [], [], []
for i in range(N):
    name, *values = input().split()
    price, level = map(int, values)
    Name.append(name)
    Price.append(price)
    Level.append(level)

for i in range(N):
    if(L >= Level[i]):
        if(M >= Price[i]):
            print(Name[i] + ' ' + str(Price[i]))
          




