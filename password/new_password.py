import random
import string

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    if type(length) == int:
        for i in range(length):
            password += random.choice(characters)
        return password
    else:
        return 'Неправильный ввод длины пароля'

# Пример использования
password_length = 12  # Вы можете выбрать любую длину пароля
print("Ваш новый пароль:", generate_password(password_length))
