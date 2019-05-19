from django.conf.urls import url
from django.urls import path
from . import views, authentication, records

urlpatterns = [
    path('', views.main_page, name='index'),
    path('bookss/', views.book_list, name='books'),
    path('books/', views.Books.as_view(), name='books'),
	path('books/reserved/', views.Books_Reserved.as_view(), name='books_reserved'),
	path('books/available/', views.Books_Available.as_view(), name='books_available'),
	path('authors/', views.Authors.as_view(), name='authors'),
	path('users/', views.Users.as_view(), name='users'),
	url(r'^user/(?P<name>\w{0,50})/$', views.user_profile),
    url(r'^author/(?P<name>\w{0,50})/$', views.author_profile),
    url(r'^book/(?P<name>\w{0,50})/$', views.book_profile),
    url(r'^authorization/$', authentication.authorization, name='authorization'),
    path('records/', records.records, name='records'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), 
]