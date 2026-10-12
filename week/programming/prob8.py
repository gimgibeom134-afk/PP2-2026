# 작성자: 김기범
# 작성일: 2026-10-02
# 문제: 8번 문제
# printSong이라는 클래스를 작성해보자. printSong의 생성자는 노래의 가사를 리스트 형태로 받아서 객체의 내부에 저장한다.


class printSong:
    def __init__(self, song):
        self.song = song

    def sing(self):
        print(self.song)


def test_prob8():
    aSong = printSong(
        "TWINKLE, twinkle, little star,\n"
        "How I wonder what you are!\n"
        "Up above the world so high,\n"
        "Like a diamond in the sky."
    )

    aSong.sing()


if __name__ == "__main__":
    test_prob8()