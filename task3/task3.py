import sys

files_name = [str(sys.argv[1]) + "/Cash1.txt",
              str(sys.argv[1]) + "/Cash2.txt",
              str(sys.argv[1]) + "/Cash3.txt",
              str(sys.argv[1]) + "/Cash4.txt",
              str(sys.argv[1]) + "/Cash5.txt"]
queue_in_time = []  # Список с очередями из всех файлов
i = 0  # Счетчик
num = 0  # Номер искомого интервала
max_queue = 0  # Наибольшая очередь
tmp_queue = 0  # Временная переменная

# Считываем из файлов данные
# Для каждого файла создается вложенный список
for file_name in files_name:
    file = open(file_name)
    queue_in_time.append([])
    for line in file:
        queue_in_time[i].append(float(line))
    file.close()
    i = i + 1
i = 0
j = 0

# Для каждого внешнего списка (т.е. кассы)
for i in range(len(queue_in_time[j])):
    # проходим по одному интервалу времени
    # и считаем максимальную длину очереди
    for j in range(len(queue_in_time)):
        tmp_queue += queue_in_time[j][i]
    if tmp_queue > max_queue:
        max_queue = tmp_queue
        num = i + 1
    tmp_queue = 0

# Вывод искомого значения
print(num)