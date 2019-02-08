class Score():
    def __init__(self, 국어, 영어, 수학):
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학

    def sum_score(self):
        return self.국어 + self.영어 + self.수학


국어, 영어, 수학 = map(int, input().split(','))
s = Score(국어, 영어, 수학)
print(f'국어, 영어, 수학의 총점:{s.sum_score()}')
