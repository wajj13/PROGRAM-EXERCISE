# 求学生成绩最高分，最低分，平均分
def compute_score():
    scores = []
    with open("G:/IDEA/PYTHON PROJECT/practionofpython/practicefile/pratice12.txt", 'r', encoding="UTF-8") as file1:
        for line in file1:
            line = line[:-1]
            files = line.split(",")
            scores.append(int(files[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()
print(f"max_score={max_score},  min_score={min_score}, avg_score={avg_score}")
