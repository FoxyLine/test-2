from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf  import get_token as get_csrf_token
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet

from ..models import Card
from .serializers import CardDetailSerializer


class CardListViewSet(ViewSet):
    serializer_class = CardDetailSerializer
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication,
    )

    queryset = Card.objects.all()

    def list(self, request):
        user = request.user
        cards = Card.objects.filter(user=user)

        res = {}
        for type, _ in Card.TYPE_CARDS:
            qs = cards.filter(type=type)
            serializer = CardDetailSerializer(qs, many=True)
            res[type] = serializer.data

        return Response(res, status=200)

    def create(self, request):
        serializer = CardDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        card = get_object_or_404(Card, pk=pk)
        card.delete()
        return Response(card.id, status=200)

    @action(detail=True, methods=["PUT"])
    def change_desk(self, request, pk=None):
        card = get_object_or_404(Card, pk=pk)

        serializer = CardDetailSerializer(card, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(detail=True, methods=["PUT"])
    def change_order(self, request, pk=None):
        order = request.data.get("order", None)
        serializer = CardDetailSerializer(card, data={"order": order}, partial=True)
        return Response(serializer.data)

@api_view(["GET"])
def obtain_csrf_token(request):
    token = get_csrf_token(request)
    return Response({"csrfToken": token})
