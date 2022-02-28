from django.shortcuts import redirect, render
from book.models import Book
from django.http import HttpResponse
# Create your views here.
# their r two types of views 1)function base view,2)class view


def homepage(request):
  print(request.method)
  print(request.POST,type(request.POST))

  name = request.POST.get("bname")
  price = request.POST.get("bprice")
  qty = request.POST.get("bqty")

  if request.method =="POST":
    if not request.POST.get("bid"):
      book_name = name
      book_price = price 
      book_qty = qty
      # print(book_name,book_qty,book_price)
      Book.objects.create(name= book_name, price=book_price, qty=book_qty)
      return redirect("homepage")
    else:
      bid =  request.POST.get("bid")
      try:
        book_obj = Book.objects.get(id=bid)
      except Book.DoesNotExist as err_msg:
        print(err_msg)
      book_obj.name = name
      book_obj.price = price
      book_obj.qty = qty
      book_obj.save()
      return redirect("show_all_books")

# print(request.build_absolute_uri())
  elif request.method =="GET":
    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request ,"home1.html", context=data)
# return HttpResponse("<h1>Hi Hellow</h1><h5>good evening</h5>")



# http://127.0.0.1:8000/home/


def show_all_books(request):
  all_books = Book.objects.all()
  data ={"books": all_books}
  return render(request,"show_books.html",context=data)

def edit_data(request,id):
  book = Book.objects.get(id=id)
  return render(request,template_name="home1.html",context={"single_book": book})


def delete_data(request,id):
  if request.method == "GET":
    try:
      book = Book.objects.get(id=id)
    except Book.DoesNotExist as err_msg:
      print(err_msg)
      return HttpResponse(f"Book Does Not exits for ID:- {id}")
    else:
      book.delete()
    return redirect("show_all_books")
  else:
    return HttpResponse(f"Request method: {request.method} Not allowed..! only POST method is allowed")  


# def view_a(request):
#   return HttpResponse("in view_a")

# def view_b(request):
#   return HttpResponse("in view_b")

# def view_c(request):
#   return HttpResponse("in view_c")

# def view_d(request):
#   return HttpResponse("in view_d")


# from django.shortcuts import render
from book.forms import AddressForm
 
# Create your views here.
def form_home(request):
  context = {"form": AddressForm()}
  return render(request, "form_home.html", context)

