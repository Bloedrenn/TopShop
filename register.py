import re
import login

def validate_username(username):
    if not re.match(r"^[a-zA-Z0-9]{4,15}$", username):
        print("❌ Ошибка: Логин должен содержать от 4 до 15 латинских букв или цифр.")
        return False
    return True

def validate_password(password):
    if len(password) < 6:
        return False
    if not any(char.isdigit() for char in password):
        print("❌ Ошибка: Пароль должен содержать хотя бы одну цифру.")
        return False
    return True

def run_registration():
    print("\n--- СТРАНИЦА РЕГИСТРАЦИИ ---")
    username = input("Придумайте логин: ").strip()
    
    if username:
        print("❌ Ошибка: Пользователь с таким логином уже существует.")
        return False

    if not validate_username(username):
        return False

    password = input("Придумайте пароль: ").strip()
    if not validate_password(password):
        return False

    # Сохраняем в нашу общую базу данных
    print(f"🎉 Успех! Пользователь '{username}' успешно зарегистрирован.")
    
    # ИМИТАЦИЯ ЛОГИКИ ПОСЛЕ УСПЕШНОЙ РЕГИСТРАЦИИ:
    # Автоматически отправляем пользователя на экран входа
    print("\n🔄 Перенаправление на страницу входа...")
    login.run_login() 
    return True

if __name__ == "__main__":
    run_registration()
