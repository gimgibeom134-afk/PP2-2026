# 작성자: 김기범
# 작성일: 2026-10-02
# 문제: 3번 문제
# 상ㅇ자를 나타내는 Box 클래스를 작성하여 보자, Box 클래스는 가로길이, 세로길이, 높이를 나타내는
# 인스턴스 변수를 가진다.


class Box:
    def __init__(self, length, height, depth):
        self.length = length
        self.height = height
        self.depth = depth

    def __str__(self):
        return f"({self.length}, {self.height}, {self.depth})"

    def getLength(self):
        return self.length

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth

    def setLength(self, length):
        self.length = length

    def setHeight(self, height):
        self.height = height

    def setDepth(self, depth):
        self.depth = depth

    def getVolume(self):
        return self.length * self.height * self.depth


def test_prob3():
    b1 = Box(100, 100, 100)

    print(b1)
    print("상자의 부피는", b1.getLength() * b1.getHeight() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()