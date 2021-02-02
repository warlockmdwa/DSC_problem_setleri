def mail():
    et = '@'
    nokta = '.'
    adres = input("mail adresini giriniz: ")
    if (et and nokta in adres):
        print("Dogru giris yapabilirsin")
        return True
    else:
        print("Yanlis eposta")
        return False

print(mail())