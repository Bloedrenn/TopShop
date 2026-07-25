import re
import time

def validate_email(email):
    """Простая проверка формата email-адреса."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))

def send_email_notification(to_email, subject, body):
    """Имитирует отправку электронного письма."""
    if not validate_email(to_email):
        print(f"⚠️ Системная ошибка: Некорректный Email-адрес '{to_email}'. Письмо не отправлено.")
        return False
        
    print(f"\n📧 [EMAIL OUTBOX] Подключение к почтовому серверу...")
    time.sleep(1) # Имитация сетевой задержки
    
    print(f"✉️ [EMAIL OUTBOX] Отправка письма на адрес: {to_email}")
    print(f"📌 Тема: {subject}")
    print(f"📝 Текст письма:\n{body}")
    print(f"✔️ [EMAIL OUTBOX] Письмо успешно доставлено!")
    print("-" * 40)
    return True

def send_welcome_email(username, to_email):
    """Шаблон приветственного письма после регистрации."""
    subject = "Добро пожаловать в наш магазин!"
    body = (
        f"Здравствуйте, {username}!\n\n"
        f"Спасибо за регистрацию на нашей платформе.\n"
        f"Теперь вам доступен полный каталог товаров и личный кабинет.\n\n"
        f"С уважением,\nКоманда поддержки."
    )
    return send_email_notification(to_email, subject, body)

def send_login_alert(username, to_email):
    """Шаблон уведомления о новом входе в аккаунт."""
    subject = "Обнаружен новый вход в аккаунт"
    # Имитируем дату и время (например, текущие системные)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    body = (
        f"Внимание, {username}!\n\n"
        f"В ваш аккаунт был выполнен вход {current_time}.\n"
        f"Если это были не вы, немедленно обратитесь в службу поддержки.\n\n"
        f"Безопасность вашего аккаунта — наш приоритет."
    )
    return send_email_notification(to_email, subject, body)
