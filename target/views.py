from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import list_route, detail_route
import json

from .models import EvaluationTarget
from .serializers import TargetSerializer
from user_and_role.permissions import *


class TargetView(mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 GenericViewSet):
    permission_classes = (IsAuthenticated, IsOrganizerUser)
    queryset = EvaluationTarget.objects.all()
    serializer_class = TargetSerializer

    @list_route(methods=['GET'])
    def individuals(self, request):
        individuals = EvaluationTarget.individuals.all()
        serializer = TargetSerializer(individuals, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def teams(self, request):
        teams = EvaluationTarget.teams.all()
        serializer = TargetSerializer(teams, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        target = TargetSerializer(data=request.data)
        if target.is_valid():
            target.save()
            return Response(status=status.HTTP_201_CREATED, data=target.data)

        return Response(status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        try:
            target = EvaluationTarget.objects.get(id=pk)
            target_serializer = TargetSerializer(target, data=request.data)
            if target_serializer.is_valid():
                target_serializer.save()
                Response(target_serializer.data)
        except EvaluationTarget.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

        return Response(status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, *args, **kwargs):
        try:
            target = EvaluationTarget.objects.get(id=pk)
            target.delete()
            return Response()
        except EvaluationTarget.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['GET'])
    def target_types(self, request):
        target_types = json.dumps(EvaluationTarget.TYPE)
        return Response(target_types)