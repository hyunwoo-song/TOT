# 02_WEB

##  1. 영화 추천 사이트 메인 페이지 기초 레이아웃을 구성

###  1. 영화 추천 사이트를 위한 레이아웃 구성

####  1. 필수사항(HTML)

```html
<!--DOCTYPE 은 html입니다.-->
<!DOCTYPE html>

<!--html 의 언어는 한국어(ko)입니다.-->
<html lang="ko">

<!--meta 태그에 인코딩 설정을 UTF-8로 설정 해주세요.-->
    <meta charset="UTF-8">
<!--meta 태그에 기본 viewport 설정을 해주세요. (width: device-width, initialscale:
1.0)-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--title 태그는 영화추천사이트 라고 설정 해주세요.-->
    <title>EPL추천사이트</title>
```

####  2. Navigation Bar

```html
<!--최상단에 위치해야합니다.-->
<!--Item List(예시 - Home/친구평점보러가기/Login)는 우측 정렬입니다.-->
<div class="collapse navbar-collapse nav justify-content-end" id="navbarNavAltMarkup">
<!--반응형으로 구성되어 일정 수준 이하에서는 item이 숨김 처리 됩니다.-->
<!--Sticky navigation bar-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
<!--Item List에서 Home을 제외한 것들은 아직 기능이 구현되어 있지 않으므로 클릭이 불
가능(disable)합니다.-->
        <a class="nav-item nav-link disabled" href="#">친구평점보러가기</a>
         <a class="nav-item nav-link disabled" href="#">Log in</a>

```

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <a class="navbar-brand" href="#"><img src="https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/42459287_1064642717037123_3190324548104880128_n.png?_nc_cat=104&_nc_ht=scontent-icn1-1.xx&oh=4df2d96f731e485f8fd625c379595722&oe=5CBDB044" width="30" height="30" class="d-inline-block align-top" alt="">
          EPL추천시스템</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse nav justify-content-end" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
            <a class="nav-item nav-link disabled" href="#">친구평점보러가기</a>
            <a class="nav-item nav-link disabled" href="#">Log in</a>
          </div>
        </div>
      </nav>
```

####  3. Header

```html
<!--높이는 350px , 너비는 브라우저 전체 영역입니다..-->
<!--이미지는 선택적으로 활용 가능하되 반드시 배경 이미지가 있어야 합니다.-->
<!--Header 영역의 수직/수평 가운데 정렬 위치에 h2 태그를 사용하여 작성 해주세요..-->
<!--Header 배경 이미지, 색상 필터 등은 자유롭게 해주세요.-->
<!--배경 이미지와 관련하여 (css 속성 background-* 를 활용해 보세요.).-->
```

```html
 <header id= header class="d-flex p-2 bd-highlight justify-content-center align-items-center">
        <h2 class= "font1 text-navy">
          꽃이지고야<br>
          봄인 줄 알았습니다....<br>
          주.....멘
        </h2>
      </header>
```

```css
header {
    height: 350px;
    background-image: url('http://img.visualdive.co.kr/story2016/2015/09/%EC%A0%9C%EB%AA%A9-%EC%97%86%EC%9D%8C-5.jpg');
    background-size: cover;
    background-position: center 620px;
}
```

####  4.  Footer

```html
<!--브라우저 최하단에 위치합니다. 옵션 중 선택 - 1) Sticky 2) 내용 최하단-->
<!--높이는 50px 이상, 너비는 브라우저 전체 영역입니다.-->
<!--왼쪽에는 본인의 이름 혹은 닉네임, 오른쪽에는 헤더로 올라가는 링크로 구성됩니다..-->
<!--Footer는 padding이 좌우로 3rem-->

```

```html
<footer class="page-footer font-small blue footer-expand-lg bg-light sticky-bottom">
          <div class="footer-copyright text-left py-3">
            <h2 class="font2 text-navy">
              Hyunwoo: 
              <a href="https://www.tottenhamhotspur.com/"> 
                spurs.com
              </a>
              <a href="#header">
                  <img class='max-small' style= 'float: right' src="https://scontent-lht6-1.cdninstagram.com/vp/81d5a5093b7399ecf4ea3fb77f396206/5CB7E417/t51.2885-15/e35/47584894_339038133598992_2936236274750750554_n.jpg?_nc_ht=scontent-lht6-1.cdninstagram.com&se=8&ig_cache_key=MTk1MDE5MDI2MTczMzE1NzIwNA%3D%3D.2">
              </a>
            </h2>
              
            
          </div>
        </footer>
```





## 2. 영화 추천 사이트를 위한 영화 리스트 구성

####  1. 레이아웃

```html
<!--영화 리스트는 container에 속합니다.-->
```

```html
<div class="container">
```

####  2. (필수) subtitle

```html
<!--subtitle 영역은 위 아래 margin이 3rem입니다.
글씨 부분은 h3 태그입니다.
밑줄은 너비가 70px이고, 색상은 자유롭게 해주세요..-->
```

#### 3. Card view

![1548398584054](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548398584054.png)

```html
    <div class="container">
        <div class = "row my-1 ">
          <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="card" >
              <img class="card-img-top" src="assets/liverpool.png" alt="..." height="250" width="250" data-target="#liverpool" data-toggle="modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
              aria-hidden="true">
              <div class="card-body">
                <h4 class="card-title">리버풀 <button type="button" class="btn btn-danger">1위</button></h4>
                <hr>
                <p class="card-text">경기장: 안필드</p>
                <a href="https://www.liverpoolfc.com/team/first-team" target= "_blank" class="btn btn-dark">선수단 보러가기</a>
              </div>
            </div>
          </div>
```





## 3. 영화 상세보기

![1548398639778](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548398639778.png)

![1548398646255](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548398646255.png)

```html
<div id="liverpool" class="modal fade" >
    <div class="modal-dialog modal-lg" role="document">


        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title w-100" id="myModalLabel">리버풀</h4>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
              <img src="assets/liv1.jpg" alt="..." height="250" width="450">
              <hr>
              <p>리그 순위: 1위</p>
                <P>경기장: 안필드 </P>
                <hr>
                <p>
                    리버풀 FC는 잉글랜드 머지사이드 주 리버풀을 연고지로 둔 프리미어 리그의 축구 					클럽이다. 또한, 영국 유일의 빅 이어 영구 소장 클럽[8]이자 UEFA 챔피언스 리그 					5회, 1부 리그 18회 우승을 차지한 잉글랜드 1부리그 역사상 최고의 명문 구단이기						도 하다
                </p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary btn-lg" data-							dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary btn-lg">Save changes</button>
          </div>
        </div>
      </div>
</div>
```

