from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Author,Book, User_Book, Category, User_Author
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@login_required(login_url='/registration/login', redirect_field_name=None)
def index(request):
    ##my books
    currently_reading = User_Book.objects.filter(user_id=request.user, status='c')
    to_be_read = User_Book.objects.filter(user_id=request.user, status='t')
    read = User_Book.objects.filter(user_id=request.user, status='r')
    my_books = {
        'currently_reading':currently_reading,
        'to_be_read':to_be_read,
        'read':read
    }
    ##my authors
    my_authors = User_Author.objects.filter(user_id=request.user,follow=1)
    for a in my_authors:
        books_num = len(a.author_id.book_set.all())
        a.author_id.books_num = books_num
    ##my categories
    my_categories = request.user.category_set.all()

    return render(request, 'library/index.html', {'my_books':my_books, 'my_authors':my_authors, 'my_categories':my_categories})

class BookList(ListView):
    model = Book
    context_object_name = "books"
    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        return context

class AuthorList(ListView):
    model = Author
    context_object_name = "authors"

    def get_queryset(self):
        authors = Author.objects.all()
        for a in authors:
            a.is_followed = False
            if(self.request.user.is_authenticated and User_Author.objects.filter(author_id=a,user_id=self.request.user,follow=1)):
                a.is_followed = True
        return authors

def categorys(request):
    categorys = Category.objects.all()
    data = {}
    for c in categorys:
        data[c.name] = c.id
    return JsonResponse({'categorys': data})

def book(request,book_id):
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    user_book = User_Book.objects.none()
    is_favourite_category = False
    is_followed_author = False
    if(request.user.is_authenticated):
        if(book.category_id.users.filter(id=request.user.id)): is_favourite_category = True
        if (User_Author.objects.filter(author_id=book.author_id,user_id=request.user,follow=1)): is_followed_author = True
        user_book = User_Book.objects.filter(book_id=book,user_id=request.user).first()
    return render(request, 'library/book_detail.html', {'book': book, 'user_book': user_book, 'is_favourite_category':is_favourite_category, 'is_followed_author':is_followed_author})

def author(request,author_id):
    # author = Author.objects.get(id=author_id)
    author = get_object_or_404(Author, id=author_id)
    author_books = author.book_set.all()
    user_author = User_Author.objects.all()
    is_followed_author = False
    if (request.user.is_authenticated):
        if(User_Author.objects.filter(author_id=author,user_id=request.user,follow=1)): is_followed_author = True
        user_author = User_Author.objects.filter(author_id=author,user_id=request.user).first()
    return render(request, 'library/author_detail.html', {'author':author,'user_author':user_author, 'author_books':author_books, 'is_followed_author':is_followed_author})

def category(request,category_id):
    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category,id=category_id)
    cat_books = category.book_set.all()
    is_favourite_category = False
    if (request.user.is_authenticated):
        if(category.users.filter(id=request.user.id)): is_favourite_category = True
    return render(request, 'library/category_detail.html', {'category':category,'cat_books':cat_books, 'is_favourite_category':is_favourite_category})

@login_required(login_url='/registration/login', redirect_field_name=None)
def book_status(request, book_id):
    a = ['r', 't', 'c', 'n']
    status = 'n'
    for s in a:
        if request.POST.get(s):
            status = s
            break
    book = Book.objects.get(id=book_id)
    obj, created = User_Book.objects.update_or_create(
        book_id=book, user_id=request.user,
        defaults = {'status': status}
    )
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/registration/login', redirect_field_name=None)
def book_rating(request, book_id):
    rating = request.POST.get('rating')
    book = Book.objects.get(id=book_id)
    obj, created = User_Book.objects.update_or_create(
        book_id=book, user_id=request.user,
        defaults={'rating': rating}
    )
    return JsonResponse({'done': True})

@login_required(login_url='/registration/login', redirect_field_name=None)
def author_rating(request, author_id):
    rating = request.POST.get('rating')
    author = Author.objects.get(id=author_id)
    obj, created = User_Author.objects.update_or_create(
        author_id=author, user_id=request.user,
        defaults={'rating': rating}
    )
    return JsonResponse({'done': True})

@login_required(login_url='/registration/login', redirect_field_name=None)
def cat_fav(request, category_id):
    category = Category.objects.get(id=category_id)
    case = request.POST.get('case')
    if(case == 'add'):
        category.users.add(request.user)
        return JsonResponse({'done': True, 'case': 'add'})
    elif(case == 'remove'):
        category.users.remove(request.user)
        return JsonResponse({'done': True, 'case': 'remove'})
    else:
        return JsonResponse({'done': False})

@login_required(login_url='/registration/login', redirect_field_name=None)
def author_follow(request, author_id):
    author = Author.objects.get(id=author_id)
    case = request.POST.get('case')
    if(case == 'add'):
        obj, created = User_Author.objects.update_or_create(
            author_id=author, user_id=request.user,
            defaults={'follow': 1}
        )
        # author.users.add(request.user)
        return JsonResponse({'done': True, 'case': 'add'})
    elif(case == 'remove'):
        obj, created = User_Author.objects.update_or_create(
            author_id=author, user_id=request.user,
            defaults={'follow': 0}
        )
        # author.users.remove(request.user)
        return JsonResponse({'done': True, 'case': 'remove'})
    else:
        return JsonResponse({'done': False})
