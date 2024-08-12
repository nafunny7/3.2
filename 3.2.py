def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith(
            (".com", ".ru", ".net")) or "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адресом {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print("Нельзя отправить  письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес{recipient}")


send_email("Burger", "Nafane@internet.com", "university.help@gmail.com")
send_email("sandwich", "university.help@gmail.com", "university.help@gmail.com")
send_email("Model X", "Elon_Musk2009@stan.ru", "university.help@gmail.com")
send_email("photo.png", "On1yFanz.com", "university.help@gmail.com")
send_email("5_sezon_smesharikov", " Elon_Musk2009@stan.ru", "Petya2009@burger.com")
