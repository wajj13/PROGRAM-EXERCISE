#复杂列表字典元组排序
students = [
    {"sno": 101, "name": "小张","grade": 88},
    {"sno": 102, "name": "小王","grade": 22},
    {"sno": 103, "name": "小李","grade": 33},
    {"sno": 104, "name": "小刘","grade": 44},
    ]
student_sort = sorted(students, key=lambda x: x["grade"], reverse=True)
print(f"source {students}, /sort result: {student_sort}")
