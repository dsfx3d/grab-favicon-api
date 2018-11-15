from django import forms



class GrabFaviconForm(forms.Form):

    url = forms.URLField(required=True)
