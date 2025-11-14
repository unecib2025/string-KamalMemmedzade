# nom 1
name = input()
name = name.strip()
if name.isalnum():
    name = name.lower()
    print("Имя корректно")
else:
    print("Ошибка")
# nom 2
password = input()
if len(password) < 8:
    print("Пароль слаб")
else:
    has_digit = False
    has_upper = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
    if has_digit and has_upper:
        print("Пароль надёжен")
    else:
        print("Пароль слаб")
# nom 3
log = "ACCESS DENIED"
print(log.capitalize() + " – вход запрещён")
# nom 4
data = "ERROR connection ERROR failed access"
new_data = data.replace("ERROR", "ALERT")
print(new_data)
print("Количество предупреждений:", new_data.count("ALERT"))
# nom 5
email = input("Введите email: ")

if email.find("@") == -1:
    print("Некорректный адрес")
else:
    domain = email.split("@")[1]
    print("Домен:", domain)
# nom 6
text = input("Введите текст: ")
text = text.strip().lower().replace(" ", "_")
print(text)
# nom 7
text = input("Введите строку: ")

if text.find("SECRET") != -1:
    text = text.replace("SECRET", "******")
    print(text)
    print("Внимание! Конфиденциальная информация!")
else:
    print("Информация безопасна")
# nom 8
word = input("Введите слово: ")

codes = ""
for char in word:
    codes += str(ord(char)) + " "
print("Коды символов:", codes)

new_word = ""
for char in word:
    new_word += chr(ord(char))
print("Обратно:", new_word)
# nom 9
text = "login attempt failed access denied unauthorized access"

failed_count = text.count("failed")
denied_count = text.count("denied")

print("failed встречается:", failed_count)
print("denied встречается:", denied_count)

if failed_count > 0 or denied_count > 0:
    print("Попытка несанкционированного доступа")
# nom 10
report = input("Введите отчёт: ")

print("Количество предложений:", len(report.split(".")) - 1)
print("Символов без пробелов:", len(report.replace(" ", "")))

if report.lower().startswith("report"):
    print("Текст начинается со слова 'Report'")
else:
    print("Текст не начинается со слова 'Report'")

if report.lower().count("error") >= 2:
    print("Ошибки найдены")
# Вопросы
Что представляет собой строка в Python?
Строка — это последовательность символов, например, "hello" или '123'.

Что такое Unicode и зачем он используется?
Unicode — это стандарт для кодирования символов всех языков. Он нужен, чтобы Python мог работать с буквами, цифрами и символами любых языков.

Что делают методы strip(), replace(), find()?

strip() — убирает пробелы в начале и конце строки.

replace(old, new) — заменяет все вхождения old на new.

find(sub) — ищет подстроку sub и возвращает её позицию, или -1, если не найдено.

Как посчитать количество вхождений подстроки?
С помощью метода count(). Например: "hello hello".count("hello") вернёт 2.

Чем отличается upper() от capitalize()?

upper() — делает все буквы заглавными.

capitalize() — делает первую букву заглавной, а все остальные маленькими.

Что возвращает ord() и chr()?

ord(char) — код символа char.

chr(code) — символ с кодом code.

Как проверить, начинается ли строка с определённого слова?
С помощью метода startswith(). Например: "Hello world".startswith("Hello") вернёт True.

Почему важно фильтровать вводимые пользователем данные?
Чтобы предотвратить ошибки, атаки на программу и сохранить безопасность данных.