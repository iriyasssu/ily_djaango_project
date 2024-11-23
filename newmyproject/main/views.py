from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import JsonResponse
import json

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category__id=category_id)

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)

    return render(request, 'product_list.html', {'categories': categories, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def rate_product(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        data = json.loads(request.body)
        product.rating = data.get('rating', 0)
        product.save()
        return JsonResponse({'status': 'success'})
