
# start_end = input("start and end number : ").split()
# print(start_end)
# print(int(start_end[0]), int(start_end[1]))

start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start:
    start, end = end, start

for i in range(start, end+1):
        # is_prime = True

    if i <= 1:
        continue
    for k in range(2, i):
        if i % k == 0:
           # is_prime = False
            break
    else:
        print(i, end=' ')




