import random
import re
login_list = ["A", "B"]
pass_list = ["1234", "123"]

def username(n: str, l: list):
    """
    Ищет логин в списке
    Возвращает True или False
    :param str n: ищет логин
    :rtype: bool
    """
    if n in l:
        t = True
    else:
        t = False
    return t
def auto_pass():
    """
    Генерация пароля
    Возвращает пароль в str
    :rtype: str
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    password = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(f"Ваш пароль: {password}")
    return password
def my_pass():
    '''
    Печать условий для пароля
    Возвращает пароль в str
    :rtype: str
    '''
    print("Пароль должен состоять минимум из 8 символов, иметь минимум 1 цифру, 1 большую и маленькую букву и 1 спецсимвол")
    password = input("Введите пароль:")
    sym = ".,:;!_*-+()/#¤%&)"
    i = 0
    while True:
        if passw(password) == True:
            break
        else:
            password = input("Введите пароль:")
            i += 1
            if password == 'y':
                return
            elif i > 1:
                print("Хотите завершить регистрацию? Напишите y")
    return password
def passw(p: str):
    '''
    Проверка пароля на условия
    Возвращает True или False
    :param str p: введеный пароль пользователя
    :rtype: bool
    '''
    if len(p) < 8:
        print("Пароль должен состоять минимум из 8 символов")
    elif re.search('[0-9]', p) is None:
        print("В пароле нет цифр")
    elif re.search('[a-z]', p) is None:
        print("В пароле нет букв в нижнем регистре")
    elif re.search('[A-Z]', p) is None:
        print("В пароле нет букв в верхнем регистре")
    elif re.search('[@#$%^&+=]', p) is None:
        print("B пароле нет спецсимволов")
        return True
    return False
def author():
    '''
    Авторизация в сети
    Возвращает True или False
    :rtype: bool
    '''
    n = input("Введите логин: ")
    u = username(n, login_list)
    if u == True:
        login = login_list.index(n)
        n = input("Введите пароль: ")
        if pass_list[login] == n:
            return True
        else:
            print("Неправильный пароль")
            return False
    else:
        print("Неправильный логин")
        return False
def reg(l: list, p: list):   
    """
    Регистрация в сети
    Возвращает списки логинов и паролей
    :rtype: list, list
    """
    print("Регистрация".center(24, ))

    n = input("Введите логин: ")
    u = username(n, login_list)
    i = 0
    while u == True:
        n = input('Такой логин уже существует.\nВведите еще раз: ')
        u = username(n, login_list)
        i += 1
        if i > 1:
            print("Хотите завершить регистрацию? Напишите y")
            if n == "y":
                print("Заканчиваем..")
                return


    v = input("Создать пароль автоматически или нет? y/n: ")
    if v == "y":
        p = auto_pass()
    else:
        p = my_pass()

    login_list.append(n)
    pass_list.append(p)
    print("Регистрация завершена".center(33, ))
    return l, p
while 1:
    print("Регистрация, авторизация, показать списки или выход")
    v = input("1/2/3/4: ")
    if v == "1":
        reg(login_list, pass_list)
    elif v == "2":
        print("Авторизация".center(24, " "))
        i = 0
        while i < 3:
            t = author() #True or False
            if t == True:
                print("Добро пожаловать!".center(30, " "))
                i = 3
            else:
                i+=1
    elif v == "3":
        print(login_list)
        print(pass_list)
    else:
        print("Выход..".center(24, ' '))
        break