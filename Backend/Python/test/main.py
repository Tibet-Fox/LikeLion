from abc import *
from code import Student
from code import StudentManagerService

# 메뉴 출력
def print_menu():
    print("====================")
    print("1. 학생 추가")
    print("2. 학생 출력")
    print("3. 전체 학생 조회")
    print("4. 학생 조회")
    print("5. 학생 제거")
    print("6. 학생 수정")
    print("7. 종료")
    print("====================")

# 학생 정보 출력
def print_student(student):
    print(f"학번: {student.getter_id()}, 이름: {student.getter_name()}, 나이: {student.getter_age()}, 전공: {student.getter_subject()}, 학점: {student.getter_grade()}")

# 학생 입력
def input_info():
    id = input("학번: ")
    name = input("이름: ")
    age = input("나이: ")
    subject = input("전공: ")
    grade = input("학점: ")

    return Student(id, name, age, subject, grade)

# main
def main(manager):
    while True:
        print_menu()
        choice = input("원하는 메뉴를 선택하세요: ")

        # 학생추가
        if choice == '1':
            student = input_info()
            manager.add_student(student)

        # 전체 학생 조회
        elif choice == '2':
            all_students = manager.list_student()
            for student in all_students:
                print_student(student)

        # 학생 검색
        elif choice == '3':
            id = input("검색할 학생의 학번을 입력하세요: ")
            student = manager.search_student(id)
            if student:
                print_student(student)
            else:
                print("학생을 찾을 수 없습니다.")
        # 학생 제거
        elif choice == '4':
            id = input("제거할 학생의 학번을 입력하세요: ")
            manager.delete_student(id)
            print("학생이 제거되었습니다.")
        # 학생 수정
        elif choice == '5':
            id = input("수정할 학생의 학번을 입력하세요: ")
            updated_student = input_info()
            manager.update_student(id, updated_student)
            print("학생 정보가 수정되었습니다.")
        # 종료
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    manager = StudentManagerService()
    main(manager)
