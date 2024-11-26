#   Дополнительное практическое задание по модулю: "Основные операторы"
#   Задание "Слишком древний шифр" module_2_hard.py
def Code(Numer):
    k = 1
    LenInp = ""
    while k <= Numer/2:
        for i in range(k + 1, Numer):
            if k + i > Numer:      break
            if Inp_RG % (k + i) == 0: LenInp = LenInp + str(k) + str(i)
        k = k + 1
    print(LenInp)
Inp_RG=1
while Inp_RG>0:
    Inp_RG=int(input('''Введите число от 3 до 20
Для выхода набеоите 0\n'''))
    if Inp_RG>2 and Inp_RG<21: Code(Inp_RG)
print('\n\nДо новых встреч')


