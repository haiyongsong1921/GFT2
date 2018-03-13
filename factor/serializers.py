from rest_framework import serializers

from .models import L1Factor, L2Factor


class L1FactorSerializer(serializers.ModelSerializer):
    target_type = serializers.ChoiceField(choices=L1Factor.TYPE)

    class Meta:
        model = L1Factor
        fields = ('id', 'summary', 'description', 'factor_type', 'target_type', 'owner')


class L2FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Factor
        fields = ('id', 'summary', 'description', 'novices', 'advanced_beginners',
                  'competent', 'proficient', 'expert')
