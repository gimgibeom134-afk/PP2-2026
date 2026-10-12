# 작성자: 김기범
# 작성일: 2026-10-02
# 문제: 7번 문제
# 사람들의 연락처를 저장하는  PhoneBook 클래스를 작성해보자. PhoneBook 클래스는 딕셔너리를  이용하여서 연락처를 저장한다.


class PhoneBook:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        return (f"{self.name}\n"
                f"office phone: {self.office}\n"
                f"email address: {self.email}")

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email


def test_prob6():
    p1 = PhoneBook("Kim", office="1234567", email="kim@company.com")
    p2 = PhoneBook("Park", office="2345678")

    p2.setEmail("park@company.com")

    print(p1)
    print()
    print(p2)


if __name__ == "__main__":
    test_prob6()