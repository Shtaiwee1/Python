from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('process_reg', views.process_reg ),
    path('process_login', views.process_login ),
    path('books', views.books_page ),
    path('add_fav_book', views.add_fav_book ),
    path('books/<int:book_id>', views.edit_show_book ),
    path('clear', views.clear ),
    path('update_info/<int:book_id>', views.update_info ),
    path('favourites/<int:book_id>/<int:user_id>', views.fav_book ),
    path('unfavourites/<int:book_id>/<int:user_id>', views.unfav_book ),]
    