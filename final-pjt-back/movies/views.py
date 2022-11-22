from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse
from django.contrib.auth import get_user_model

import requests, random, json

from .models import Movie, Genre, Review
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewListSerializer

API_KEY = '3e6bef93583f44f23148ae1a83169eb1'


# DB 에 저장되어 있는 영화 중 장르에 따라 10개(10개 미만일 수도 있음) 추천 
@api_view(['GET'])
def recommend10(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    sampleNum = min(10, len(list(genre.movie_set.all()[:100])))
    movies = random.sample(list(genre.movie_set.all()[:100]), sampleNum)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 회원가입할 때 입력받은 선호 장르를 가지고 장르로 영화 추천하기
@api_view(['POST'])
def firstrecommend(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    like_genres = user.prefer.json()
    for elt in like_genres.keys():
    #     recommend10(request, genre_pk=int(elt))
    #     break
    # return HttpResponse()
        genre = get_object_or_404(Genre, pk=int(elt))
        sampleNum = min(10, len(list(genre.movie_set.all()[:100])))
        movies = random.sample(list(genre.movie_set.all()[:100]), sampleNum)
        serializer = MovieListSerializer(movies, many=True)
        break
    return Response(serializer.data)
        


# 전체 영화 조회
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 단일 영화 조회
@api_view(['GET'])
def movie_detail(request, movieid):
    # movie = Movie.objects.get(movieid=movieid)
    movie = get_object_or_404(Movie, movieid=movieid)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


# GET : 특정 영화 전체 review 조회  /  POST : 특정 영화의 review 작성
@api_view(['POST', 'GET'])
def review(request, movieid):
    if request.method == 'POST':
        movie = Movie.objects.get(movieid=movieid)
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        reviews = get_list_or_404(Review, movie=movieid)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


# GET : 특정 review 조회  /  PUT : 특정 review 수정  /  DELETE : 특정 review 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def review_UD(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewListSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


# username 받으면 user의 pk 반환하기
@api_view(['GET'])
def want_user_pk(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return Response({'user_pk': user.pk})


# username 받고 그 user가 좋아요, 싫어요 한 영화와 작성한 댓글 출력
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    reviews = get_list_or_404(Review, user_id=user.pk)
    reviewSerializer = ReviewListSerializer(reviews, many=True)
    movie_like = []
    movie_unlike = []
    like_genres = user.prefer.json()
    for review in reviews:
        movie = Movie.objects.get(movieid=review.movie_id)
        movieSerializer = MovieDetailSerializer(movie)
        if review.vote_average:
            movie_like.append(movieSerializer.data)
        else:
            movie_unlike.append(movieSerializer.data)
    if movie_like:
        for elt in movie_like:
            for elt2 in elt['genres']:
                if elt2['name'] not in like_genres:
                    like_genres[elt2['name']] = 1
                else:
                    like_genres[elt2['name']] += 1

    return Response({'userid': user.pk, 'username': user.username, 'likes': movie_like, 'unlikes': movie_unlike, 'review_all': reviewSerializer.data, 'like_genres': like_genres})


# tmdb에서 추천 영화 받기
@api_view(['GET'])
def recommend(request, movieid):
    request_url = f"https://api.themoviedb.org/3/movie/{movieid}/recommendations?api_key={API_KEY}&language=ko-KR&page=1"
    movies = requests.get(request_url).json()
    
    # 받아온 movie들 DB에 추가 저장
    for movie in movies['results']:
        movie_instance = Movie()
        movie_instance.title  = movie['title']
        movie_instance.movieid  = movie['id']
        movie_instance.backdrop_path = movie['backdrop_path']
        movie_instance.release_date = movie.get('release_date')
        movie_instance.vote_average = movie['vote_average']
        movie_instance.overview = movie['overview']
        movie_instance.poster_path = movie['poster_path']
        if movie_instance.overview and movie_instance.release_date and movie_instance.poster_path and movie_instance.backdrop_path:
            movie_instance.save()
            for genre in movie.get('genre_ids'):
                movie_instance.genres.add(genre)
    m = movies['results']
    return Response({'recommendations': m})


@api_view(['GET'])
def movie_credit(request, movieid):
    request_url = f"https://api.themoviedb.org/3/movie/{movieid}/credits?api_key={API_KEY}&language=ko-KR"
    credits_all = requests.get(request_url).json()
    actor_all = []
    for actor in credits_all['cast']:
        if actor['known_for_department'] == 'Acting' and actor['profile_path']:
            actor_all += [{'name': actor['name'], 'profile_path': actor['profile_path']}]
            if len(actor_all) == 5:break
    return Response({'credit': actor_all})


# 초반 fixtures data 만들기 위한 함수
def get_movie_datas(request):
    for i in range(1, 30):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            movie_instance = Movie()
            movie_instance.title  = movie['title']
            movie_instance.movieid  = movie['id']
            movie_instance.backdrop_path = movie['backdrop_path']
            movie_instance.release_date = movie.get('release_date')
            movie_instance.vote_average = movie['vote_average']
            movie_instance.overview = movie['overview']
            movie_instance.poster_path = movie['poster_path']
            # movie_instance.genres = movie.get('genre_ids')   
            if movie_instance.overview and movie_instance.release_date and movie_instance.poster_path and movie_instance.backdrop_path:
                movie_instance.save()
                for genre in movie.get('genre_ids'):
                    movie_instance.genres.add(genre)
    return HttpResponse()


def get_genre(request):
    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()
    for genre in genres['genres']:
        g = Genre()
        print(genre)
        g.genreid = genre['id']
        g.name = genre['name']
        if g.genreid and g.name:
            g.save()
    return HttpResponse()