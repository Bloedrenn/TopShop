import re

# Имитация базы данных (ключ - логин, значение - пароль)
USERS_DB = {}

def validate_username(username):
    """Проверка логина: от 4 до 15 символов, только буквы и цифры."""
    if not re.match(r"^[a-zA-Z0-9]{4,15}$", username):
        print("❌ Ошибка: Логин должен содержать от 4 до 15 латинских букв или цифр.")
        return False
    return True

def validate_password(password):
    """Проверка пароля: минимум 6 символов, наличие цифры и заглавной буквы."""
    if len(password) < 6:
        print("❌ Ошибка: Пароль должен быть не менее 6 символов.")
        return False
    if not any(char.isdigit() for char in password):
        print("❌ Ошибка: Пароль должен содержать хотя бы одну цифру.")
        return False
    if not any(char.isupper() for char in password):
        print("❌ Ошибка: Пароль должен содержать хотя бы одну заглавную букву.")
        return False
    return True

def register_user():
    """Логика регистрации нового пользователя."""
    print("\n--- РЕГИСТРАЦИЯ ---")
    username = input("Придумайте логин: ").strip()
    
    if username in USERS_DB:
        print("❌ Ошибка: Пользователь с таким логином уже существует.")
        return

    password = input("Придумайте пароль: ").strip()
    if not validate_password(password):
        return

    confirm_password = input("Повторите пароль: ").strip()
    if password != confirm_password:
        print("❌ Ошибка: Пароли не совпадают.")
        return

    # Сохраняем в "базу данных"
    USERS_DB[username] = password
    print(f"🎉 Успех! Пользователь '{username}' успешно зарегистрирован.")

def login_user():
    """Логика входа в систему."""
    print("\n--- ВХОД В СИСТЕМУ ---")
    username = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    # Проверяем наличие пользователя и соответствие пароля
    if username in USERS_DB and USERS_DB[username] == password:
        print(f"🔓 Добро пожаловать, {username}! Вы успешно вошли в систему.")
        return True
    else:
        print("❌ Ошибка: Неверный логин или пароль.")
        return False

# Демонстрация работы (Интерфейс в консоли)
def main():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Зарегистрироваться")
        print("2. Войти")
        print("3. Показать зарегистрированных (для теста)")
        print("4. Выйти из программы")
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print(f"\n👥 Текущая БД пользователей: {USERS_DB}")
        elif choice == "4":
            print("👋 Программа завершена. До свидания!")
            break
        else:
            print("⚠️ Неверный пункт меню. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
