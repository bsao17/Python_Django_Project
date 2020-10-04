
from django.urls import path
from django.urls import register_converter

from appTwo import views as appTwo_views
from appTwo import convert

register_converter(convert.twoDigitDayConverter, 'dd')

urlpatterns = [
    path('djangorocks', appTwo_views.djangorocks),
    path('picture/<str:category>', appTwo_views.picture_details),
    path('picture/<str:category>/<int:year>/<int:month>', appTwo_views.picture_details),
    path('picture/<str:category>/<int:year>/<int:month>/<dd:day>', appTwo_views.picture_details),

]
