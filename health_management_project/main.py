"""
프로젝트명: 건강관리 프로그램
파일명: main.py
설명: 건강관리 프로그램의 실행 및 모듈 연결
"""

from modules.health_db import HealthDB
from modules.health_logic import HealthManager

db = HealthDB()

print(hasattr(db, "save_json"))

def main():

    print("=" * 40)
    print("       건강관리 프로그램")
    print("=" * 40)

    # 건강정보 관리 객체 생성
    db = HealthDB()
    manager = HealthManager()
    
    # 환자 정보 등록
    db.add_health("김기범", 2007, "남", 176, 70, 23.4, "과체중")
    db.add_health("최민호", 2001, "남", 172, 79, 26.40, "비만")

     # HealthManager에도 환자 정보 등록
    manager.add_health(db.health_list[0])
    manager.add_health(db.health_list[1])

     # 건강정보 통계 확인
    print("\n[건강정보 통계]")

    stats = manager.get_statistics()

    if stats is not None:
        print("전체 환자 수:", stats["total"])
        print("평균 키:", stats["avg_height"])
        print("평균 몸무게:", stats["avg_weight"])
        print("평균 BMI:", stats["avg_bmi"])
        print("키 표준편차:", stats["std_height"])
        print("몸무게 표준편차:", stats["std_weight"])
        print("BMI 표준편차:", stats["std_bmi"])

     # 환자 번호로 검색
    print("\n[환자 번호 검색]")

    result = manager.find_health(1)

    if  result is not None:
        print(result.to_dict())
    else:
          print("환자 정보를 찾을 수 없습니다.")

    # 이름으로 검색
    print("\n[이름으로 검색]")

    results = manager.find_health_by_name("김기범")

    for health in results:
        print(health.to_dict())

    # BMI 범위로 검색
    print("\n[BMI 범위로 검색]")

    result = manager.find_health_by_bmi(23, 27)

    for health_data in result:
        print(health_data.to_dict())

    # 건강정보 수정 테스트
    print("\n[건강정보 수정]")

    result = manager.update_health(1, weight=80)

    if result:
        health_data = manager.find_health(1)
        print(health_data.to_dict())
    else:
         print("환자 정보를 찾을 수 없습니다.")

    # 건강정보 삭제 테스트
    print("\n[건강정보 삭제]")

    result = manager.delete_health(2)

    if result:
        print("환자 정보 삭제 완료!")
    else:
        print("환자 정보를 찾을 수 없습니다.")

    print("\n[삭제 후 환자 목록]")
    for health_data in manager.get_all_health():
        print(health_data.to_dict())

    # 중복 환자 등록 테스트
    print("\n[중복 환자 등록 테스트]")

    health_data = db.health_list[0]

    result = manager.add_health(health_data)

    if result:
        print("환자 등록 성공!")
    else:
         print("중복 환자입니다. 등록할 수 없습니다.")

    # 잘못된 입력값 테스트
    print("\n[입력값 검증 테스트]")

    health_data = db.health_list[0]

    health_data.height = 176

    result = manager.add_health(health_data)

    if result:
        print("환자 등록 성공!")
    else:
         print("잘못된 입력값입니다. 등록할 수 없습니다.")

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