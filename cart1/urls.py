from django.urls import path
from .views import addtocartview,CartListView  # new
urlpatterns = [
path('', addtocartview, name='addtocart'), # new
path('view/',CartListView.as_view(),name='viewcart'),
]

