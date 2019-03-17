import time
import sys
n = 10
for i in range(n):
    time.sleep(0.3)
    sys.stdout.write('\r')
    sys.stdout.write(str(i)*(n-i))
    sys.stdout.flush()
    print()
sys.stdout.write('\n')