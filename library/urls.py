from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/$', views.BookList.as_view(), name="books"),
    url(r'^authors/$', views.AuthorList.as_view(), name="authors"),
    url(r'^categorys/$', views.categorys, name="categorys"),
    url(r'^books/([0-9]+)$', views.book, name="viewbook"),
    url(r'^authors/([0-9]+)$', views.author, name="viewauthor"),
    url(r'^categorys/([0-9]+)$', views.category, name="viewcategory"),
    url(r'^books/([0-9]+)/status$', views.book_status),
    url(r'^books/([0-9]+)/rating$', views.book_rating),
    url(r'^authors/([0-9]+)/rating$', views.author_rating),
    url(r'^authors/([0-9]+)/follow', views.author_follow),
    url(r'^categorys/([0-9]+)/favourites', views.cat_fav),
]