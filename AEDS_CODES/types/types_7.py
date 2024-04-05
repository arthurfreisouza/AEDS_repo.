import sys

word = str(input())
arr = word.split(" ")

n_infec = int(arr[0])
chain_infec = int(arr[1])

cond1 = 2 <= n_infec <= 1000
cond2 = 1 <= chain_infec <= n_infec - 1

if cond1 == False or cond2 == False:
    sys.exit()

p_susp = set()
arr_total_pac = set()
for i in range(chain_infec):
    word = str(input())
    arr = word.split(" ")
    p_susp.add(int(arr[0]))
    cond3 = (1 <= int(arr[0]) <= n_infec)
    cond4 = (1 <= int(arr[1]) <= n_infec - 1)
    if cond3 == False or cond4 == False:
        sys.exit()
    arr_total_pac.update(map(int, arr[2 : ]))

ordened_result = list(sorted(p_susp.difference(arr_total_pac)))
arr_total_pac = list(arr_total_pac).sort()

if arr_total_pac[len(arr_total_pac) - 1] > 1000:
    sys.exit()
for i in ordened_result:
    print(int(i))
