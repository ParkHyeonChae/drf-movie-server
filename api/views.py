"""api/views.py"""

from django.shortcuts import render
from .models import MovieList as MovieListModel
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import MovieListSerializer


class MovieList(APIView):
    """A function, able to get list of MovieList
    - GET
    Arguments:
        viewsets {[APIView]} -- [GET handler]
    QuerystringOptions:
        #ordering
        limit -- [default 20, data amount in page]
        page -- [default 1, page of data-perpage]
        sort_by -- [default id, order by title or year or rating]
        order_by -- [default desc, order by desc or asc]

        #filterings
        genre -- [default All, filter by genres]
    Returns:
        [GET-status] -- [GET-200-HTTP_200_OK]

    - POST(create)
    A function, able to Post and register new Movie
    Arguments:
        viewsets {[APIView]} -- [POST, handler]
    Raises:
        ValidationError: [POST-HTTP_400_BAD_REQUEST]
    Returns:
        [status] -- [POST-201_CREATED]
    """

    def post(self, request, format=None):
        data={}
        data['title'] = request.GET.get("title")
        data['year'] = request.GET.get("year")
        data['rating'] = request.GET.get("rating")
        data['genre'] = request.GET.get("genre")
        data['summary'] = request.GET.get("summary")

        serializer = MovieListSerializer(data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
    def get(self, request, format=None):
        start = 0
        last = 20
        page = 1
        sort_by = 'id'
        genre = ''

        # GET요청으로 들어온 URL Parameter 저장
        get_limit = self.request.query_params.get('limit', None)
        get_page = self.request.query_params.get('page', None)
        get_sort_by = self.request.query_params.get('sort_by', None)
        get_genre = self.request.query_params.get('genre', None)
        get_order_by = self.request.query_params.get('order_by', None)

        # limit
        if get_limit:
            if int(get_limit) >= 1 and int(get_limit) <= 50:
                last = int(get_limit)
            else:
                get_limit = 20
        else:
            get_limit = 20
            
        # page Parameter (페이지당 limit갯수를 반환하는 로직)
        if get_page:
            if int(get_page) >= 1 and int(get_page) * last <= 500:
                start = (last * int(get_page)) - last
                last = last * int(get_page)
            else:
                get_page = 1
        else:
            get_page = 1

        # sort_by Parameter
        if get_sort_by:
            if get_sort_by == 'title':
                sort_by = 'title'
            elif get_sort_by == 'year':
                sort_by = '-year'
            elif get_sort_by == 'rating':
                sort_by = '-rating'

        # genre Parameter
        if get_genre:
            genre = get_genre

        # order_by Parameter
        if get_order_by:
            if get_order_by == 'asc':
                if sort_by[0] != '-':
                    tmp_sort_by = []
                    tmp_sort_by.append('-')
                    tmp_sort_by.append(sort_by)
                    sort_by = ''.join(tmp_sort_by)
                else:
                    sort_by = sort_by[1:]

        # json Response에 출력될 movie data
        queryset = MovieListModel.objects.filter(genre__icontains=genre).order_by(sort_by)[start:last]
        serializer = MovieListSerializer(queryset, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'api/index.html')