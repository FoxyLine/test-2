from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CardDetailSerializer

from ..models import Card


class CardListViewSet(ViewSet):
    serializer_class = CardDetailSerializer
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

    def create(self, request):
        
        serializer = CardDetailSerializer(
            data=request.data)

        serializer.is_valid()
        serializer.save(user=request.user)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        card = get_object_or_404(Card, pk=pk)
        card.delete()

        return Response(card.id, status=200)

    @action(detail=True, methods=["PUT"])
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