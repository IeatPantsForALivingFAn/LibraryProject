from django import forms
from .models import Student, User
#student forms
class StudentSignUpForm(forms.Form):
    name = forms.CharField(max_length=256)
    roll_no = forms.IntegerField()
    sem = forms.IntegerField()
    branch = forms.ChoiceField(choices =[
                    ('EXTC','EXTC'),
                    ('ETRX','ETRX'),
                    ('Comps','Comps'),
                    ('Bio','Bio'),
                    ('Mech','Mech'),
                    ('Civil','Civil'),
                    ])
    email = forms.EmailField()
    set_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget= forms.PasswordInput)

    def clean_password(self):
        password1 = self.cleaned_data['set_password']
        password2 = self.cleaned_data['confirm_password']

        if password1!=password2 and password1 and password2:
            raise forms.ValidationError('Passwords do not match')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email


class Login(forms.Form):
    username = forms.CharField(max_length =100,widget=forms.TextInput(attrs={'class':'login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login'}))
