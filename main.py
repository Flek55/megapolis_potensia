"""Файл с выполненным 1 заданием"""
import csv

with open("magical.txt", encoding='utf-8') as f:
    """Открытие и обработка файла magical.txt и его дальнейшая обработка
    reader — обработчик файла
    arr — список рецептов из файла magical.txt
    mhk — словарь с искомыми травами и их кол-вом 
    hl — множество искомых трав
    sum_herbs — общее количество искомых трав
    """
    reader = csv.reader(f, delimiter="№")
    arr = list(reader)[1:]
    mhk = {}
    hl = set()
    sum_herbs = 0
    for magicaPotions, count, magic_herbs_1, magic_herbs_2, magic_herbs_3 in arr:
        """Поиск нужных трав и добавление их в hk и hl"""
        if int(count) == 1:
            mhk[magic_herbs_1] = 0
            mhk[magic_herbs_2] = 0
            mhk[magic_herbs_3] = 0
            hl.add(magic_herbs_1)
            hl.add(magic_herbs_2)
            hl.add(magic_herbs_3)
    for magicaPotions, count, magic_herbs_1, magic_herbs_2, magic_herbs_3 in arr:
        """Подсчет нужных трав"""
        if int(count) == 1:
            mhk[magic_herbs_1] += 1
            mhk[magic_herbs_2] += 1
            mhk[magic_herbs_3] += 1
            sum_herbs += 3
    hl = list(hl)
    with open("magicaPotions.csv", "w", encoding='utf-8') as outfile:
        """Сохранение результата в файл"""
        writer = csv.writer(outfile, delimiter='№', lineterminator="\n")
        headline = ["magic_herbs", "count_herbs"]
        writer.writerow(headline, )
        for i in range(len(hl)):
            x = [hl[i], str(mhk[hl[i]])]
            writer.writerow(x)
    with open("count.txt", "w", encoding='utf-8') as oc:
        """Сохранение общего кол-ва в файл"""
        oc.write(str(sum_herbs))
