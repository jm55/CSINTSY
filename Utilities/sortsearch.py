import random
import time

#Vars
start = 0
nums = [1,10,100,1000,10000,100000,1000000,10000000,100000000]
target_sum = 123
ls = []
result = []
for n in nums:
    #Fill ls[]
    print(n, "Filling array...")
    for i in range(n):
        ls.append(random.randint(1,n))

    #Get start time
    start = time.time()

    #Sort ls[]
    print(n, "Sorting...")
    ls.sort()

    #Get end time
    end = round(time.time()-start,5)

    ls = []

    print(n, "Sorted!", str(end)+"s\n")
    result = result + [[n, end]]

print(result)