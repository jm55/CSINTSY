import time

runs = 100
ave = 0

for i in range(runs):
    start = time.time()
    time.sleep(.1)
    elapse = time.time()-start
    ave = ave + elapse

print("Average: ", ave/runs)