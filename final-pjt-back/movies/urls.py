from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 전체 영화 조회
    path('', views.movie_list, name='movie_list'),
    
    # 단일 영화 조회
    path('<int:movieid>/', views.movie_detail, name='movie_detail'),
    
    # 영화 credit 조회
    path('<int:movieid>/credit/', views.movie_credit, name='movie_credit'),
    
    # GET : 특정 영화 전체 review 조회 / POST : 특정 영화의 review 작성
    path('<int:movieid>/review/', views.review, name='review'),
    
    # GET : 특정 review 조회 / PUT : 특정 review 수정 / DELETE : 특정 review 삭제
    path('review/<int:review_pk>/', views.review_UD, name='review_UD'),
    
    # DB 에 저장되어 있는 영화 중 장르에 따라 10개(10개 미만일 수도 있음) 추천 
    path('recommend/<int:genre_pk>/', views.recommend10, name='recommend10'),

    # username 받으면 user의 pk 반환하기
    path('user/<str:username>/', views.want_user_pk, name='want_user_pk'),
    
    # username 받고 그 user가 좋아요, 싫어요 한 영화와 작성한 댓글 출력
    path('user/<str:username>/profile/', views.profile, name='profile'),
    
    # 회원가입할 때 입력받은 선호 장르를 가지고 장르로 영화 추천하기
    # path('user/<str:username>/firstrecommend/', views.firstrecommend, name='firstrecommend'),
    
    # tmdb에서 추천 영화 받기
    path('<int:movieid>/recommendations/', views.recommend, name='recommend'),

    # 초반 fixtures data 만들기 위한 경로
    path('get_movie_datas/', views.get_movie_datas, name='get_movie_datas'),
    path('get_genre/', views.get_genre, name='get_genre'),
]