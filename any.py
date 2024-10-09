import math
def calcmean(nums):
    return sum(nums)/len(nums)
def calcvar(nums,mean):
    return sum((x-mean)**2for x in nums)/len(nums)
def standarddev(variance):
    return math.sqrt(variance)

n=int(input("no.of elements:"))
nums=[]
for i in range(n):
    num = float(input(f"enter element {i+1}:"))
    nums.append(num)

mean= calcmean(nums)
variance=calcvar(nums,mean)
stddev=standarddev(variance)

print(f"{mean:.2f}")
print(f"{variance:.2f}")
print(f"{stddev:.2f}")