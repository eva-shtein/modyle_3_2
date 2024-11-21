def send_email(message, recipient, sender = "university.help@gmail.com"):
    recipient_domain = recipient.split(".")[-1]
    sender_domain = sender.split(".")[-1]
    if "@" not in recipient and "@" not in sender or recipient_domain not in ".com" and recipient_domain not in ".ru" and recipient_domain not in ".net" and sender_domain not in ".com" and sender_domain not in ".ru" and sender_domain not in ".net":
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса",sender,"на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

send_email("Сообщение для проверки", "vasyok1337@gmail.com")
#send_email("Сообщение для проверки связи", "urban.fan@mail.ru", "urban.info@gmail.com")
# send_email ("Пожалуйста, исправьте задание", "urban.student@mail.ru", "urban.teacher@mail.uk")
#send_email ("Напомнить о вебинаре", "urban.teacher@mail.ru", "urban.teacher@mail.ru")