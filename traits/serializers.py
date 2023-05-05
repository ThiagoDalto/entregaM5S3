from rest_framework import serializers
from datetime import datetime
from traits.models import Trait


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: list) -> Trait:
        traits_list = validated_data.pop('traits')
        trait_obj = Trait.objects.create(**validated_data)
        for trait_dict in traits_list:
            trait_obj, created = Trait.objects.get_or_create(
                **trait_dict
            )
            traits_list.set(trait_obj)

        return traits_list

    # def get_created_at(self, obj):
    #     now = datetime.now()
    #     date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    #     return date_time
