from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(max_length=30,min_length=2,widget=forms.TextInput(attrs={'class':'input','placeholder':'আপনার পূর্ণ নামটি লিখেন অবশ্যই ২ অক্ষবের বেশি হবে'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input','placeholder':'ইমেল অ্যাড্রেস '}))
    phone = forms.RegexField(max_length=11,min_length=11,regex=r'^017',widget=forms.TextInput(attrs={'class':'input','placeholder':'ফোন নাম্বার '}))
