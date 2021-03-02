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
        pass

    def destroy(self, request, pk=None):
        pass

    @action(detail=True, methods=["PUT"])
    def change_type(self, request, pk=None):
        pass

    @action(detail=True, methods=["PUT"])
    def change_order(self, request, pk=None):
        pass