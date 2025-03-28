import pytest
from mkr.main import process_files


@pytest.fixture
def file_setup(tmp_path):
    """
    Фікстура, що створює та повертає шляхи до тимчасових файлів:
      - file1.txt
      - file2.txt
      - same.txt (вихідний)
      - diff.txt (вихідний)
    """
    paths = {
        "file1": tmp_path / "file1.txt",
        "file2": tmp_path / "file2.txt",
        "same": tmp_path / "same.txt",
        "diff": tmp_path / "diff.txt"
    }
    return paths

@pytest.mark.parametrize(
    "file1_content, file2_content, expected_same, expected_diff",
    [
        (
            "apple\nbanana\ncherry\n",
            "banana\ncherry\ndurian\n",
            {"banana", "cherry"},
            {"apple", "durian"},
        ),
        (
            "python\njava\n",
            "java\nc++\n",
            {"java"},
            {"python", "c++"},
        ),
        (
            "one\ntwo\nthree\n",
            "four\nfive\n",
            set(),
            {"one", "two", "three", "four", "five"},
        ),
    ]
)
def test_process_files_combined(file_setup, file1_content, file2_content, expected_same, expected_diff):
    """
    Тест перевіряє функцію process_files із використанням одночасно
    фікстури (file_setup) та параметризації для різних сценаріїв вхідних даних.
    """
    # Записуємо тестові дані у тимчасові файли
    file_setup["file1"].write_text(file1_content, encoding="utf-8")
    file_setup["file2"].write_text(file2_content, encoding="utf-8")
    
    # Викликаємо основну функцію з відповідними шляхами
    process_files(str(file_setup["file1"]), str(file_setup["file2"]), str(file_setup["same"]), str(file_setup["diff"]))
    
    # Зчитуємо результати
    same_content = file_setup["same"].read_text(encoding="utf-8").strip().split("\n")
    diff_content = file_setup["diff"].read_text(encoding="utf-8").strip().split("\n")
    
    # Прибираємо можливі пусті рядки
    same_content = list(filter(None, same_content))
    diff_content = list(filter(None, diff_content))
    
    # Перевіряємо відповідність отриманих даних очікуваним
    assert set(same_content) == expected_same
    assert set(diff_content) == expected_diff
