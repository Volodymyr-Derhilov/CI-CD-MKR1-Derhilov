def process_files(file1_path, file2_path, same_path, diff_path):
    """Зчитує рядки з file1_path і file2_path, знаходить спільні та різні,
       записує результати у same_path та diff_path."""
    # Зчитування рядків з першого файлу
    with open(file1_path, "r", encoding="utf-8") as f:
        lines1 = set(line.strip() for line in f if line.strip())

    # Зчитування рядків з другого файлу
    with open(file2_path, "r", encoding="utf-8") as f:
        lines2 = set(line.strip() for line in f if line.strip())

    # Рядки, що містяться в обох файлах
    same = lines1.intersection(lines2)
    # Рядки, що містяться лише в одному з файлів
    diff = (lines1.union(lines2)) - same

    # Запис спільних рядків у файл same.txt
    with open(same_path, "w", encoding="utf-8") as f:
        for line in sorted(same):
            f.write(line + "\n")

    # Запис різних рядків у файл diff.txt
    with open(diff_path, "w", encoding="utf-8") as f:
        for line in sorted(diff):
            f.write(line + "\n")


def task():
    process_files("./inputData/file1.txt", "./inputData/file2.txt", "./outputData/same.txt", "./outputData/diff.txt")



if __name__ == "__main__":
    task()