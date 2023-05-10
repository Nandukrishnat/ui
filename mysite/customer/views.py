from django.shortcuts import render,redirect

from customer.models import Customer

# Create your views here.


def index(request):
    if request.method == "POST":
        customer = Customer(name=request.POST["name"], email=request.POST["email"], phone_no=request.POST["phone_no"])
        customer.save()
        return redirect("/customer")
    
    
    elif request.method == "GET":
        all_customer = Customer.objects.all()
        return render(request,"customer/index.html",{"customer":all_customer})
    
def create(request):
    return render(request,"customer/create.html")
        
def update(request,id):
    if request.method == "GET":
        customer = Customer.objects.get(id=id)
        return render(request,"customer/update.html",{"customer":customer})
    

  

    elif request.method == "POST":

        customer = Customer.objects.get(id=id)

        customer.name = request.POST.get("name")
        customer.email=request.POST.get("email")
        customer.phone_no=request.POST.get("phone_no")
        customer.save()

        return redirect("/customer")
    
def delete(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customer")
