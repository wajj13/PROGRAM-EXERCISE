#按文件后缀名整理文件夹
import os
import shutil

dir = "G:\IDEA\PYTHON PROJECT\practionofpython\practicefile"
for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")
    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)


# course_grade = {}
# with open("xxx") as file2:
#     for line in file2:
#         line = line[:-1]
#         fied = line.split(",")
#         cor, sno, sanme, grade = line.split(",")
#         if cor not in course_grade:
#             course_grade[cor] = []
#         course_grade[cor].append(int(grade))
# print(course_grade)
# for cor, grade in course_grade.items():
#     print(
#         cor,
#         max(grade),
#         min(grade),
#         sum(grade) / len(grade)
#     )