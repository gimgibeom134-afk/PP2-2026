"""
프로젝트명: 건강관리 프로그램
파일명: main.py
설명: 건강관리 프로그램의 실행 및 모듈 연결
"""

from modules.health_db import HealthDB

db = HealthDB()

print(hasattr(db, "save_json"))

def main():

    print("=" * 40)
    print("       건강관리 프로그램")
    print("=" * 40)

    # 건강정보 관리 객체 생성
    db = HealthDB()

    # 환자 정보 등록
    db.add_health("김기범", 2007, "남", 176, 70, 23.4, "과체중")
    db.add_health("최민호", 2001, "남", 172, 79, 26.40, "비만")

    # 등록된 환자 정보 확인
    print("\n[환자 정보 조회]")
    db.show_all()

    # JSON 파일 저장
    print("\n[JSON 저장]")
    db.save_json()

    # CSV 파일 저장
    print("\n[CSV 저장]")
    db.save_csv()

    # TXT 파일 저장
    print("\n[TXT 저장]")
    db.save_txt()

    # Pickle 파일 저장
    print("\n[Pickle 저장]")
    db.save_pickle()

    # 새로운 객체 생성 후 JSON 불러오기
    print("\n[JSON 불러오기]")
    db2 = HealthDB()
    db2.load_json()

    # CSV 파일 불러오기
    print("\n[CSV 불러오기]")
    db2.load_csv()

    # TXT 파일 불러오기
    print("\n[TXT 불러오기]")
    db2.load_txt()

    # Pickle 파일 불러오기
    print("\n[Pickle 불러오기]")
    db2.load_pickle()

    # 불러온 정보 확인
    print("\n[불러온 환자 정보]")
    db2.show_all()


if __name__ == "__main__":
    main()