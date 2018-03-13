from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import list_route

from user_and_role.permissions import *
from .models import L1Factor, L2Factor
from .serializers import L1FactorSerializer, L2FactorSerializer


def not_found_l1_response(id):
    return Response(status=status.HTTP_400_BAD_REQUEST, data='Cannot find the L1 factor which ID is %s' % id)


def not_found_l2_response(id):
    return Response(status=status.HTTP_400_BAD_REQUEST, data='Cannot find the L2 factor which ID is %s' % id)


class SharedL1FactorView(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    permission_classes = (IsAuthenticated, IsDesignerUser)
    queryset = L1Factor.shared.all()
    serializer_class = L1FactorSerializer
    factor_type = L1Factor.SHARED
    category = L1Factor.shared
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        shared_factors = self.queryset
        serializer = L1FactorSerializer(shared_factors, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        new_factor = L1Factor()
        new_factor.summary = request.data.get('summary', None)
        new_factor.description = request.data.get('description', None)
        new_factor.factor_type = self.factor_type
        new_factor.target_type = request.data.get('target_type', None)
        new_factor.owner = request.user.username
        new_factor.save()
        serializer = L1FactorSerializer(new_factor)
        return Response(serializer.data)

    def retrieve(self, request, id, *args, **kwargs):
        try:
            factor = self.category.get(id=id)
            serializer = L1FactorSerializer(factor)
            return Response(serializer.data)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(id)

    def update(self, request, id):
        try:
            factor = self.category.get(id=id)
            factor.summary = request.data.get('summary', None)
            factor.description = request.data.get('description', None)
            factor.target_type = request.data.get('target_type', None)
            factor.save()
            serializer = L1FactorSerializer(factor)
            return Response(serializer.data)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(id)

    def destroy(self, request, id):
        try:
            factor = self.category.get(id=id)
            factor.delete()
            return Response()
        except L1Factor.DoesNotExist:
            return not_found_l1_response(id)


class PrivateL1FactorView(SharedL1FactorView):
    permission_classes = (IsAuthenticated, IsReviewerUser)
    queryset = L1Factor.private.all()
    serializer_class = L1FactorSerializer
    factor_type = L1Factor.PRIVATE
    category = L1Factor.private


class L2FactorView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    permission_classes = (IsAuthenticated, IsReviewerUser)
    queryset = L2Factor.objects.all()
    serializer_class = L2FactorSerializer
    lookup_field = 'id'

    def list(self, request, l1_id, *args, **kwargs):
        try:
            l1 = L1Factor.objects.get(id=l1_id)
            l2s = L2Factor.objects.filter(l1_factor=l1)
            serializer = L2FactorSerializer(l2s, many=True)
            return Response(serializer.data)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(l1_id)

    def retrieve(self, request, l1_id, id, *args, **kwargs):
        try:
            l1 = L1Factor.objects.get(id=l1_id)
            l2 = L2Factor.objects.get(id=id)
            if l2.l1_factor != l1:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="L1 and L2 factors are not match")
            serializer = L2FactorSerializer(l2)
            return Response(serializer.data)
        except L2Factor.DoesNotExist:
            return not_found_l2_response(id)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(l1_id)

    def create(self, request, l1_id, *args, **kwargs):
        try:
            l1 = L1Factor.objects.get(id=l1_id)
            l2 = L2Factor(l1_factor=l1)
            l2.summary = request.data.get('summary', '')
            l2.description = request.data.get('description', '')
            l2.novices = request.data.get('novices', '')
            l2.advanced_beginners = request.data.get('advanced_beginners', '')
            l2.competent = request.data.get('competent', '')
            l2.proficient = request.data.get('proficient', '')
            l2.expert = request.data.get('expert', '')
            l2.save()
            serializer = L2FactorSerializer(l2)
            return Response(serializer.data)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(l1_id)

    def update(self, request, l1_id, id, *args, **kwargs):
        try:
            l1 = L1Factor.objects.get(id=l1_id)
            l2 = L2Factor.objects.get(id=id)
            if l2.l1_factor != l1:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="L1 and L2 factors are not match")
            l2.summary = request.data.get('summary', l2.summary)
            l2.description = request.data.get('description', l2.description)
            l2.novices = request.data.get('novices', l2.novices)
            l2.advanced_beginners = request.data.get('advanced_beginners', l2.advanced_beginners)
            l2.competent = request.data.get('competent', l2.competent)
            l2.proficient = request.data.get('proficient', l2.proficient)
            l2.expert = request.data.get('expert', l2.expert)
            l2.save()
            serializer = L2FactorSerializer(l2)
            return Response(serializer.data)
        except L2Factor.DoesNotExist:
            return not_found_l2_response(id)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(l1_id)

    def destroy(self, request, l1_id, id, *args, **kwargs):
        try:
            l1 = L1Factor.objects.get(id=l1_id)
            l2 = L2Factor.objects.get(id=id)
            if l2.l1_factor != l1:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="L1 and L2 factors are not match")
            l2.delete()
            return Response('L2 Factor removed.')
        except L2Factor.DoesNotExist:
            return not_found_l2_response(id)
        except L1Factor.DoesNotExist:
            return not_found_l1_response(l1_id)


