from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.parsers import JSONParser
from .models import Pet
from .serializers import PetSerializer


class PetView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        pets = Pet.objects.all()

        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class PetDetailView(APIView):
    def patch(self, request: Request, pet_id: int):
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, request: Request, pet_id: int):
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pet_id: int):
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)
