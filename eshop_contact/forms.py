from django import forms
from django.core import validators
class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید','class':'form-control'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(20,"نام و نام خانوانوادگی نمیتواند بیشتر از 20 کاراکتر باشد"),
            validators.MinLengthValidator(4,"نام و نام خانوانوادگی معتبر نیست"),
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید','class':'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(35, "ایمیل نمیتواند بیشتر از 35 کاراکتر باشد"),
            validators.MinLengthValidator(15, "ایمیل معتبر نیست"),
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان پیام خود را وارد کنید','class':'form-control'}),
        label='عنوان پیام',
        validators=[
            validators.MaxLengthValidator(40, "عنوان پیام نمیتواند بیشتر از 40 کاراکتر باشد"),
            validators.MinLengthValidator(2, "عنوان پیام معتبر نیست"),
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا متن پیام خود را وارد کنید','class':'form-control' , 'rows':8,'id':'message'}),
        label='متن پیام',
        validators=[
            validators.MaxLengthValidator(500, "متن پیام نمیتواند بیشتر از 500 کاراکتر باشد"),
            validators.MinLengthValidator(10, "متن پیام معتبر نیست"),
        ]
    )

class CommentsForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا متن پیام خود را وارد کنید','class':'form-control' , 'rows':8,'id':'message'}),
        label='متن پیام',
        validators=[
            validators.MaxLengthValidator(1000, "متن نظر نمیتواند بیشتر از 1000 کاراکتر باشد"),
            validators.MinLengthValidator(2, "متن پیام معتبر نیست"),
        ]
    )
