# 작성자: 김기범
# 작성일: 2026-10-02
# 문제: 4번 문제
# 사각형을 나타내는 Rectangle 클래스를 작성하여 보자, Rectangle 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"({self.x}, {self.y}, {self.width}, {self.height})"

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if (self.x < r.x + r.width and
                self.x + self.width > r.x and
                self.y < r.y + r.height and
                self.y + self.height > r.y):
            return True
        else:
            return False


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")


if __name__ == "__main__":
    test_prob4()