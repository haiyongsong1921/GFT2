from rest_framework import serializers

from .models import EvaluationTarget


class TargetSerializer(serializers.ModelSerializer):
    target_type = serializers.ChoiceField(choices=EvaluationTarget.TYPE)

    class Meta:
        model = EvaluationTarget
        fields = ('id', 'name', 'target_type')
