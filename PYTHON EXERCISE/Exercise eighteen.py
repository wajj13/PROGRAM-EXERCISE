# 实现不同文件之间数据关联


courseteachermap = {}
with open("/PYTHON EXERCISE/practice18.txt", "r", encoding="UTF-8") as file1:
    for line in file1:
        line.strip()
        if not line:
            continue
        try:
            course, teacher = line.split(",")
            courseteachermap[course] = teacher
        except ValueError:
            print(f"Skipping invalid line: {line}")
print(courseteachermap)
    