def f_person_params(**kwargs):
    """
    Функция возращает входные данные 
    
    """
    return kwargs 


'''регулярные выражения пока еще не прошли(e-mail и phone без проверки)'''

v = False
while not v :
    l_name = input("Введите фамилию:\n")
    v = l_name.isalpha()
v = False
while not v :
    l_sirname = input("Введите имя:\n")
    v = l_sirname.isalpha()
v = False
while not v :    
    l_birth = input("Введите дату рождения(ддммгг):\n")
    v = True if l_birth.isdigit() and len(l_birth) == 6 else False
v = False
while not v :
    l_city = input("Введите город:\n")
    v = l_city.isalpha()
v = False
while not v :        
    l_email = input("Введите e-mail:\n")
    '''Проверим как можем:
        * знак '@' должен быть в строке
        * до знака '@' должны быть символы
        * между знаками '@' должны '.' быть символы
        * перед последними 2-3 символами должна быть '.'
        * последние 2-3 символа должны быть буквами(com,net,org,tr,ru,it,fr...)
    '''
    
    v = True if l_email.count('@') == 1 \
                and len(l_email[:l_email.find('@')]) > 0 \
                and len(l_email[l_email.find('@'):(len(l_email)-2-l_email[::-1].find('.'))]) > 0 \
                and l_email[::-1].find('.') in [2,3] \
                and ( \
                    l_email[:len(l_email)-3:-1].isalpha() \
                    or l_email[:len(l_email)-4:-1].isalpha() \
                    ) \
                else False
v = False
while not v :        
    l_phone = input("Введите №телефона:\n")
    v = l_phone.isdigit()
    
print(f_person_params(p_name=l_name,\
                      p_sirname=l_sirname,\
                      p_birth=l_birth,\
                      p_city=l_city,\
                      p_email=l_email,\
                      p_phone=l_phone
                      ))

