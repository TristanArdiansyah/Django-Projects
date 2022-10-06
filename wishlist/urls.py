from django.urls import path
from wishlist.views import *
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', request_function, name='request_function'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_json_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('ajax/', show_wishlist_ajax, name='ajax'),
    path('ajax/submit', show_create_wishlist, name='show_create_wishlist')
]