import itertools

from django.shortcuts import render, redirect

from eshop_product_brand.models import ProductBrand
from eshop_products.models import Product
from eshop_products_category.models import ProductCategory
from eshop_sliders.models import Slider
from eshop_settings.models import SiteSetting, SiteImageSetting


# header code behind
def header(request, *args, **kwargs):
    siteSetting = SiteSetting.objects.first()
    siteImage = SiteImageSetting.objects.first()
    context = {
        'setting': siteSetting,
        'siteImage': siteImage
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    siteSetting = SiteSetting.objects.first()
    siteImage = SiteImageSetting.objects.first()
    context = {
        'setting': siteSetting,
        'siteImage': siteImage
    }
    return render(request, 'shared/Footer.html', context)


def sidebar(request, *args, **kwargs):
    brands = ProductBrand.objects.all()
    categories = ProductCategory.objects.all()
    siteImage = SiteImageSetting.objects.first()
    context = {
        'siteImage': siteImage,
        'brands': brands,
        'categories': categories
    }
    return render(request, 'shared/sidebar.html', context)


def page_not_found(request, *args, **kwargs):
    return render(request, '404.html')


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
def home_page(request):
    siteSetting = SiteSetting.objects.first()
    sliders = Slider.objects.all()
    siteImage = SiteImageSetting.objects.first()
    most_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]
    categories = ProductCategory.objects.all()
    listOfCategory = []
    for category in categories:
        listOfCategory.append(Product.objects.get_product_by_category_for_home(category))
    context = {
        'setting': siteSetting,
        'sliders': sliders,
        'siteImage': siteImage,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products),
        'categories': categories,
        'listOfCategory': listOfCategory,
    }
    return render(request, "home_page.html", context)


def about_page(request):
    siteSetting = SiteSetting.objects.first()
    siteImage = SiteImageSetting.objects.first()
    context = {
        'setting': siteSetting,
        'siteImage': siteImage
    }
    return render(request, "about_page.html", context)


def image_product_list(request):
    siteImage = SiteImageSetting.objects.first()
    contect = {
        'siteImage': siteImage
    }
    return render(request, "products/image_product_list.html", contect)
def icon(request):
    siteImage = SiteImageSetting.objects.first()
    context = {
        'siteImage': siteImage
    }
    return render(request, "shared/settingLode/icon.html", context)

def meta(request):
    siteSetting = SiteSetting.objects.first()
    siteImage = SiteImageSetting.objects.first()
    context = {
        'setting': siteSetting,
        'siteImage': siteImage
    }
    return render(request, "shared/meta.html", context)