from django import forms

class kullanicikayitForm(forms.Form):
    tckimlik = forms.CharField(max_length=50,label="Tc Kimlik NO")
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