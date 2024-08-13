from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.db.models import Q
def form(request):
    data = Category.objects.all()
    if request.method == "POST":
        book_obj = book()
        book_obj.book_name = request.POST.get('bookname')
        book_obj.book_author = request.POST.get('bookauthor')
        book_obj.category = Category.objects.get(category_name=request.POST.get('category'))
        book_obj.book_price = request.POST.get('bookprice')
        book_obj.book_img = request.FILES['bookimg']
        book_obj.save()
        return redirect('/')
    return render(request, 'form.html', {'value': data})
def show(request):
    data = book.objects.all()
    data1 = Category.objects.all()
    if request.method == "POST":
        s_item = request.POST.get("search")
        c_item = request.POST.get('category')

        if c_item:
            data = data.filter(category_id=c_item)

        data = data.filter(Q(book_name__icontains=s_item) | Q(book_author__icontains=s_item) | Q(book_price__icontains=s_item))
        print(data)
    return render(request, 'show.html', {'b_data': data, 'value': data1})
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get("user_name")
        Email = request.POST.get("mail")
        pwsd = request.POST.get("pwd")

        sign_obj = SIGNUP()
        sign_obj.username = uname
        sign_obj.email = Email
        sign_obj.password = pwsd
        sign_obj.save()
    return render(request, 'signup.html')
def login(request):
    if request.method == "POST":
        EMAIL = request.POST.get("mail")
        PWD = request.POST.get("pwd")
        user = SIGNUP.objects.filter(email=EMAIL, password=PWD).values()
        if user is not None:
            return redirect("/")
        else:
            return HttpResponse("Email or password is incorrect")
    return render(request,'login.html')
def product(request,id):
    data = book.objects.filter(id=id)
    return render(request, 'product.html', {'value': data})
def buynow(request,id):
    data = book.objects.filter(id=id)
    if request.method == "POST":
        return HttpResponse("Order conformed..")
    return render(request, 'buy.html', {'value': data})
def cart(request):
    return render(request, 'cart.html')
