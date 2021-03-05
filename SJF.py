# SJF - Shortest Job First
print("Shortest Job First system")
print("\n")

burst_time = []
waiting_time = []
nop = int(input("Number of process?: "))

k = 1
while k < nop + 1:
    a = int(input("Burst time of process %s: " % k))
    burst_time.append(a)
    k = k + 1

std = sorted(burst_time)

# p1        p2          p3          p4
# 6s        8s          7s          3s               WT = (WT1+WT2+WT3+WT4)/4 = 7
#After sorting
# 3s        6s          7s          8s
# WT-0S     WT-3S      WT-9        WT-16

summ = 0
for x in range(0, len(burst_time)):
    waiting_time.append(sum(std[:x]))

    if len(burst_time) - 1 == x:
        summ = (sum(waiting_time) / len(std))

o = 0
print("|\t Burst time \t|\t Waiting Time    \t|")
for y in range(0, len(burst_time)):
    print("|\t     %s        \t|\t       %s         \t|" % (std[y], waiting_time[y]))
    o = o + 1

print("\n")
print("Average waiting time = %s" % summ)
