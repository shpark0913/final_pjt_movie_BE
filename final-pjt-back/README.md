# 👍 0일차 (221115)

### 1. **앱 만들기**

- **movies** - 영화 데이터를 다루기 위한 앱
- **accounts** - 로그인, 회원가입, 탈퇴 등의 기능 구현을 위한 앱

### 2. 기본 설정

- 기본 User 모델 ****변경
  
  - AUTH_USER_MODEL을 **accounts.User** 모델로 변경

- AJAX 요청 준비
  
  - axios 설치

- CORS (Cross-Origin Resource Sharing)
  
  - HTTP Response Header 중에서 **Access-Control-Allow_Origin** 사용
    
    - 이를 위해 djnago-cors-headers 설치
    
    - settings.py에 추가 설정
      
      - INSTALLED_APPS 에 corsheaders 추가
      
      - MIDDLEWARE에 corsheaders.middleware.CorsMiddleware, django.middleware.common.CommonMiddleware 추가
      
      - CORS_ALLOWED_ORIGINS에 교차 출처 자원 공유를 위해
        
        local host Domain을 등록

### 3. 회원가입

- 기본적인 인증 절차를 DRF의 기본 인증 방식 중 하나인 **TokenAuthentication** 으로 결정
  - TokenAuthentication의 특징
    1. 간단히 구현 가능
    2. 기본적인 보안 기능 제공
    3. 다양한 외부 패키지 이용

. settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 정의해서 TokenAuthentication 사용할 것임을 명시함

. INSTALLED_APPS에 rest_framework.authtoken을 등록해 각 User마다 고유 Token이 생성되는 것을 확인

- dj-rest-auth 사용하기 위해 설치함
  - Registration 기능을 사용하기 위해 django-allauth 설치
  - INSTALLED_APPS에 관련 App들 추가하고 SITE_ID = 1 설정
    - 현재 프로젝트가 첫번째 사이트임을 알 수 있다.

---

# 👍 1일차 (221116)

### 목표

1. ERD 만들기 ( 추가 기능 구현을 위한 Model 제외하고, 기본 Model들만 포함)
2. ERD 내에 있는 Model 구현하기
3. TMDB에서 json data 받아서 DB에 저장하기

### 모델 구현 ( Movie )

- movies 앱의 models.py에 작성
- field : title, overview, release_date, vote_average, poster_path, backdrop_path
- ManyToManyField를 이용해 중개 테이블 생성
  - `genres = models.ManyToManyField(Genre)`

### 모델 구현 ( Genre )

- movies 앱의 models.py에 작성
- field : name

### DB에 Json data 저장하기

- 시도했던 방법
  
  : API_key 를 통해 TMDB 에서 json data 받기
  
  → 원하는 data만 식별해 DB에 저장하기
  
  → 이를 이용해 fixtures data 만들기
  
  → 실패

- 실패한 이유는?
  
  - 오류가 많이 남
    
    ex) 특정 영화의 장르를 조회할 때
    
    ```
      url마다 integer로 응답하거나 text로 응답하는 등의 차이가 있음
    ```

- 방향 수정
  
  - view 함수를 통해 구현해보기로 함

---

# 👍 2일차 (221117)

### 목표

1. 1일차에 실패했던 DB에 json data 저장하기 성공

2. DB에 저장한 data를 바탕으로 fixtures data 만들기

3. DB에 저장한 data를 serializer를 통해 json 형식으로 넘겨주기
   
   (Vue 에서 이용가능하도록)

### DB에 json data 저장하기

1. view 함수에서 반복문을 통해 api_key를 통한 data를 수신함
2. Movie 모델의 field 중 overview, release_date, poster_path, backdrop_path 가 없는 항목들이 있는 것을 발견.
   - 이 항목들 때문에 오류들이 다수 발생
3. 이 field들이 모두 존재하는 data가 필요하기 때문에, if 문을 사용해서 필터링을 함
   - 필터링 된 data만 fixtures data로 만들기로 함
4. 데이터 저장 성공

### Vue 에 data 넘겨주기

- serializer를 통해 Vue에 json 형태로 data를 넘겨주기로 결정
  - postman을 사용해 전체 영화 조회, 단일 영화 조회가 성공적으로 되는 것을 확인

