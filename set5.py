import random


class school1():
    def __init__(self,okulIsmi,archMage,ogrenciSayisi,ogretmenSayisi,enBasariliSinif,konum,okulSiralamasi):
        self.okulIsmi = okulIsmi
        self.archMage = archMage
        self.ogrenciSayisi = ogrenciSayisi
        self.ogretmenSayisi = ogretmenSayisi
        self.enBasariliSinif = enBasariliSinif
        self.konum = konum
        self.okulSiralamasi = okulSiralamasi


sc1 = school1("SCHOOL NAME: VOZGARTH MAGE ACADEMY", 'ARCHMAGE: ADAM WARLOCK',

                #Random metoduyla rasgele sayi atanmistir
              "STUDENTS: "+str(random.randint(2000,5000)), "TEACHERS: "+str(random.randint(100,1000)),

                "BEST MAGE-CLASS: CONJURATION", "LOCATION: MURKEY - WANKARA", "SCHOOL RANK: 1")


sc2 = school1("NAME: MARVARD MAGE ACADEMY", 'ARCHMAGE: MANDALF THE GRAY',

              "STUDENTS: "+str(random.randint(2000,5000)), "TEACHERS: "+str(random.randint(100,1000)),

                "BEST MAGE-CLASS: ALTERATION", "LOCATION: ARSTOTZKA - MERLYN", "SCHOOL RANK: 3")


sc3 = school1("NAME: YONSEI MAGE ACADEMY", 'ARCH MAGE: MUMBLEDORE',

              'STUDENTS: '+str(random.randint(2000,5000)), "TEACHERS: "+str(random.randint(100,1000)),

                "BEST MAGE-CLASS: DESTRUCTION", "LOCATION: SOUTH BOREA - MEOUL", "SCHOOL RANK: 4")




print(sc1.okulIsmi+"\n"+sc1.archMage+'\n'+sc1.ogrenciSayisi+'\n'+sc1.ogretmenSayisi+'\n'+sc1.enBasariliSinif+'\n'+sc1.konum+'\n'+sc1.okulSiralamasi+'\n')
print(sc2.okulIsmi+"\n"+sc2.archMage+'\n'+sc2.ogrenciSayisi+'\n'+sc2.ogretmenSayisi+'\n'+sc2.enBasariliSinif+'\n'+sc2.konum+'\n'+sc2.okulSiralamasi+'\n')
print(sc3.okulIsmi+"\n"+sc3.archMage+'\n'+sc3.ogrenciSayisi+'\n'+sc3.ogretmenSayisi+'\n'+sc3.enBasariliSinif+'\n'+sc3.konum+'\n'+sc3.okulSiralamasi+'\n')
