# M5 - Pet Kare
 .
from pets.serializers import PetSerializer
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer

 full_pet_data = {
  "name": "Strogonoff",
  "age": 4,
  "weight": 5,
  "sex": "Female",
  "group": {
    "scientific_name": "Felis catus"
  },
  "traits": [
    {"name": "curious"},
    {"name": "hairy"}
  ]
}


serializer = PetSerializer(data=full_pet_data)
serializer.is_valid()
serializer.validated_data