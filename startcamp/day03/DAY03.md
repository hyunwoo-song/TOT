git clone 주소 :폴더만들기

## Bootstrap Template : 필요한 템플릿 제공 



git status

git add . 

git status

git commit -m "이름"

git status

git push





#<h1 class="mb-0">Clarence
​    수정

​    

드래그후 ctrl + D :같이수정 

alt + 클릭 : 커서 한개 더 생성









html 5: +tab  : 기본적인 뼈대가 나온다

#<title>HTML Practice</title>

style: 꾸미기

​	h1 : 주제

​	p: 내용

​	br: 띄우기	

​	ul: *

​	ol: 1. 2. 3.

​	div 구역을 나눈다

​	b: 굵게

​	i: 기울인 글꼴

ctrl + / :주석 작성 

추천사이트 w3school





``` html
 <title>HTML Practice</title>
        <style>
            h1, h3 {
                color: red;
            }
            h2 {
                color: green;
            }
            #green {
                color: yellowgreen; 
            }
            .yellow {
                color: yellow;
            }
        </style><body>
        <!-- 이것은 주석입니다. -->
        <h1>이것은 h1 태그입니다.</h1>
        <h2>이것은 h2 태그입니다.</h2>
        <h3>이것은 h3 태그입니다.</h3>
        <h4 id="green">이것은 h4 태그입니다.</h4>      
        <h5 class="yellow">이것은 h5 태그입니다.</h5>
        <h6 class="yellow">이것은 h6 태그입니다.</h6>

        <p style="color: pink;">         ------인라인이 최우선, id, class, 태그순
            이것은 p 태그입니다. <br>
            이것은 p 태그입니다. <br>
            이것은 p 태그입니다. <br>
            이것은 p 태그입니다. <br>
        </p>

        <ul>
            <li>리스트 1번째</li>
            <li>리스트 2번째</li>
            <li>리스트 3번째</li>
        </ul>

        <ol>
                <li>리스트 1번째</li>
                <li>리스트 2번째</li>
                <li>리스트 3번째</li>
        </ol>

        <div>
            <b>여기는 div입니다.</b>
            <i>여기는 div입니다.</i>
        </div>




    </body>
```







# flask

​        

pip install flask



from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

​    return "Hello World!"



FLASK_APP=hello.py flask run



@app.route("/greeting/<string:name>")

def greeting(name):

​    return f'반갑습니다! {name}님'



@app.route("/cube/<int:num>")

def cube(num):

​    cube = num**3 # == num * num * num

​    return cube

​    \# return f'{num}의 세제곱은 {cube}입니다.'

​        

@app.route("/lunch/<int:person>")    #주의할것은 외장함수 random을 사용하려면  import 필요

def lunch(person):

​    menu = ['햄버거', '곱창', '냉면', '갈비탕', '피자', '치킨', '삼겹살', '해물라면']

​    order = random.sample(menu, person)

​    return str(order)   



@app.route("/html")

def html():

​    multiline_string = '''

​    <h1> 이것은 h1 입니다. </h1>

    <p> 여기는 p 입니다. </p>

​    '''

​    return multiline_string







@app.route("/html_file")      # render_template 도 import

def html_flie():

​    return render_template('html_file.html')

<h1> 여기는 h1 입니다! </h1>

<p> 여기는 p 입니다. </p>





@app.route("/hi/<string:name>")

def hi(name):

​    return render_template('hi.html', name_in_html=name)

​        

<style>
    h1 {
        color: red;
    }
</style>

<h1>만나서 반갑습니다. {{ name_in_html }}님!</h1>

​    

@app.route("/fake_naver")

def f_n():

​    return render_template('fake_naver.html')   

<h1>Naver</h1>

<form action="https://search.naver.com/search.naver">

​    <input type="text" name="query">

​    <input type="submit">

</form>



