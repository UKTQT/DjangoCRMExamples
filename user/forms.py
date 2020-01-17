from django import forms
import mysql.connector
import request

# Cihaz EKleme Formu --------------------------------------------------------------

class cihazekleform(forms.Form):
    CIHAZ_TIP = [
        ('secilmedi', 'SEÇİNİZ'),
        ('hub', 'HUB'),
        ('topraks', 'Toprak Sensörü'),
        ('nems', 'Nem Sensörü'),
        ('basincs', 'Basınç Sensörü')
    ]
    cihaz_tip = forms.ChoiceField(choices=CIHAZ_TIP)


    def clean(self):
        cihaz_tip = self.cleaned_data.get("cihaz_tip")
        valuessss = {
            "cihaz_tip": cihaz_tip
        }
        return valuessss


class cihazkayitForm(forms.Form):
    CIHAZ_TIP = [
        ('secilmedi', 'SEÇİNİZ'),
        ('hub', 'HUB'),
        ('topraks', 'Toprak Sensörü'),
        ('nems', 'Nem Sensörü'),
        ('basincs', 'Basınç Sensörü')
    ]
    mydb = mysql.connector.connect(
        host="185.207.37.66",
        user="ufuk",
        passwd="Ukt_2699",
        database="sis")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT NAME FROM SUBSCRIBER")
    myresult = mycursor.fetchall()

    kullanicilarr = []
    a = 0
    for x in myresult:
        a = a+1
        kullanicilarr.append((a,x[0]))





    cihaz_tip = forms.ChoiceField(choices=CIHAZ_TIP)
    kullanicilar = forms.ChoiceField(choices=kullanicilarr)
    def clean(self):
        cihaz_tip = self.cleaned_data.get("cihaz_tip")
        kullanicilar = self.cleaned_data.get("kullanicilar")
        valuesss = {
            "cihaz_tip" : cihaz_tip,
            "kullanicilar" : kullanicilar
        }
        return valuesss

    mycursor.close()


# Müşteri Ekleme formu
class kullanicikayitForm(forms.Form):
    tckimlik = forms.CharField(max_length=11,label="Tc Kimlik NO")
    musteriad = forms.CharField(max_length=30,label="Müşteri Adı")
    musterisoyad = forms.CharField(max_length=50,label="Müşteri Soyad")
    musteritelefon = forms.CharField(max_length=11,label="Telefon No")
    musteriadres = forms.CharField(max_length=200,label="Adres")
    def clean(self):
        tckimlik = self.cleaned_data.get("tckimlik")
        musteriad = self.cleaned_data.get("musteriad")
        musterisoyad = self.cleaned_data.get("musterisoyad")
        musteritelefon = self.cleaned_data.get("musteritelefon")
        musteriadres = self.cleaned_data.get("musteriadres")
        valuess = {
            "tckimlik" : tckimlik,
            "musteriad" : musteriad,
            "musterisoyad" : musterisoyad,
            "musteritelefon" : musteritelefon,
            "musteriadres" : musteriadres
        }
        return valuess

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı = ")
    password = forms.CharField(max_length=20,label = "Parola = ",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label = "Parolayı Doğrula = ",widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "username" : username,
            "password" : password
        }
        return values