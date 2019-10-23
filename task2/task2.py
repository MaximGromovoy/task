import sys

# file_name_... - имена файлов, первый - узлы фигуры, второй - точки
file_name_1 = str(sys.argv[1])
file_name_2 = str(sys.argv[2])
#file_name_1 = "file1.txt"
#file_name_2 = "file2.txt"
# count - счетчик для удобного считывания данных из файла, который находид пробел между двумя значениями
# ,т.е. между x и y
count = 0
# list_1 - список узлов фигуры
# list_2 - список точек
list_1 = []
list_2 = []
# Переменная, которая позволяет не продолжать дальнейшую проверки точки, если она совпала с одной из вершин
# и перейти к новой итерации внешнего цикла
tmp = 0

# list1 - список, состоящий из списков пар координат фигуры(x,y)
    # list1[0] - первый узел
        # list1[0][0] - x1
        # list1[0][1] - y1
    # list1[1] - второй узел
        # list1[1][0] - x2
        # list1[1][1] - y2
    # list1[2] - третий узел
        # list1[2][0] - x3
        # list1[2][1] - y3
    # list1[3] - четвертый узел
        # list1[3][0] - x4
        # list1[3][1] - y4
# list2 - аналогичный список list1, только хранит координаты точек (x,y)
    # list2[0] - первая точка
        # list2[0][0] - x
        # list2[0][1] - y
    # list2[...]

# Функция определения точки относительно фигуры (внутри - 1, вне - 0)
def check_inout_shape(x, y, shape):
    for i in range(len(shape)):
        if (((shape[i][1]<=y and y<shape[i-1][1]) or (shape[i-1][1]<=y and y<shape[i][1])) and \
            (x > (shape[i-1][0] - shape[i][0]) * (y - shape[i][1]) / (shape[i-1][1] - shape[i][1]) + shape[i][0])):
            return 1
    return 0

# Функция проверки принадлежности точки (x,y) прямой [(x1,y1);(x2,y2)]
# Уравнение: (x-x1)/(x2-x1)=(y-y1)/(y2-y1)
def check_on_line(x, y, x1, y1, x2, y2):
    # Избегаем деления на ноль
    if ((x2-x1) == 0) or ((y2-y1) == 0):
        if x == x1:
            return 1
        if y == y1:
            return 1
        return 0
    # Проверяем
    if ((x-x1)/(x2-x1) == (y-y1)/(y2-y1)) and ((x1 < x < x2 or x2 < x < x1) and (y1 < y < y2 or y2 < y < y1)):
        return 1
    else:
        return 0

# Считываем координаты узлов фигуры
file_1 = open(file_name_1, 'r')
for line in file_1:
    for tmp in line:
        if tmp == ' ':
            list_1.append([float(line[0:count:1]), float(line[count + 1:len(line) - 1:1])])
        count = count + 1
    count = 0

# Считываем координаты точек
file_2 = open(file_name_2, 'r')
for line in file_2:
    for tmp in line:
        if tmp == ' ':
            list_2.append([float(line[0:count:1]), float(line[count + 1:len(line) - 1:1])])
        count = count + 1
    count = 0

# print(list_1) # Вывод списка узлов
# print(list_2) # Вывод списка точек

# Проверка точек относительно фигуры
for point in list_2:
    # print("Point: " + str(point)) # Вывод текущей точки
    # Совпадают ли точки с вершинами
    for line_1 in list_1:
        if point == line_1:
            tmp = 1
    if tmp == 1:
        print("0")
        tmp = 0
        continue
    # Совпадают ли точки с границей
    if check_on_line(point[0], point[1], list_1[0][0], list_1[0][1], list_1[1][0], list_1[1][1]) == 1:
        print("1")
        continue
    if check_on_line(point[0], point[1], list_1[1][0], list_1[1][1], list_1[2][0], list_1[2][1]) == 1:
        print("1")
        continue
    if check_on_line(point[0], point[1], list_1[2][0], list_1[2][1], list_1[3][0], list_1[3][1]) == 1:
        print("1")
        continue
    if check_on_line(point[0], point[1], list_1[3][0], list_1[3][1], list_1[0][0], list_1[0][1]) == 1:
        print("1")
        continue
    # Проверяем, внутри ли точка
    if check_inout_shape(point[0], point[1], list_1):
        print("2")
        continue
    # В остальных случаях, точка лежит вне фигуры
    print("3")