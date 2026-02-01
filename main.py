"""
Задача №3
В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны.
Необходимо объединить их в один по следующим правилам:
1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк,
 а последним - с наибольшим)
2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

Пример Даны файлы: 1.txt

Строка номер 1 файла номер 1
Строка номер 2 файла номер 1

2.txt

Строка номер 1 файла номер 2

Итоговый файл:

2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1

"""

import os


def get_dict_files(path_dir):
    '''

    the function creates a dictionary
    with keys that are the paths to files in the given directory
    and values that are the number of lines in the file
    :param path_dir - the path to the directory where the files are located:
    :return a dictionary with the keys file path and the value number of lines in the file:
    '''
    result = {}
    if os.path.isdir(path_dir):
        files = os.listdir(path_dir)
        for file in files:
            path_file = os.path.join(path_dir, file)
            if os.path.isfile(path_file):
                with open(path_file, encoding='utf-8') as f:
                    count_ = sum(1 for _ in f)  # for count_, _ in enumerate(f, start=1):
                    result[path_file] = count_
    return result


def combining_files(dict_files):
    '''

    write the final file "final.txt" to a directory "final" inside the directory where the recording files are located
    :param dict_files - a dictionary with the keys file path and the value number of lines in the file
           example - {'resources\\1.txt': 8, 'resources\\2.txt': 1, 'resources\\3.txt': 9}:
    :return:
    '''
    sorted_dict_files = dict(sorted(dict_files.items(), key=lambda item: item[1]))
    path_name = list(sorted_dict_files.keys())[0]
    directory_name = os.path.dirname(path_name)
    final_file_name = os.path.join(directory_name, 'final', 'final.txt')
    number_files = len(dict_files)

    with open(final_file_name, 'w', encoding='utf-8') as final_file:
        for i, (path_, lines) in enumerate(sorted_dict_files.items(), start=1):
            file_name = os.path.basename(path_)
            with open(path_, encoding='utf-8') as f:
                final_file.writelines([file_name + '\n', str(lines) + '\n'])
                for line in f:
                    final_file.write(line)
                if i < number_files:
                    final_file.write('\n')
                # final_file.write(f.read() + '\n') if i < number_files else final_file.write(f.read())


combining_files(get_dict_files("resources"))

