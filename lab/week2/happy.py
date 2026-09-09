#
# 생일 축하 함수
#
def say_happy_birthday(name:str) -> None:
    print("안녕하세요?")
    print(name+"님의 생일을 축하드립니다.")
    return None

def test_say_happy_birthday() :
    say_happy_birthday("기범")
    say_happy_birthday("태현")
    say_happy_birthday("민호")
    say_happy_birthday("재균")

def test_say_happy_birthday2() :
    names = ["기범", "태현", "민호", "재균"]
    for name in names:
        say_happy_birthday(name)

def test_say_happy_birthday3() :
    say_happy_birthday(3.141592)
    say_happy_birthday(100)
    say_happy_birthday(1, 2, 3)

if __name__ == "__main__":
#    test_say_happy_birthday1()
#    test_say_happy_birthday2()
     test_say_happy_birthday3()
