from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import AllowAny, IsAuthenticated
from parkitu.models import Car, Garage
from parkitu.serializers import CarSerializer, GarageDetailSerializer, GarageSerializer, CarListSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return [AllowAny()]
    #     return super().get_serializer_class()


class GarageViewSet(ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["retrieve, list"]:
            return GarageDetailSerializer
        return super().get_serializer_class()
