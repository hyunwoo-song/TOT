# 문제
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100,
}
# 1. 이 학생의 평균을 구하시오.
total_score = 0
for subject_score in score.values():
    total_score = total_score + subject_score
    
ave_score = total_score / len(score)
print(ave_score) 

# sum은 바로 사용할 수 없다. 내장함수로 다른기능으로 등록되어있기 때문이다.

# 1.2 두번째 풀이
total_score = sum(score.values()) # sum([80, 90, 100]) => 270
ave_score = total_score / len(score)
print(ave_score) 

