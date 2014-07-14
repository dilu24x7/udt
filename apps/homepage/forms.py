from django import forms


class ContactForm(forms.Form):

    email = forms.EmailField()
    phone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
    def clean_phone(self):
        email = self.cleaned_data.get('phone')
        return email
    def clean_message(self):
        email = self.cleaned_data.get('message')
        return email
    def clean(self):
        return self.cleaned_data
