"""
프로젝트명: 건강관리 프로그램
파일명: health_logic.py
설명: 핵심 비즈니스 규칙 및 CRUD
"""
import statistics

class HealthManager:

    def __init__(self):
        # 건강정보를 저장할 리스트
        self.health_list = []

    def get_all_health(self):
        # 전체 건강정보 반환
        return self.health_list

    def find_health(self, patient_id):
        # 환자 ID로 검색
        for health_data in self.health_list:
            if health_data.patient_id == patient_id:
                return health_data

        # 해당 ID가 없으면 None 반환
        return None

    def calculate_bmi(self, height, weight):
        # 키를 cm에서 m로 변환
        height_m = height / 100

        # BMI 계산
        bmi = weight / (height_m ** 2)

        # 소수점 둘째 자리까지 반환
        return round(bmi, 2)

    def check_obesity(self, bmi):
        # BMI에 따른 비만도 판정
        if bmi < 18.5:
            return "저체중"
        elif bmi < 23:
            return "정상"
        elif bmi < 25:
            return "과체중"
        else:
            return "비만"

    def update_health(self, patient_id, height=None, weight=None):
        # 수정할 환자 검색
        health_data = self.find_health(patient_id)

        # 환자가 없으면 수정 실패
        if health_data is None:
            return False

        # 키 수정
        if height is not None:
            health_data.height = height

        # 몸무게 수정
        if weight is not None:
            health_data.weight = weight

        # BMI 자동 계산
        health_data.bmi = self.calculate_bmi(
            health_data.height,
            health_data.weight
        )

        # 비만도 자동 판정
        health_data.obesity_status = self.check_obesity(
            health_data.bmi
        )

        return True

    def delete_health(self, patient_id):
        # 삭제할 환자 검색
        health_data = self.find_health(patient_id)

        # 환자가 없으면 삭제 실패
        if health_data is None:
            return False

        # 환자 정보 삭제
        self.health_list.remove(health_data)

        return True

    def check_duplicate(self, name, birth_year, gender):
        # 기존 환자 정보 확인
        for health_data in self.health_list:

            # 이름, 출생 연도, 성별이 모두 같은지 확인
            if (health_data.name == name and
                health_data.birth_year == birth_year and
                health_data.gender == gender):

                return True

        # 중복 정보가 없으면 False 반환
        return False

    def validate_health(self, name, birth_year, height, weight):
        # 이름 확인
        if not name:
            return False

        # 출생 연도 확인
        if birth_year <= 0:
            return False

        # 키 확인
        if height <= 0:
            return False

        # 몸무게 확인
        if weight <= 0:
            return False

        return True

    def add_health(self, health_data):
        # 입력값 검증
        if not self.validate_health(
            health_data.name,
            health_data.birth_year,
            health_data.height,
            health_data.weight
        ):
            return False

        # 중복 환자 확인
        if self.check_duplicate(
            health_data.name,
            health_data.birth_year,
            health_data.gender
        ):
            return False

          # BMI 자동 계산
        health_data.bmi = self.calculate_bmi(
            health_data.height,
            health_data.weight
        )

        # 비만도 자동 판정
        health_data.obesity_status = self.check_obesity(
            health_data.bmi
        )

        # 건강정보 추가
        self.health_list.append(health_data)

        return True

    def find_health_by_name(self, name):
        # 검색 결과를 저장할 리스트
        result = []

        # 전체 환자 정보 확인
        for health_data in self.health_list:
            if name in health_data.name:
                result.append(health_data)

        return result

    def find_health_by_bmi(self, min_bmi=None, max_bmi=None):
        result = []

        for health_data in self.health_list:
            if min_bmi is not None and health_data.bmi < min_bmi:
                continue

            if max_bmi is not None and health_data.bmi > max_bmi:
                continue

            result.append(health_data)

        return result

    def get_statistics(self):
        # 전체 환자 정보 가져오기
        total = len(self.health_list)

        # 등록된 환자가 없으면 빈 결과 반환
        if total == 0:
            return None

        # 키, 몸무게, BMI 데이터 추출
        heights = [data.height for data in self.health_list]
        weights = [data.weight for data in self.health_list]
        bmis = [data.bmi for data in self.health_list]

        # 통계 결과 반환
        return {
            "total": total,
            "avg_height": round(statistics.mean(heights), 2),
            "avg_weight": round(statistics.mean(weights), 2),
            "avg_bmi": round(statistics.mean(bmis), 2),
            "std_height": round(statistics.stdev(heights), 2) if total >= 2 else 0,
            "std_weight": round(statistics.stdev(weights), 2) if total >= 2 else 0,
            "std_bmi": round(statistics.stdev(bmis), 2) if total >= 2 else 0
        }






