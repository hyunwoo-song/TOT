# DAY02



### write_file

```python
with open('ssafy.txt','w',encoding='utf8') as f: 
# open은 close와 함께 써야하나 with를 쓰면 자동으로 close가 된다.
# 'w' : 작성할때, 'r' : 읽을때 'a' : 추가할때
# encoding='utf8': 파일이 깨지지않게 한글을 불러옴

    f.writelines(['1\n','2\n','3\n'])
    # for i in range(10):
       # f.write(f'This is SSAFY! {i}\n')
        # \t: tab, \\ : \문자 \'&\" :따옴표, 쌍따옴표 문자
```



### read_file

```python
with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()
    
    for line in lines:
        print(line.strip()) # strip() : 쓸때없는 공백란을 제거(개행문자)
    
```



## csv

###  write_csv

``` python
lunch = {
    '벌교꼬막비빔밥':'054-451-5484' ,
    '돌막창':'054-428-1152' ,
    '대패삼겹살':'054-887-4848'
}

import csv

with open('lunch.csv','w',encoding='utf8',newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items(): # 리스트 [(key, value), ...]
        csv_writer.writerow(item)
        
        # f.write(f'{item[0]},{item[1]}\n')
```



### read_csv

```python
import csv

with open('lunch.csv','r',encoding='utf8',) as f:
   # lines=f.readlines()
    items = csv.reader(f)
    for item in items:
        print(item)
```









