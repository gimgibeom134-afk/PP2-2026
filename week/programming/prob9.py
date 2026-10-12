# 작성자: 김기범
# 작성일: 2026-10-06
# 문제: 9번 문제
# 터틀 그래픽에서 각각의 거북이는 객체이다. 2개의 거북이를 생성하여서 다음과 같이 서로 다른 방향으로 움직이도록 하자.


import turtle


def draw_turtle():
    lee = turtle.Turtle()
    kim = turtle.Turtle()

    lee.shape("turtle")
    kim.shape("turtle")

    lee.penup()
    lee.goto(-250, 100)
    lee.pendown()

    kim.penup()
    kim.goto(250, -100)
    kim.pendown()

    lee.forward(100)
    lee.right(90)
    lee.forward(100)
    lee.left(90)
    lee.forward(150)
    lee.right(90)
    lee.forward(100)

    kim.forward(100)
    kim.left(90)
    kim.forward(100)
    kim.right(90)
    kim.forward(150)
    kim.left(90)
    kim.forward(100)

    turtle.done()


def test_prob9():
    draw_turtle()


if __name__ == "__main__":
    test_prob9()