# 打印的数据输出直接到文件，不在pyhton Console中显示
import time
import sys
f_handler=open('out.log', 'w')
sys.stdout=f_handler
print('hello')
# this hello can't be viewed on concole
# this hello is in file out.log