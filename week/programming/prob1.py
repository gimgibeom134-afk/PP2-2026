# 작성자: 김기범
# 작성일: 2026-10-02
# 문제: 1번 문제
# Cat 클래스를 만들고 이름과 나이를 인스턴스 변수로 저장한다.
# 생성자, 문자열 변환 함수, 접근자와 설정자 함수를 작성한다.


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


def test_prob1():
    missy = Cat("Missy", 3)
    lucky = Cat("Lucky", 5)

    print(missy)
    print(lucky)


if __name__ == "__main__":
    test_prob1()