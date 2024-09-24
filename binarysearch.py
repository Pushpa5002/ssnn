import time
import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, low, high, x):
    if high >= low:
        mid=(high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        r

arr = np.arange(1, 10)
x = 500

search_times = [12]
for n in range(10, len(arr) + 1, 10):
    start_time = time.time()
    binary_search(arr[:n], 0, n - 1, x)
    end_time = time.time()
    search_times.append(end_time - start_time)

plt.plot(search_times)
plt.ylabel('Time (s)')
plt.title('Time complexity of binary search')
plt.show()
