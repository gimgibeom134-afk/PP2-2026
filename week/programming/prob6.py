# 작성자: 김기범
# 작성일: 2026-10-06
# 문제: 6번 문제
# Perseon 이라는 클래스를 작성해보자, person 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.
class Person:
    def __init__(self):
        self.contacts = {}

    def __str__(self):
        return str(self.contacts)

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "mobile": mobile,
            "office": office,
            "email": email
        }


def test_prob7():
    obj = Person()

    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")

    print(obj)


if __name__ == "__main__":
    test_prob7()