"""api/views.py"""

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import MovieListSerializer
from .models import MovieList

   
# @api_view(['GET'])
# def movie_list(request):
#     MovieLists = MovieList.objects.order_by('id')[:20]
#     serializers = MovieListSerializer(MovieLists, many=True)
#     return Response(serializers.data)


class MovieListViewSet(viewsets.generics.ListAPIView):
    serializer_class = MovieListSerializer  

    def get_queryset(self):
        queryset = MovieList.objects.order_by('id')[:20]
        # state = self.request.query_params.get("state", None)
        # country = self.request.query_params.get("country", None)
        # host = self.request.query_params.get("host", None)
        # if state:
        #     queryset = queryset.filter(state__name=state)
        # elif country:
        #     queryset = queryset.filter(state__country__name=country)
        # if host:
        #     queryset = queryset.filter(host__username=host)
        # queryset = filter_backend(queryset, self.request.query_params)
        print(queryset)
        return queryset