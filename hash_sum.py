import hashlib
import os


path = os.listdir(path=os.getcwd())
path_to_dir = os.listdir(path=path[1])
path_to_file = path[2]
path_file = os.getcwd() + "\\" + path[1] + "\\"


try:
    with open(path_to_file, "r") as file:
        for line in file:
            file_name = line.strip().split()[0]
            algorithm = line.strip().split()[1]
            hash_in_file = line.strip().split()[2]

            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            sha256 = hashlib.sha256()

            if file_name in path_to_dir:
                with open(path_file + file_name, 'rb') as path_dir:
                    md5.update(path_dir.read())
                    sha1.update(path_dir.read())
                    sha256.update(path_dir.read())

                if algorithm == "md5":
                    hash_sum = md5.hexdigest()

                elif algorithm == "sha1":
                    hash_sum = sha1.hexdigest()

                elif algorithm == "sha256":
                    hash_sum = sha256.hexdigest()

                if hash_in_file == hash_sum:
                    print(file_name, "OK")
                else:
                    print(file_name, "FAIL")
            else:
                print(file_name, "NOT FOUND")


except FileNotFoundError:
    print("Файл {} не найден".format(path_to_file))
