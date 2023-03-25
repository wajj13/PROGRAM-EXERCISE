#统计学生喜欢的运动总类



like_count = {}
with open("G:/IDEA/PYTHON PROJECT/practionofpython/practicefile/practice18.txt", encoding="UTF-8") as file1:
    for line in file1:
        line = line.strip()
        sname, like = line.split(" ")
        like_list = like.split(',')
        for like in like_list:
            if like not in  like_count:
                like_count[like] = 0
            like_count[like] =+ 1
