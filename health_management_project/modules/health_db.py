"""
프로젝트명: 건강관리 프로그램
파일명: health_db.py
설명: 건강정보 데이터 관리 및 파일 저장
"""
import json
import csv
import pickle
import os

class HealthData:

    def __init__(self, patient_id, name, birth_year, gender,
                 height, weight, bmi, obesity_status):

        self.patient_id = patient_id
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.obesity_status = obesity_status

    def to_dict(self):
        """건강정보를 딕셔너리로 변환"""

        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "obesity_status": self.obesity_status
        }
    
# 건강정보 관리 클래스
class HealthDB:

    def __init__(self):
        self.health_list = []
        self.next_id = 1

    def add_health(self, name, birth_year, gender,
                   height, weight, bmi, obesity_status):

        # 환자 번호 자동 생성
        patient_id = self.next_id

        # 건강정보 객체 생성
        health = HealthData(
            patient_id, name, birth_year, gender,
            height, weight, bmi, obesity_status
        )

        # 리스트에 건강정보 추가
        self.health_list.append(health)

        # 다음 환자 번호 증가
        self.next_id += 1

        return health

    def show_all(self):

        # 등록된 건강정보가 없는 경우
        if not self.health_list:
            print("등록된 건강정보가 없습니다.")
            return

        # 등록된 건강정보 출력
        for health in self.health_list:
            print(health.to_dict())

    def find_health(self, patient_id):

        # 등록된 건강정보 검색
        for health in self.health_list:

            if health.patient_id == patient_id:
                return health

        # 해당 번호가 없는 경우
        return None

    def delete_health(self, patient_id):

        # 환자 정보 검색
        health = self.find_health(patient_id)

        # 해당 환자가 없는 경우
        if health is None:
            print("해당 환자 정보를 찾을 수 없습니다.")
            return False

        # 환자 정보 삭제
        self.health_list.remove(health)

        print("환자 정보가 삭제되었습니다.")
        return True
    
    def update_health(self, patient_id, weight):

        # 환자 정보 검색
        health = self.find_health(patient_id)

        # 환자가 없는 경우
        if health is None:
            print("해당 환자 정보를 찾을 수 없습니다.")
            return False

        # 몸무게 수정
        health.weight = weight

        print("환자 정보가 수정되었습니다.")
        return True

    def save_json(self):

        # 저장할 파일 경로
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.json"
        )

         # data 폴더가 없으면 자동 생성
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 건강정보를 딕셔너리로 변환
        data = [health.to_dict() for health in self.health_list]

        # JSON 파일 저장
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("JSON 파일 저장 완료!")

    def load_json(self):

        # 저장된 파일 경로
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.json"
        )

        try:
            # JSON 파일 읽기
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # 기존 건강정보 초기화
            self.health_list = []

            # 딕셔너리를 객체로 변환
            for item in data:
                health = HealthData(**item)
                self.health_list.append(health)

            # 다음 환자 번호 설정
            if self.health_list:
                self.next_id = max(
                    health.patient_id for health in self.health_list
                ) + 1
            else:
                self.next_id = 1

            print("JSON 파일 불러오기 완료!")

        except FileNotFoundError:
            print("저장된 JSON 파일이 없습니다.")

        except json.JSONDecodeError:
            print("JSON 파일의 형식이 올바르지 않습니다.")

    def save_csv(self):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.csv"
        )

         # data 폴더가 없으면 자동 생성
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 저장할 데이터 항목
        fieldnames = [
            "patient_id", "name", "birth_year", "gender",
            "height", "weight", "bmi", "obesity_status"
        ]

        # CSV 파일 저장
        with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for health in self.health_list:
                writer.writerow(health.to_dict())

        print("CSV 파일 저장 완료!")

    def load_csv(self):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.csv"
        )

        try:
            # CSV 파일 읽기
            with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)

                self.health_list = []

                for item in reader:
                    health = HealthData(
                        int(item["patient_id"]),
                        item["name"],
                        int(item["birth_year"]),
                        item["gender"],
                        float(item["height"]),
                        float(item["weight"]),
                        float(item["bmi"]),
                        item["obesity_status"]
                    )

                    self.health_list.append(health)

                # 다음 환자 번호 설정
                if self.health_list:
                    self.next_id = max(
                        health.patient_id for health in self.health_list
                    ) + 1
                else:
                    self.next_id = 1

            print("CSV 파일 불러오기 완료!")

        except FileNotFoundError:
            print("저장된 CSV 파일이 없습니다.")

        except (ValueError, KeyError, csv.Error):
            print("CSV 파일의 데이터 형식이 올바르지 않습니다.")

    def save_txt(self):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.txt"
        )

         # data 폴더가 없으면 자동 생성
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # TXT 파일 저장
        with open(file_path, "w", encoding="utf-8") as file:

            for health in self.health_list:
                data = health.to_dict()

                line = (
                    f"{data['patient_id']}|"
                    f"{data['name']}|"
                    f"{data['birth_year']}|"
                    f"{data['gender']}|"
                    f"{data['height']}|"
                    f"{data['weight']}|"
                    f"{data['bmi']}|"
                    f"{data['obesity_status']}\n"
                )

                file.write(line)

        print("TXT 파일 저장 완료!")

    def load_txt(self):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.txt"
        )

        try:
            self.health_list = []

            with open(file_path, "r", encoding="utf-8") as file:

                for line in file:
                    item = line.strip().split("|")

                    health = HealthData(
                        int(item[0]),
                        item[1],
                        int(item[2]),
                        item[3],
                        float(item[4]),
                        float(item[5]),
                        float(item[6]),
                        item[7]
                    )

                    self.health_list.append(health)

            if self.health_list:
                self.next_id = max(
                    health.patient_id for health in self.health_list
                ) + 1
            else:
                self.next_id = 1

            print("TXT 파일 불러오기 완료!")

        except FileNotFoundError:
            print("저장된 TXT 파일이 없습니다.")

        except (ValueError, IndexError):
            print("TXT 파일의 데이터 형식이 올바르지 않습니다.")

    def save_pickle(self):

        # 저장할 파일 경로
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.pkl"
        )

         # data 폴더가 없으면 자동 생성
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Pickle 파일 저장
        with open(file_path, "wb") as file:
            pickle.dump(self.health_list, file)

        print("Pickle 파일 저장 완료!")

    def load_pickle(self):

        # 저장된 파일 경로
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "health_data.pkl"
        )

        try:
            # Pickle 파일 불러오기
            with open(file_path, "rb") as file:
                self.health_list = pickle.load(file)

            # 다음 환자 번호 설정
            if self.health_list:
                self.next_id = max(
                    health.patient_id for health in self.health_list
                ) + 1
            else:
                self.next_id = 1

            print("Pickle 파일 불러오기 완료!")

        except FileNotFoundError:
            print("저장된 Pickle 파일이 없습니다.")

        except (pickle.UnpicklingError, EOFError):
            print("Pickle 파일을 읽을 수 없습니다.")
