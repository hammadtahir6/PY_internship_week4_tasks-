import re
import os

folder_path= 'E:\PY Internship tasks'
files= os.listdir(folder_path)

filtered_files = [f for f in files if f.endswith(".txt") and re.match(r"^report", f)]

print("matching .txt files: ")
for file in filtered_files:
    print(files)