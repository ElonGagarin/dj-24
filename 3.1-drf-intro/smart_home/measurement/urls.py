from django.urls import path
from .views import MeasurementsList, SensorsList, SensorDetail

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('measurements/', MeasurementsList.as_view()),
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),

]
