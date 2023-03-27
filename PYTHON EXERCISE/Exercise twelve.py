#获取学生成绩TXT并输出
def read_file():
    result = []
    with open("/PYTHON EXERCISE/pratice12.txt", 'r', encoding="UTF-8") as file1:
        for line in file1:
            line = line[:-1]
            result.append(line.split(","))
    return result
def sort_grades(datas):
    return sorted(datas,
                  key=lambda x : int(x[2]),
                  reverse=True)
def write_file(datas):
    with open("/PYTHON EXERCISE/pratice12_output.txt", "w", encoding="UTF-8") as file2:
        for data in datas:
            file2.write(",".join(data) + "\n")


#读取文件
datas = read_file()
print("read_file datas:", datas)
#排序
datas = sort_grades(datas)
print("sort_grades data:", datas)
#打印排序文件
write_file(datas)