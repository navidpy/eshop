from django import forms
from django.contrib.auth.models import User

from eshop_account.models import UserInformation

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']

class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید','class':'form-control'}),
        label='نام',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید','class':'form-control'}),
        label='نام خانواگی'
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید','class':'form-control'}),
        label='نام کاربری'
    )
    phone = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا شماره تلفن خود را وارد کنید','class':'form-control'}),
        label='شماره تلفن',
        max_length=11
    )
    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید','class':'form-control'}),
    #     label='ایمیل'
    # )
    def clean_username(self):
        user_name = self.cleaned_data.get('username').lower().replace(" ","")
        for i in user_name:
            if i not in letters:
                raise forms.ValidationError('نام کاربری نا معتبر است. شما میتوانید از کاراکترهای 0-9 و a-z و زیرخط استفاده کنید.')
        if len(user_name) < 5:
            raise forms.ValidationError('نام کاربری کوتاه است. حداقل طول مجاز 5 کاراکتر است.')
        return user_name
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone[:2] == '09' and len(phone) == 11:
            return phone
        raise forms.ValidationError("شماره تلفن وارد شده اشتباه است")

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if '@gmail.com' not in email:
    #         raise forms.ValidationError('ایمیل وارد شده نامعتبر است')
    #
    #     elif len(email) > 40:
    #         raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 40 باشد')
    #     return email

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید'}),
        label="کلمه ی عبور"
    )


class RegisterForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد کنید'}),
        label='نام',
        max_length=14
    )
    family = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد کنید'}),
        label='نام خانوادگی',
        max_length=20

    )
    phone = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا شماره تلفن خود را وارد کنید'}),
        label='شماره تلفن',
        max_length=11
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری',
        max_length=25
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل'
    )
    def clean_username(self):
        user_name = self.cleaned_data.get('username').lower().replace(" ","")
        for i in user_name:
            if i not in letters:
                raise forms.ValidationError('نام کاربری نا معتبر است. شما میتوانید از کاراکترهای 0-9 و a-z و زیرخط استفاده کنید.')
        if len(user_name) < 5:
            raise forms.ValidationError('نام کاربری کوتاه است. حداقل طول مجاز 5 کاراکتر است.')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این نام کاربری پیش تر در سامانه ثبت شده است.')

        return user_name

    def clean_phone(self):
        phone=self.cleaned_data.get('phone')
        qs=UserInformation.objects.filter(phone=phone)
        if qs.exists():
            raise forms.ValidationError('این شماره تلفن پیش تر در سامانه ثبت شده است.')
        if phone[:2]=='09' and len(phone)==11:
            return phone
        raise forms.ValidationError("شماره تلفن وارد شده اشتباه است")
    def clean_email(self):
        email=self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if '@gmail.com' not in email:
            raise forms.ValidationError('ایمیل وارد شده نامعتبر است')
        elif is_exists_user_by_email:
            raise forms.ValidationError('این ایمیل پیش تر در سامانه ثبت شده است.')

        elif len(email) > 40:
            raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 40 باشد')
        return email

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
    )



class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور فعلی خود را وارد کنید','class':'form-control'}),
        label="کلمه ی عبور فعلی : ",
        max_length=20
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید','class':'form-control'}),
        label="کلمه ی عبور جدید : ",
        max_length=20
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را تکرار کنید','class':'form-control'}),
        label="تکرار کلمه ی عبور : "
    )

class ChangeNewPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید','class':'form-control'}),
        label="کلمه ی عبور جدید : ",
        max_length=20
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را تکرار کنید','class':'form-control'}),
        label="تکرار کلمه ی عبور : "
    )