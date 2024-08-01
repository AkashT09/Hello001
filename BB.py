"""Program to demonstrate bubbble sort"""
import time
import matplotlib.pyplot as plt
import tracemalloc
start=time.time()
n=len(nums)
def Bubble_sort(nums):
    for i in range (n-1,0,1):
        for j in range(i):
            if (nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
            print(nums)
        print("\n")

tracemalloc.start()
nums=[4,89,58,5,86,275,85]
print("Before sorting the given number")
print(nums)
print("\n")

Bubble_sort(nums)
print("After sorting the given number")
print(nums)

print("Memory space",tracemalloc.get_tracemalloc_memory(),"Bytes")
print("Run time of program :",end-start)
tracemalloc.stop()

x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Bubble sort time complexity is O(n\u00b2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()





        
