from django import forms
from django.contrib.auth.models import User

from eshop_order.models import Discount


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1,
        min_value=1,
        max_value=1000
    )
class DiscountForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'کد تخفیف خود را وارد نمایید ...'}),
    )
    def clean_code(self):
        code = self.cleaned_data.get('code')
        is_discount = Discount.objects.filter(code=code , active=True).first()
        if is_discount is None:
            raise forms.ValidationError("کد تخفیف وارد شده اشتباه است(به بزرگی و کوچکی حروف دقت کنید)")
        elif is_discount.total <= is_discount.count:
            raise forms.ValidationError("کد تخفیف وارد شده منقضی شده است")
        is_discount.count+=1
        is_discount.save()
        return is_discount.percentage



