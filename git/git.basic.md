# Git & Github

## Git에 내 정보 설정

* `git config --global user.name 'Minsu Seo'`
* `git config --global user.email 'tjalstn10@gmail.com'`
* `git config --global --list`: 유저 설정 보기

# Git repo를 처음 생성한 경우

* `git init`: git 초기화. 지금 폴더를 git으로 관리하겠다! 
  (관리하려는 폴더 안에서 입력)
* `git remote add origin url주소` : 원격 저장소(remote repository) 주소(URL) 등록
  * `git remote set-url origin url주소`: 원격 저장소 URL 수정

## Git repo clone한 경우

* `git clone https://github.com/blossomwill/TIL.git`: 주소로부터 내용 내려받기
  * git clone을 하면 git 폴더로 설정되어`git init` 할 필요 없다.
  * `git remote add origin url주소`도  이 url로 받아왔기 때문에 할 필요없다.

## Git Commit & Push

* `git status`: 현재 폴더의 git의 상태 확인
* `git add .`: 현재 폴더의 변경사항들을 commit하기 위해서 준비. `.` 대신에 특정 파일 이름도 가능.
* `git commit -m 'D04 | 190107 AM | Git & CLI'`: commit, 변경 사항 저장, ' '안에 commit 설명

- `git push -u origin master`: remote로 등록된 원격저장소(remote repository)에  commit한 것들 올리기
  - 이후에는 `git push`만 입력해도 동작합니다. `git clone`을 한 경우에도 해당합니다.
  - 이 컴퓨터에서 최초 push인 경우, 로그인 창이뜨며 로그인을 해줍니다.
- `git log`: 커밋 기록 보기

## Git Pull

- `git pull`: GitHub에 올라가 있는 내용들, 즉 commit들을 내려받는 것.
- 아침에 오자마자 `git pull` 한번 하고 시작합시다!

## Git & GitHub 재설정

```bash
# Git 이름, 이메일 재설정
git config --global user.name 'Minsu Seo'
git config --global user.email 'tjalstn10@gmail.com'

# GitHub 로그인 정보 초기화
$ git credential reject
protocol=https
host=github.com
(한줄은 그냥 공백, 엔터)

$ git push
```



## 자리이동 git 설정

1. `git clone 'url주소' '폴더이름'`

2. `git credential reject`

   `protocol=https`

   `host=github.com`
   host의 사용자를 

3. cd 폴더이동

4. `git remote add origin 주소` (clone 사용한 경우는 skip)

5. `git push` 로그인창 pop-up

   everything up-to-date

6. `git config --global --list`

7. `git config --global user.name 'Minsu Seo'`

8. `git config --global user.email 'tjalstn10@gmail.com'`

9. `git log`: commit작성했던 내용확인가능 , 나가기는 `q`



### 새로운  Repo 생성

---

0. github repo 생성

1. local로 생성한 폴더로 이동
2. `git init`
3. `git add .`
4. `git status` 확인
5. `git commit -m ""`
6. ` git remote add origin https://github.com/blossomwill/homeworkshop.git`
7. `git push -u origin master`



## Git lab

### git lab repo push

* `lab.ssafy.com` 

* new repository 생성
  * clone의 https 주소 복사

* `git remote set-url origin [주소] `

* `git push`

#### git 주소와 git lab 주소 둘 다 쓰기

* remote 주소 추가
  * `git remote add github [주소]`
  * `git push github master`: github로 master branch를 보내라
* `git push -u origin`을 했으므로 origin인 git lab은 `git push`로 하면된다.
