# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from rest_framework.response import Response

from .models import Measurements, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorCreateSerializer

class MeasurementsList(generics.CreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer

    def sensor_create(self, serializer):
        serializer.save()
        
class SensorsList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateSerializer

    def post(self, request):
        serializer = SensorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data)

class SensorDetail(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def patch(self, request):
    #     print('>>> ',request.data)
    #     serializer = SensorCreateSerializer(data=request.data, partial=True)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(request.data)