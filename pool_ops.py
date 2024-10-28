# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p.
#
# Written by Alwaleed Alrashidi 
# Other contributors: Prof Brad Denby (Boilerplate and lecture slide refernce code)
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math

if len(sys.argv)==9:

c_in = int(sys.argv[1])
h_in = int(sys.argv[2])
w_in = int(sys.argv[3])
h_pool = int(sys.argv[4])
w_pool = int(sys.argv[5])
s = int(sys.argv[6])
p = int(sys.argv[7])

# Calculate output dimensions
h_out = (h_in-h_pool+2*p)//s+1
w_out = (w_in-w_pool+2*p)//s+1
c_out = c_in  # Channel count remains the same for pooling layers

# Calculate operations
adds = c_out*h_out*w_out*(h_pool*w_pool-1)  # Adds required for each pooling operation
muls = 0  # No multiplications needed for average pooling
divs = c_out*h_out*w_out  # One division per pooled output element

# Output the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed