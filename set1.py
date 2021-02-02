def fb():

    while True:
        fizzerBuzzer = input("Sayı sınırını belirtiz: ")
        try:
            for f in range(int(fizzerBuzzer)):  #fizzerBuzzer degiskenini for dongusune alip istedigimiz sayiyi veriyoruz
                if (f % 3 == 0):
                    print("FİZZ")
                    continue
                elif (f % 5 == 0): #dongudeki sayilar 5 liklere esitse Buzz cevabini bastiriyor
                    print("BUZZ")
                    continue
                print(f)
            break

        except ValueError:
            print("Sadece sayi girin lutfen")




fb()
print('----Bitti----')
