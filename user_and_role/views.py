from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import list_route, detail_route
import json

from .serializers import UserSerializer
from .permissions import *


class CurrentUserView(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['GET'])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def admins(self, request):
        admins = User.admins.all()
        serializer = UserSerializer(admins, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def designers(self, request):
        designers = User.designers.all()
        serializer = UserSerializer(designers, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def organizers(self, request):
        organizers = User.organizers.all()
        serializer = UserSerializer(organizers, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def reviewers(self, request):
        reviewers = User.reviewers.all()
        serializer = UserSerializer(reviewers, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def roles(self, request):
        roles_data = json.dumps(User.ROLES)
        return Response(roles_data)


    @detail_route(methods=['PUT'], permission_classes=[IsAdminUser])
    def assign_role(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            new_role = request.data.get('role', '')
            if not new_role:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            user.role = new_role
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

