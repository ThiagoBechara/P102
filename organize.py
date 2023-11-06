import os
import shutil

from_dir='c:/Users/Cliente/Downloads'
to_dir='c:/Users/Cliente/Desktop/BYJUS/PRO102'

list_of_files=os.listdir(from_dir)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #! splitext vai separar nome e extensão "imagem.png" = 'imagem' / 'png'

    if extension == '':
        continue
    if extension in ['.gif', '.jpg', '.png', '.jpeg', '.jfif', '.webp']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Arquivos_Imagens'
        path3 = to_dir + '/' + 'Arquivos_Imagens' + '/' + file_name

    if os.path.exists(path2):
        print('movendo' + file_name + ".....")
        shutil.move(path1, path3)
       
    else:
        os.makedirs(path2)
        print("movendo" + file_name + ".....")
        #método de automação
        shutil.move(path1, path3)
