from googletrans import Translator
import json

# task 1 + 2

sample = ""
s = 0

while s != '':
    s = input("Вводите ваш текст, желательно в виде предложений, "
              "для прекращения ввода нажмите enter сразу после этого сообщения: ")
    sample = sample + s + '\n'
sample = sample[:-2]
print('\n' + sample + '\n')

with open("a.txt", "w+", encoding="utf-8") as text:
    text.writelines(sample)
    text.seek(0)
    text_len = text.readlines()
    print(f"В данном файле такое количество строк: {len(text_len)}\n")
    j = 0

    for i in text_len:
        #i = i[:-1]
        i = i.split()
        j += 1
        print(f"Количество слов в {j}-й строке количество слов равное {len(i)}")

# task 3

with open("text_3.txt", "r", encoding="utf-8") as text3:
    text_len3 = text3.readlines()
    salary = []
    reach = []

    for i in text_len3:
        #i = i[:-1]
        i = i.split()
        salary.append(float(i[1]))
        if float(i[1]) >= 20000:
            reach.append(i[0])
print(f'\nФамилии богачей с зарпалатой от 20к рублей: {", ".join(reach)}')
print(f'Средняя зарплата всех сотрудников: {(sum(salary))/len(salary)} рублей\n')

# task 4 в итоге я оставил так, как и хотел, чтобы без особых бубнов. Вроде больше не падало. *пожимаю плечами*


def y(a):
    res = Translator().translate(a, src='en', dest='ru')
    return res.text


with open("text_4.txt", "r", encoding="utf-8") as text4:
    text_len4 = text4.read()
    text_len4 = y(text_len4)

with open("text_41.txt", "w", encoding="utf-8") as text41:
    text41.writelines(text_len4)


# with open("text_41.txt", "w", encoding="utf-8") as text41:
#     with open("text_4.txt", "r", encoding="utf-8") as text4:
#         text_len4 = text4.read()
#     text41.write(Translator().translate(text_len4, dest='ru').text)

# task 5

sample = ""
s = 0

while s != '':
    s = input("Вводите ваш целые числа, разделённые пробелом; допускается ввод чисел несколькими строкам, "
              "для прекращения ввода нажмите enter сразу после этого сообщения: ")
    sample = sample + s + '\n'
sample = sample[:-2]
print('\n' + sample + '\n')

with open("a5.txt", "w+", encoding="utf-8") as text5:
    text5.writelines(sample)
    text5.seek(0)
    text_len5 = text5.readlines()    
    sum_int = 0

    for i in text_len5:
        i = i.split()
        for n in i:
            if n.isdigit() is True or (n[0] == "-" and n[1:].isdigit() is True):
                sum_int = sum_int + int(n)        
    print(f"Сумма чисел, отделённых пробелами от других вводимых элемнтов текста равна {(sum_int)}")

# task 6

with open("text_6.txt", "r", encoding="utf-8") as text6:
    text_len6 = text6.readlines()
    sum_list = []
    subj = []

    for i in text_len6:
        i = i.split()
        sum_int = 0

        for n in i:
            if "(" in n:
                n = n[:n.index("(")]
            if n.isdigit() is True:
                sum_int = sum_int + int(n)

        sum_list.append(sum_int)
        subj.append(i[0][:-1])

    hours = {subj[i]: sum_list[i] for i in range(len(subj))}
    print(f"\nПеред вами словарь вида «название предмета»: количество академических часов\n{hours}")

# task 7

with open("text_7.txt", "r", encoding="utf-8") as text7:
    text_len7 = text7.readlines()
    firm_dict = {}
    sum_int = 0
    j = 0

    for i in text_len7:
        i = i.split()
        k = int(i[2]) - int(i[3])
        if k > 0:
            sum_int = sum_int + k
            j += 1
        firm_dict.update({i[0]: k})

    dict_2 = {"average_profit": sum_int / j}
    company_list = [firm_dict, dict_2]
    print(company_list)

    with open("text_7.json", "w", encoding="utf-8") as text71:
        json.dump(company_list, text71, indent=4, ensure_ascii=False)
