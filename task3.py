# 2. 중급 문제
from task1 import Student


## 문제 3: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        return sum(self.scores) // len(self.scores)

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요.
        # YOUR CODE HERE
        study_score = hours  # 1시간당 1점
        self.add_score(study_score)


# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE
# Gstdnt = GradedStudent("영기", 24, 1)
# for _ in range(3):
#     score_now = int(input())
#     Gstdnt.study(score_now)
# avg = Gstdnt.calculate_average()
# print(f"평균 점수는 {avg}점입니다")
