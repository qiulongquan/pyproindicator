import time
import sys
for i in range(5):
    time.sleep(0.3)
    print(str(i)*10, end='')
    sys.stdout.flush()
print()