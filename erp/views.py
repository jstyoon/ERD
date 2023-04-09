from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect ,render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from erp.forms import ProductForm


from erp.models import Product


def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'erp/home.html')
    else:
        return redirect('/sign-in')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Stock
from .forms import ProductForm


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'erp/product_list.html', {'products': products})


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            stock = Stock(product=product, quantity=0)
            stock.save()
            messages.success(request, f"{product.name}이(가) 등록되었습니다.")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'erp/product_form.html', {'form': form})


@login_required
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'erp/stock_list.html', {'stocks': stocks})


@login_required
def stock_create(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        stock = Stock.objects.get(product=product)
        stock.quantity += quantity
        stock.save()
        messages.success(request, f"{product.name}의 재고가 {quantity}개 추가되었습니다.")
        return redirect('stock_list')
    return render(request, 'erp/stock_form.html', {'product': product})