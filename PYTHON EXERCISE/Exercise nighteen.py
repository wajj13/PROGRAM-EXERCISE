#批量合并TXT文件
import os

data_dir = "/PYTHON EXERCISE"

content = []
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path, encoding="UTF-8") as file1:
            content.append(file1.read())
final_content = "\n".join(content)
with open(os.path.join(data_dir, "practice19.txt"), "w", encoding="UTF-8") as file2:
    file2.write(final_content)
