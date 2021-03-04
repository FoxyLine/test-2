from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CardDetailSerializer

from ..models import Card

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CardListViewSet(ViewSet):
    serializer_class = CardDetailSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    queryset = Card.objects.all()

    def list(self, request):
        user = request.user
        cards = Card.objects.filter(user=user)

        res = {}
        for type, full_type in Card.TYPE_CARDS:
            qs = cards.filter(type=type)
            serializer = CardDetailSerializer(qs, many=True)
            res[type] = serializer.data

        return Response(res, status=200)

    @csrf_exempt
    def create(self, request):
        
        serializer = CardDetailSerializer(
            data=request.data)

        serializer.is_valid()
        serializer.save(user=request.user)

        return Response(serializer.data)

    @csrf_exempt
    def destroy(self, request, pk=None):
        card = get_object_or_404(Card, pk=pk)
        card.delete()

        return Response(card.id, status=200)

    @action(detail=True, methods=["PUT"])
    @csrf_exempt
    def change_type(self, request, pk=None):
        type = request.GET["to"]
        card = get_object_or_404(Card, pk=pk)
        card.type = type
        card.save()

        serializer = CardDetailSerializer(card)
        return Response(serializer.data)

    @action(detail=True, methods=["PUT"])
    def change_desk(self, request, pk=None):
        type = request.GET["type"]
        order = request.GET["order"]
        order = int(order)

        card = get_object_or_404(Card, pk=pk)
        card.type = type
        card.save()

        card.set_order(order)

        serializer = CardDetailSerializer(card)
        return Response(serializer.data)

    @action(detail=True, methods=["PUT"])
    def change_order(self, request, pk=None):
        try:
            order = request.GET["to"]            
        except:
            return Response("must specify the 'to' parameter", status=404)

        try:
            order = int(order)
        except:
            return Response(" parameter 'to' must be positive integer", status=404)
        

        card = get_object_or_404(Card, pk=pk)
        card.set_order(order)

        serializer = CardDetailSerializer(card)
        return Response(serializer.data)