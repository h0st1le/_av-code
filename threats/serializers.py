from rest_framework import serializers
from threats.models import Visitor, Visit


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('address', 'timestamp', 'endpoint',)


class VisitorSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = Visitor
        fields = ('alienvaultid', 'visits',)


class DetailsSerializer(serializers.Serializer):
    # updated field type to reflect change in DRF v3.0
    id = serializers.ReadOnlyField()
    input = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    is_valid = serializers.ReadOnlyField()
    reputation_val = serializers.ReadOnlyField()
    first_activity = serializers.ReadOnlyField()
    last_activity = serializers.ReadOnlyField()
    activities = serializers.ReadOnlyField()
    activity_types = serializers.ReadOnlyField()
    error_status = serializers.ReadOnlyField()
