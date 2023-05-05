from rest_framework import serializers
from datetime import datetime
from groups.models import Group


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> Group:
        group = Group.objects.create(**validated_data)

        return group

    # def get_created_at(self, obj):
    #     now = datetime.now()
    #     date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    #     return date_time

    