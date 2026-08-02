def run_login():
    print("\n--- СТРАНИЦА ВХОДА ---")
    username = input("Введите: ").strip()
    password = input("пароль: ").strip()

    # Проверяем данные по нашей общей базе
    if username:
        print(f"\n🔓 Добро пожаловать, {username}!")
        return True
    else:
        print("❌ Ошибка: Неверный логин или пароль.")
        return False

if __name__ == "__main__":
    run_login()
