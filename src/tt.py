import glob
yy=glob.glob('C:\\Users\\Nadav\\connection\\connection_projects\\project\Docker\\tests\\*.txt')
for fi in yy:
    print(fi.split('\\')[-1])
# print(glob.glob('C:\\Users\\Nadav\\connection\\connection_projects\\project\Docker\\src\\*.py'))