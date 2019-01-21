

```python
n=int(input())
m=int(input())
print(('*'*n +'\n')*m)
```

    5
    4
    *****
    *****
    *****
    *****


​    


```python
import math
student={'python':80,'algorithm':99, 'django':89,'flask':83}

avg=student.values()
print(sum(avg)/4)
```

    87.75



```python
blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
```


```python
count_a=0
count_b=0
count_ab=0
count_o=0
for i in blood_types:
    if i =='A':
        count_a+=1
    elif i=='B':
        count_b+=1
    elif i=='AB':
        count_ab+=1
    elif i=='O':
        count_o+=1

    
        
print(f'혈액형 A {count_a}명, 혈액형 B {count_b}명,혈액형 O {count_o}명,혈액형 AB {count_ab}명')
```

    혈액형 A 3명, 혈액형 B 3명,혈액형 O 3명,혈액형 AB 3명



```python

```


```python

```
