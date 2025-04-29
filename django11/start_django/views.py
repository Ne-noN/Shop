from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'start_django/list.html',
                  {'category':category,
                            'categories': categories,
                            'products': products
                   })
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id ,slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'start_django/detail.html',
                  {'product': product,
                           'cart_product_form':cart_product_form})


'''
scheme - схема запроса
body - тело запроса ввиде строки байтов
method - метод запроса GET POST
encoding - кодировка
content_type - тип содержимого запроса (значение заголовка CONTENT_TYPE)
GET - объект ввиде словаря, который содержит параметры запроса GET
POST - объект ввиде словаря, который содержит параметры запроса POST
COOKIES - отправленные клиентом куки
FILES - отправленные клиентом файлы
META - хранит все заголовки http в виде словаря

def index(request):
    return HttpResponse('<h2>Главная страница</h2>')

def products(request):
    return HttpResponse('<h2>Список товаров</h2>')

def new(request):
    return HttpResponse('<h2>Новые товары</h2>')

def top(request):
    return HttpResponse('<h2>Лучшие товары на этой неделе</h2>')

    #return HttpResponse( 'Заголовки', headers={'SecretCode': '124558'})
    #return HttpResponse('Ошибка', status = 400, reason='Incorrect data')
    return HttpResponse('<h2>О сайте</h2>', content_type='text/plain', charset='utf-16')

def about(request,missiya,adres):
    return HttpResponse(f'<h2>О сайте</h2>
                            <p>Миссия: {missiya}</p>
                            <p>Адрес: {adres} </p>
                        '
                        )

def contact(request):
    return HttpResponse(f'<h2>Контакты</h2>')


def user (request,name,age):
    return HttpResponse(f'<h2>Имя:{name}</h2> \n <h2>Возраст:{age}</h2>')

'''