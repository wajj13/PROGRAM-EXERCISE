# 获取文件大小与各个文件大小的和
import os

print(os.path.getsize("/PYTHON EXERCISE/practice14.txt"))
sum_size = 0
for file in os.listdir("/PYTHON EXERCISE"):
    if os.path.isfile(file):
            sum_size += os.path.getsize(file)
print(sum_size / 1000)