---

# 👍 3일차 (221118)

### 목표

1. ERD 추가하기
2. Review 모델 수정

### ERD 만들기

- Review 모델 구현을 위해 ERD 수정

### Review 모델 구현

- field : title, content, vote_average, movie, user
  - movie, user은 ForeignKey를 통해 생성
- Movie의 Detail 페이지에서 로그인을 한 유저가 댓글을 달 수 있는 기능 구현
  - CRUD (Create, Read, Update, Delete) 기능 구현
  - form 을 이용한 방법과 serializer를 이용한 방법 2가지 구현
    - 이 중 serializer로 구현한 방법 선택
      - R, U, D 기능 구현이 더 간편

---

# 👍 4일차 (221119)

### 목표

1. Review model의 field 중 vote_average 속성 변경

### Review 의 field 변경

- Vue에서 ture, false 의 2가지로 평점을 관리하는게 편하겠다는 의견 수용
- 기존 FloatField에서 BooleanField로 변경

---

# 👍 5일차 (221120)

### 목표

1. FE와 중간 점검 및 방향 협의

---

# 👍 6일차 (221121)

### 목표

1. Username을 이용해 User의 pk를 조회할 수 있는 함수 만들기
2. review component에 작성한 user의 pk가 조회되는데, 이를 username 으로 바꾸기
3. movie detail 페이지에서 pk로 조회되는 장르를 genre name으로 조회하기
4. movie의 pk를 이용해서 TMDB에서 추천 영화 불러오기
5. 특정 user가 좋아한 영화와 싫어한 영화 조회하기
6. 특정 user가 작성한 댓글들 조회하기

### Username을 이용해 User의 pk 조회하기

- `user/str:username/` 라는 새로운 경로를 지정해 view 함수를 생성

### Review componet에 user의 pk가 아닌 username 나오게 하기

- serializer를 이용해 해결
  - `username = serializers.CharField(source='user.username')` 을 추가해 username을 추가로 조회할 수 있도록 구현

### movie detail 페이지에서 genre를 pk가 아닌 name으로 조회하기

```
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ('genre',)

class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
```

- GenreSerializer를 만들어서 해결

### 특정 movie의 pk를 이용해 TMDB에서 추천 영화 불러오기

```
@api_view(['GET'])
def recommend(request, movieid):
    request_url = f"<https://api.themoviedb.org/3/movie/{movieid}/recommendations?api_key={API_KEY}&language=ko-KR&page=1>"
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
```

- f-string을 사용해 해결
- TMDB로부터 받아온 새로운 영화들을 다시 활용하기 위해 DB에 저장하는 기능을 추가함.

### user가 좋아하거나 싫어한 영화 조회하기, 작성한 댓글 조회하기 기능 통합

```jsx
@api_view(['GET'])
def profile(request, username):
    u = get_object_or_404(get_user_model(), username=username)
    reviews = get_list_or_404(Review, user_id=u.pk)
    movie_like = []
    movie_unlike = []
    review_like = []
    review_unlike = []
    for review in reviews:
        if review.vote_average:
            movie_like.append(review.movie_id)
            review_like.append({'movieid': review.movie_id, 'content': review.content})
        else:
            movie_unlike.append(review.movie_id)
            review_unlike.append({'movieid': review.movie_id, 'content': review.content})
    return Response({'userid': u.pk, 'username': u.username, 'likes': movie_like, 'unlikes': movie_unlike, 'like_reviews': review_like, 'unlike_reviews': review_unlike})
```

- 코드를 작성해 보니
  
  - user가 좋아한 영화 목록 조회, 싫어한 영화 목록 조회
  
  - 작성한 댓글 조회
    
    각각의 코드가 유사하여 하나로 통합

- 편의를 위해 Response에 userid 와 username을 명시적으로 표시

---

# 👍 7일차 (221122)

### 목표

1. mypage에서 user가 작성한 review 조회할 때 코드 수정
   
   1. review serializer 활용
   
   2. movie detail serializer 활용
   - 수정 이유는?
     - 불필요한 코드 줄이기
     - vue에서 component 재사용성을 위해

