from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=250)
    last_name  = forms.CharField(max_length=250)
    enrolled = forms.BooleanField(required=False)
    homeroom = forms.CharField(max_length=20, required=False)
    adults = forms.CharField(max_length=250, required=False)
    phone = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    school = forms.MultipleChoiceField(required=True,
                                       widget=forms.CheckboxSelectMultiple,
                                       choices=(('sc1', 'SC1'),
                                                ('sc2', 'SC2'),
                                                ('sc3', 'SC3')))


    
