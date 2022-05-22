import os

BASE_PATH = os.getcwd()
TEXT_FILE_NAME = "text.txt"
directories = list(filter(os.path.isdir, os.listdir(BASE_PATH)))


for directory in directories:
    if directory == "files_for_task_3":
        path_to_files = os.path.join(BASE_PATH, directory)
        files = os.listdir(path_to_files)
        all_text_files = {}

        for file in files:
            path_file = os.path.join(path_to_files,file)

            with open(path_file) as text:
                all_text_files[file] = text.readlines()

        sort = sorted(all_text_files, key = lambda x: len(all_text_files[x]))

        for file in sort:
            with open("text.txt", "a") as new_document:
                new_document.write(file + '\n')
                new_document.write(str(len(all_text_files[file])) + '\n')
                new_document.writelines(all_text_files[file] + ['\n'])



