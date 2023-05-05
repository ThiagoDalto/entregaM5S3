from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from pets.models import PetSex, Pet
from traits.models import Trait
from groups.models import Group


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        coerce_to_string=False,
    )
    sex = serializers.ChoiceField(
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    traits_count = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Pet:

        group_dict = validated_data.pop(
            "group",
        )
        group, _ = Group.objects.get_or_create(**group_dict)
        traits_dict = validated_data.pop("traits")

        pet = Pet.objects.create(**validated_data, group=group)
        for trait in traits_dict:
            traits, _ = Trait.objects.get_or_create(**trait)
            pet.traits.add(traits)

        return pet

    def update(self, instance: Pet, validated_data: dict):

        if validated_data.get("traits", None):
            trait_list: list = validated_data.pop("traits", None)
            instance.traits.clear()
            for trait in trait_list:
                trait_obj, created = Trait.objects.get_or_create(**trait)
                instance.traits.add(trait_obj)

        group: dict = validated_data.pop("group", None)
        if group:
            group_obj, created = Group.objects.get_or_create(**group)
            instance.group = group_obj

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def validate_scientific_name(self, scientific_name: str) -> str:
        sci_name_exists = Group.objects.filter(scientific_name=scientific_name).exists()
        if sci_name_exists:
            raise serializers.ValidationError(
                detail="Scientific name already\
                 exists"
            )
        return scientific_name

    def get_traits_count(self, obj):

        return obj.traits.count()