2. user가 좋아하는 영화의 장르 비율 계산하기
   
   1. 절대도수를 Response하는 방식으로 구현 예정

### mypage 에서 data 를 손쉽게 조회하기 위해 profile view 함수 수정 & user가 좋아하는 영화의 장르 비율 계산하는 기능 추가

# 

## ver.1

```python
@api_view(['GET'])
def profile(request, username):
    u = get_object_or_404(get_user_model(), username=username)
    reviews = get_list_or_404(Review, user_id=u.pk)
    movie_like = []
    movie_unlike = []
    review_all = []
    for review in reviews:
        m = Movie.objects.get(movieid=review.movie_id)
        movieObj = {'movieid': m.movieid, 'moviename': m.title, 'poster_path': m.poster_path}
        reviewObj = {'movie': movieObj, 'content': review.content}
        review_all.append(reviewObj)
        if review.vote_average:
            movie_like.append(movieObj)
        else:
            movie_unlike.append(movieObj)

    return Response({'userid': u.pk, 'username': u.username, 'likes': movie_like, 'unlikes': movie_unlike, 'review_all': review_all})
```

- 입력받은 username을 이용해 u라는 유저 찾기
  
  → 좋아한 영화: movie_like, 싫어한 영화: movie_unlike, 작성한 리뷰들: review_all 에 각각 저장

- Object의 property 이름이 달라서 재사용이 힘들었음

## ver.2

```python
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    reviews = get_list_or_404(Review, user_id=user.pk)
    movie_like_genre = []
    movie_like = []
    movie_unlike = []
    for review in reviews:
        movie = Movie.objects.get(movieid=review.movie_id)
        movieSerializer = MovieDetailSerializer(movie)
        movieObj = {'movieid': movie.movieid, 'moviename': movie.title, 'poster_path': movie.poster_path}
        if review.vote_average:
            movie_like_genre.append(movieObj)
            movie_like.append(movieSerializer.data)
        else:
            movie_unlike.append(movieSerializer.data)
    reviewSerializer = ReviewListSerializer(reviews, many=True)
    like_genres = {}

    if movie_like_genre:
        for elt in movie_like_genre:
            m = Movie.objects.get(movieid=elt['movieid'])
            m = list(m.genres.all().values())
            for elt in m:
                if elt['name'] not in like_genres:
                    like_genres[elt['name']] = 1
                else:
                    like_genres[elt['name']] += 1

    return Response({'userid': user.pk, 'username': user.username, 'likes': movie_like, 'unlikes': movie_unlike, 'review_all': reviewSerializer.data, 'like_genres': like_genres})
```

- MovieDetailSerializer와 ReviewListSerializer를 이용해 Object의 property 이름을 일치시킴
  
  → vue에서 component의 재사용성 확보

- 좋아한 영화의 장르들을 like_genres에 저장

- BUT! movie_like_genre와 movie_like를 통합할 수 있을 것 같아 더 간단한 코드를 구현해보기로 결심

## ver.3

```python
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    reviews = get_list_or_404(Review, user_id=user.pk)
    reviewSerializer = ReviewListSerializer(reviews, many=True)
    movie_like = []
    movie_unlike = []
    like_genres = {}
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

    return Response({'userid': user.pk, 'username': user.username, 'likes': movie_like, 'unlikes': movie_unlike, 'review_all': reviewSerializer.data, 'like_g data를 조회해 like_genres 완성
```

- movie_like_genre를 따로 만들지 않고 movie_like에서 data를 조회해 like_genres 완성



### movie의 pk를 사용해서 출연진 정보 불러오기

- profile이 존재하는 배우만 5명 선별하기로 함

```python
@api_view(['GET'])
def movie_credit(request, movieid):
    request_url = f"<https://api.themoviedb.org/3/movie/{movieid}/credits?api_key={API_KEY}&language=ko-KR>"
    credits_all = requests.get(request_url).json()
    actor_all = []
    for actor in credits_all['cast']:
        if actor['known_for_department'] == 'Acting' and actor['profile_path']:
            actor_all += [{'name': actor['name'], 'profile_path': actor['profile_path']}]
            if len(actor_all) == 5:break
    return Response({'credit': actor_all})
```
