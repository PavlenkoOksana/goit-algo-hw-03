import os
import shutil
import argparse

def read_directory(path, destination_dir):
    if not os.path.isdir(path):
        print(f"\033[31m Помилка виконання: {path} не є дійсним каталогом \033[0m")
        return

    print(f"\033[94m Читаємо каталог: {path} \033[0m")
    
    elements = os.listdir(path)
    
    for element in elements:
        element_path = os.path.join(path, element)

        if os.path.isdir(element_path):
            try:
                read_directory(element_path, destination_dir)
            except Exception as e:
                print(f"\033[31m Виникла помилка: {e} \033[0m")
        else:
            extension = os.path.splitext(element)[1][1:] 
            destination_subdir = os.path.join(destination_dir, extension)
            os.makedirs(destination_subdir, exist_ok=True)
            try:
                shutil.copy(element_path, destination_subdir)                  
            except Exception as e:
                print(f"\033[31m Не вдалося скопіювати '{element}': {e} \033[0m")
            else:
                print(f"Копіюю '{element}' в '{destination_subdir}'")

def copy_files(source_dir, destination_dir):
    if not os.path.isdir(source_dir):
        print(f"\033[31m Помилка виконання: {source_dir} не є дійсним каталогом \033[0m")
        return

    try:
        read_directory(source_dir, destination_dir)
        print(f"\033[32m Копіювання завершене успішно! \033[0m")
    except Exception as e:
        print(f"\033[31m Виникла помилка: {e} \033[0m")

def main():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням')
    parser.add_argument('source_dir', type=str, help='Шлях до вихідного каталогу')
    parser.add_argument('destination_dir', nargs='?', type=str, default='dist', help='Шлях до цільового каталогу (default: dist)')
    args = parser.parse_args()

    source_directory = args.source_dir
    destination_directory = args.destination_dir

    copy_files(source_directory, destination_directory)
    

if __name__ == "__main__":
    main()

# python3 D:\Projects\My_Repository\goit-algo-hw-03\goit-algo-hw-03\hw1-1.py C:/Users/kompik/Downloads/1 C:/Users/kompik/Downloads/1_Copy