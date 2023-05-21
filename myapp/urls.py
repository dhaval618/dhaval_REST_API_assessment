from django.urls import path
from.views import *

urlpatterns = [
    path('read_data/<int:pk>', ReadData.as_view() ,name='read_data'),
    path('create_data/', CreateData.as_view() ,name='create_data'),
    path('update_data/<int:pk>', UpdateData.as_view() ,name='update_data'),
    path('delete_data/<int:pk>', DeleteData.as_view() ,name='delete_data'),
]