def replace_text_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            replaced_content = file_content.replace('1', '2')
        
        with open(file_path, 'w') as file:
            file.write(replaced_content)
        
        print(f"Замена завершена в файле {file_path}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")

# Пример вызова функции для замены в файле "example.txt"
replace_text_in_file('example.txt')