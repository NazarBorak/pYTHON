# FCFS/FIFO

print("Firs Come First Served")
print("\n")
burst_time = []
waiting_time = []
nop = int(input("Number of process?: "))

k = 1
while k < nop + 1:
    a = int(input("Burst time of process %s: " % k))
    burst_time.append(a)
    k = k + 1

# p1        p2          p3
# 24s       3s          3s      AWT = (WT1+WT2+WT3)/3 = 17
# WT-0S     WT-24S      WT-27

awt = 0
for x in range(0, len(burst_time)):
    waiting_time.append(sum(burst_time[:x]))

    if len(burst_time) - 1 == x:
        awt = (sum(waiting_time) / len(burst_time))

p = 1
print("|\t    Process ID    \t|\t   Burst time     \t|\t   Waiting time    \t|")
for y in range(0, len(burst_time)):
    print(
        "|\t       %s         \t|\t       %s         \t|\t       %s         \t|" % (p, burst_time[y], waiting_time[y]))
    p = p + 1

print("Average waiting time = %s" % awt)
