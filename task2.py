from task1 import Student


## 문제 2: 상속을 이용한 고등학생 클래스 만들기
class HighSchoolStudent(Student):
    def __init__(self, name, age, grade, school_name):
        # super()를 사용하여 부모 클래스의 __init__ 메서드를 호출하세요.
        # YOUR CODE HERE
        super().__init__(name, age, grade)
        self.school_name = school_name

    # study 메서드를 오버라이딩하여 고등학생에 맞는 메시지를 출력하세요.
    # YOUR CODE HERE
    def study(self, hours):
        super().study(hours)


# HighSchoolStudent 클래스의 객체를 생성하고 study 메서드를 호출해보세요.
# 이름 나이 학년 학교 = 철수 , 17 , 3 , 새싹고
# YOUR CODE HERE
HSstdnt = HighSchoolStudent("철수", 17, 3, "새싹고")
HSstdnt.study(4)
