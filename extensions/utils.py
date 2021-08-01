from . import Jalali
from django.utils import timezone


def jalali_converter(time):
    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    time = timezone.localtime(time)
    time_to_str = f"{time.year},{time.month},{time.day}"
    time_to_list = list(Jalali.Gregorian(time_to_str).persian_tuple())
    time_to_list[1] = months[int(time_to_list[1])-1]
    output = f'{time_to_list[2]} {time_to_list[1]} {time_to_list[0]}'
    return output


