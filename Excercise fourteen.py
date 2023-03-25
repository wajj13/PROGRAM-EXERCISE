# 统计英文文章单词出现的次数
word_count = {}
with open("G:/IDEA/PYTHON PROJECT/practionofpython/practicefile/practice14.txt", "r", encoding="UTF-8") as file1:
    for line in file1:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
# print(word_count)
print(
    sorted(
        word_count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
)
