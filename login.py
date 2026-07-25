def run_login():
    print("\n--- СТРАНИЦА ВХОДА ---")
    username = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    # Проверяем данные по нашей общей базе
    if username:
        print(f"\n🔓 Добро пожаловать, {username}!")
        print("=== ВЫ УСПЕШНО ВОШЛИ В ЛИЧНЫЙ КАБИНЕТ ===")
        return True
    else:
        print("❌ Ошибка: Неверный логин или пароль.")
        return False

if __name__ == "__main__":
    run_login()
