from django.shortcuts import render, redirect

from datetime import datetime, timedelta

from product.models import Product

from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == "POST":
        date = request.POST.get('date')
        date_format = '%Y-%m-%d'
        parsed_date = datetime.strptime(date, date_format).date()

        product = Product(name=request.POST["name"], date=parsed_date, price=float(
            request.POST["price"]), quantity=request.POST["qty"], customer_id=request.POST["customer_id"])
        product.save()
        return redirect("/product")

    elif request.method == "GET":
        all_products = Product.objects.all()
        return render(request, "product/index.html", {"products": all_products})


def create(request):
    return render(request, "product/create.html")


def update(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        return render(request, "product/update.html", {"product": product})

    elif request.method == "POST":

        product = Product.objects.get(id=id)

        print(request.POST.get("active"))

        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.date = request.POST.get("date")
        product.quantity = request.POST.get("qty")
        product.customer_id = request.POST.get("customer_id")

        if request.POST.get("active") == None:
            date_format = '%Y-%m-%d'
            parsed_date = datetime.strptime(
                request.POST.get("date"), date_format).date()
            today = datetime.now().date()
            two_months_ago = today - timedelta(days=2 * 30)
            if parsed_date <= two_months_ago:
                product.active = False

        elif request.POST.get("active") == "on":
            product.active = True
        product.save()

        return redirect("/product")


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/product")


def products(request, id):
    product = Product.objects.filter(customer_id=id)
    return render(request, "product/index.html", {"products": product})
