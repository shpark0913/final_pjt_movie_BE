## FE, BE 각자의 README

- [프론트엔드 README](https://github.com/shpark0913/final_pjt_movie/tree/master/final-pjt-front)

- [백엔드 README](https://github.com/shpark0913/final_pjt_movie/tree/master/final-pjt-back)

### 

## 0일차(221115)

#### 기획 단계

- **추천 알고리즘** 브레인스토밍
  
  - 선호하는 배우/감독의 작품 추천
  
  - 회원가입 후 좋았던 영화/장르 선택
  
  - 리뷰를 작성할 때 별점이 높았던 영화와 비슷한 영화 추천
  
  - 등등등...

- **커뮤니티** 관련
  
  - 별점으로 평점을 매길지 단순히 좋아요/싫어요만 구현할지 -> 별점으로 결정
  
  - 커뮤니티
    
    - 커뮤니티에는 모든 영화에 대한 리뷰가 보인다.
    
    - 특정 영화 페이지에서는 그 영화에 대한 리뷰만 보이도록.
    
    - 댓글 기능 추가 논의 예정

- API 관련
  
  - TMDB의 데이터...

#### 우선순위

1. 영화 Model - TMDB의 json 데이터 serializer 제작, DB에 저장하기

2. 로그인/회원가입/탈퇴 구현하기

3. 영화 DB를 axios로 받아와 Detail view 만들기

4. User 모델

5. 커뮤니티 CRUD 제작

6. 추천 알고리즘 -> User database에 좋아요 한 영화 저장하기.........

7. 댓글..좋아요 팔로잉 등 구현...

### 

## 1일차(221116)

#### Git 협의사항

- 매일 9시에 master branch `git pull` 받기

- 각자 branch로 switch, `git switch Frontend` , `git switch Backend`

- **BE 담당** : `final-pjt-back` 만 수정
  
  **FE 담당** : `final-pjt-front` 만 수정

- 기능을 완성할 때마다 push할 것
  
  : `git push origin Frontend` , `git push origin Backend`

- commit message 형식 : `[월일(1116)]_[적용사항]`

- 오후 6시
  
  1. 각자의 branch에서 push
     
     `git push origin Frontend` , `git push origin Backend`
  
  2. master 브랜치로 이동 `git switch master`
  
  3. `git pull`
  
  4. 브랜치 merge하기
     
     `git merge Frontend` , `git merge Backend`
  
  5. `git push`

### 

## 2일차(221117)

#### BE

- json 파일 DB에 저장하기

- fixtures 생성하기

- serializer 제작

#### FE

- vue component 구조

- router , vuex 정리

- authentication 관련 정리

### 

## 3일차(221118)

#### BE

- ERD 완성

- 추가 데이터 ( ... )

- 커뮤니티 앱
  
  - User 모델 custom

#### FE

- Movie Detail Page 완성

- 로그인/회원가입 오류 시 에러메시지 띄우기

- 로그아웃 - sessionstorage에서 토큰 삭제

- 로그인 로직 수정 - token을 세션 스토리지에서만 관리...

### 

## 4일차(221119)

#### BE

- Review model의 field 중 vote_average 속성 변경

#### FE

- 

## 5일차(221120)

#### BE

- FE와 중간 점검 및 방향 협의

#### FE

- BE와 중간 점검 및 방향 협의

### 

## 6일차(221121)

#### BE

- Username을 이용해 User의 pk를 조회할 수 있는 함수 만들기

- review component에 작성한 user의 pk가 조회되는데, 이를 username 으로 바꾸기

- movie detail 페이지에서 pk로 조회되는 장르를 genre name으로 조회하기

- movie의 pk를 이용해서 TMDB에서 추천 영화 불러오기

- 특정 user가 좋아한 영화와 싫어한 영화 조회하기

- 특정 user가 작성한 댓글들 조회하기

#### FE

- vue 로직 정리

- update review 하기

- user name 받아오기

- 404 NOT FOUND → router.replace 이용하면 뒤로가기 가능

- flex로 레이아웃 배치하기

- mypage 구성

### 

## 7일차(221122)

#### BE

- mypage에서 user가 작성한 review 조회하는 코드 수정

- user가 좋아하는 영화의 장르 비율 계산하기

#### FE

- mypage 꾸미기

- 내비게이션 가드 공부하고 다시 적용하기
