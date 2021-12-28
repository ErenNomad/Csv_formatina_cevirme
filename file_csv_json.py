import json
import pandas as pd
from csv import writer

class Lessons:
    def __init__(self):
        pass

    def convert(self):
        kontrol1 = 0
        df_json = pd.read_json('kisi.json')
        df = df_json.to_csv('kisi.csv')
        kontrol1 + 1
        if kontrol1 > 1:
            df.to_csv('kisi.csv', mode='a', index=False, header=False)


    def kayit(self):
        self.ogrenci = input("Öğrenci adı giriniz :")
        self.ogrencino = int(input("Öğrenci numarası giriniz :"))
        self.ders = input("Ders adı giriniz :")
        self.vizeNot = int(input(f"{self.ders.title()} dersinin vize notunuzu giriniz :"))
        self.finalNot = int(input(f"{self.ders.title()} dersinin final notunuzu giriniz :"))


        kisi_dict = [{
            'ogrenci': self.ogrenci,
            'ogrencino': self.ogrencino,
            'ders': self.ders,
            'vizeNot': self.finalNot,
            'finalNot': self.vizeNot
            }]

        with open('kisi.json', 'w') as json_dosya:
            json.dump(kisi_dict, json_dosya)
    def derskayitlari(self):


        kontrol = input("Daha çok ders girecek misiniz?      E/H: ")
        while kontrol == "E" or "H":

            if kontrol.lower() == "E":
                pass
            else:
                break

        dersSayisi = int(input("Kaç tane daha ders gireceksiniz :"))
        self.ogrenci = input("Öğrenci adı giriniz :")
        self.ogrencino = int(input("Öğrenci numarası giriniz :"))
        kontrol2 = 0
        for i in range(0,dersSayisi):

            self.ders = input("Ders adı giriniz :")
            self.vizeNot = int(input(f"{self.ders.title()} dersinin vize notunuzu giriniz :"))
            self.finalNot = int(input(f"{self.ders.title()} dersinin final notunuzu giriniz :"))
            with open('kisi.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([self.ogrenci, self.ogrencino, self.ders, self.vizeNot, self.finalNot])

        f_object.close()

Lessons().kayit()
try:
    Lessons().convert()
except AttributeError:
    Lessons().convert()
    os.system("cls")
    os.system("clear")
Lessons().derskayitlari()
