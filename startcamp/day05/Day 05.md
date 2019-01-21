#  Day 05

## Telegram을 이용해 chat_bot 만들기

botfather 검색

/start

/newbot  입력

name_bot : name은 설정하고자 하는 이름



757804762:AAHU-P4GRV3DNSRWOuOmG4ns3O2NUZizM8g : 자신의 토큰

토큰: HTTP API에 access 하기 위한 고유 번호



### Making requests

https://api.telegram.org/bot<token>/METHOD_NAME :를통해 ID확인

https://api.telegram.org/bot<token>/getUpdate : 토큰에 입력



"from": {
​          "id": 687974136,

```html
https://api.telegram.org/bot757804762:AAHU-P4GRV3DNSRWOuOmG4ns3O2NUZizM8g/sendMessage?chat_id=687974136&text=%ED%95%98%EC%9C%84


```

sendMessage?chat_id=687974136&text=하위



## python으로 실행하기



###  send_message.py

```python
import os
import requests


token = os.getenv('TELEGRAM_BOT_TOKEN') 
chat_id = os.getenv('CHAT_ID') 
text = '하위'
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
```



### .bash_profile

```python

```



code ~/.bash_profile

source ~/.bash_profile

printenv







### hello.py



```python
@app.route('/write')
def write():
    return render_template('write.html')
```



#### write.html

```python
<h1>메시지 작성</h1>

<form action="/send">
    <input type="text" name="message">
    <input type="submit">
</form>

```



```python
import os

@app.route('/send')
def send():
    token = os.getenv('TELEGRAM_BOT_TOKEN') 
    chat_id = os.getenv('CHAT_ID') 
    text = request.args['message']
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')    
    
```



####  send.html

```python
<h1>전송 완료!</h1>

<a href="/write">돌아가기</a>

```

