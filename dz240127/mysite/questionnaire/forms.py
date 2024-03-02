from django import forms


class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    num = forms.IntegerField()
    cc_myself = forms.BooleanField(required=False)