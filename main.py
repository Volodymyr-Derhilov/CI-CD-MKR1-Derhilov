def task():
    # Зчитування рядків з першого файлу
    with open("./inputData/file1.txt", "r", encoding="utf-8") as f:
        lines1 = set(line.strip() for line in f if line.strip())

    # Зчитування рядків з другого файлу
    with open("./inputData/file2.txt", "r", encoding="utf-8") as f:
        lines2 = set(line.strip() for line in f if line.strip())

    same = lines1.intersection(lines2)  # Рядки, що містяться в обох файлах

    diff = (lines1.union(lines2)) - same  # Рядки, що містяться лише в одному з файлів

    # Запис спільних рядків у файл same.txt
    with open("./outputData/same.txt", "w", encoding="utf-8") as f:
        for line in sorted(same):
            f.write(line + "\n")

    # Запис різних рядків у файл diff.txt
    with open("./outputData/diff.txt", "w", encoding="utf-8") as f:
        for line in sorted(diff):
            f.write(line + "\n")

if __name__ == "__main__":
    task()