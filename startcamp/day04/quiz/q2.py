# 문제 2. 반 평균을 구하시오.

scores = {
            'a': {
                    '수학': 80,
                    '국어': 90,
                    '음악': 100,
                 },
            'b': {
                    '수학': 80,
                    '국어': 90,
                    '음악': 100,
                 }
         }

total_scores = 0 #=> 80 + 90 + 70
count = 0 #=> 1 + 1 + 1

for person_scores in scores.values(): #=> [{'수학': 80, '국어': 90, '음악': 100}, {'수학': 80, '국어': 90, '음악': 100}]
    person_scores #=>{'수학': 80, '국어': 90, '음악': 100}
    person_scores.values() # =>[80, 90, 70]
    for subject_scores in person_scores.values():
        # 3번째 시행
        # subject_scores #=> 70
        total_scores += subject_scores
        count += 1

avg_scores = total_scores/count   
print(avg_scores)







    
