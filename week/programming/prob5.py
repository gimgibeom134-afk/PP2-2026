# 작성자: 김기범
# 작성일: 2026-10-02
# 문제: 5번 문제
# 삼각형을 나타내는 클래스 Triangle을 작성해보자. 
# Triangle 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.


class Triangle:
    def __init__(self, a1, a2, a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3
        self.numberOfSides = 3

    def __str__(self):
        return f"{self.angle1}, {self.angle2}, {self.angle3}"

    def setAngle1(self, angle):
        self.angle1 = angle

    def getAngle1(self):
        return self.angle1

    def setAngle2(self, angle):
        self.angle2 = angle

    def getAngle2(self):
        return self.angle2

    def setAngle3(self, angle):
        self.angle3 = angle

    def getAngle3(self):
        return self.angle3

    def checkAngle(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngle())


if __name__ == "__main__":
    test_prob5()