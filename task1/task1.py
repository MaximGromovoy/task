import sys

list_from_file = []  # Список элементов из файла
percentile = 0  # Перцентиль
median = 0  # Медиана
max_num = 0  # Максимальное значение
min_num = 0  # Минимальное значение
mean_num = 0  # Среднее значение
file_name = str(sys.argv[1])  # Имя файла
#file_name = "file1.txt"  # Имя файла
count = 0  # Количество элементов в списке

file = open(file_name, 'r')

for line in file:
    list_from_file.append(float(line))
    count = count + 1
file.close()
list_from_file.sort()
# Вычисляем 90 Перцентиль
percentile = list_from_file[int((len(list_from_file)/100)*90)]
#  Вычисляем медиану
if count % 2 != 0:
    median = list_from_file[int(count / 2) + 1]
if count % 2 == 0:
    median = (list_from_file[int(count / 2)] + list_from_file[int(count / 2) + 1]) / 2
#  Вычисляем макс, мин и ср значения
max_num = list_from_file[-1]
min_num = list_from_file[0]
for num in list_from_file:
    mean_num = mean_num + num
mean_num = mean_num / count
#  Вывод всех значений
print("%.2f" % percentile)
print("%.2f" % median)
print("%.2f" % max_num)
print("%.2f" % min_num)
print("%.2f" % mean_num)
