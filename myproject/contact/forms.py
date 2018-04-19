from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    full_name = forms.CharField(required=True)
    email_adress = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.Textarea()
    
    
    class Meta:
        model = Contact
        fields = ('full_name', 'email_adress', 'subject', 'message')


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Your name:"
        self.fields['email_adress'].label = "Your email:"
        self.fields['subject'].label = "Your subject:"
        self.fields['message'].label = "What do you want to say?"

    
    
    