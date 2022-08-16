from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render,redirect
from products.models import *
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'products.html')


    

def product_billing(request)    :
    data=Products.objects.all()
    invoice=Invoice.objects.all()
    return render(request,'product-billing.html',{"data":data,"invoice":invoice})


def add_product(request):
    if request.method=="POST":
        p_name=request.POST['p_name']
        desc=request.POST['desc']
        category=request.POST['category']
        sub_category=request.POST['sub_category']
        weight=request.POST['weight']
        unit=request.POST['unit']
        quantity=request.POST['quantity']
        amount=request.POST['amount']

        obj=Products(p_name=p_name,desc=desc,category=category,sub_category=sub_category,weight=weight,unit=unit,quantity=quantity,amount=amount)
        obj.save()
        return redirect('add-product')

    data=Products.objects.all()
    return render(request,'add-products.html',{"data":data})


def AddToInvoice(request,):
    id=request.POST['id']
    qty=request.POST['qty']
    

    obj=Invoice(p_id_id=id,qty=qty)
    obj.save()
    


    return redirect('product-billing')


def update_quantity(request):

    total=0
    qty=request.GET['qty']
    i_id=request.GET['i_id']
    order_detail=Invoice.objects.get(id=i_id)
    order_detail.qty=qty
    print(qty)
    
    order_detail.save()
    product_total=order_detail.p_id.price* int(qty)
    bag_data = Products.objects.all()
    for prod in bag_data:
            price=prod.p_id.amount*prod.qty
            total+=price

            
   
    return JsonResponse({"total": total,"product_total":product_total})



def search(request):
    search_word=request.POST['search_box']
    search_list=search_word.split(' ')
    search_products=Products.objects.filter(Q(p_name__icontains=search_word)|Q(desc__icontains=search_word)|Q(category__icontains=search_word)|
    Q(sub_category__icontains=search_word))

    return render(request,'search.html',{"s_data":search_products}) 


def check_out(request):
    data=Invoice.objects.all()
    data.delete()
    return redirect("product-billing")