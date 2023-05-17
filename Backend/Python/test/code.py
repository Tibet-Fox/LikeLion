from abc import *

class Student:
    def __init__(self, id, name, age, subject, grade):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__subject = subject
        self.__grade = grade

    def getter_id(self):
        return self.__id
    
    def getter_name(self):
        return self.__name
    
    def getter_age(self):
        return self.__age
    
    def getter_subject(self):
        return self.__subject
    
    def getter_grade(self):
        return self.__grade


class StudentManagerRepo:
    @abstractmethod
    def add_student(self, student): # 학생 추가
        pass

    @abstractmethod
    def list_student(self): # 전체 학생 조회
        pass

    @abstractmethod
    def search_student(self, name): # 학생 조회
        pass

    @abstractmethod
    def delete_student(self, name): # 학생 제거
        pass

    @abstractmethod
    def update_student(self, name, student): # 학생 수정
        pass

class StudentManagerImpl(StudentManagerRepo):
    def __init__(self):
        self.__students = {}

    def add_student(self, student):
        if student.getter_id() in self.__students:
            raise ValueError("이미 등록된 학번입니다.")
        self.__students[student.getter_id()] = student

    def list_student(self):
        return list(self.__students.values())

    def search_student(self, id):
        if id in self.__students:
            return self.__students[id]
        else:
            return None

    def delete_student(self, id):
        if id in self.__students:
            del self.__students[id]
        else:
            raise ValueError("해당 학번의 학생을 찾을 수 없습니다.")

    def update_student(self, id, updated_student):
        if id in self.__students:
            self.__students[id] = updated_student
        else:
            raise ValueError("해당 학번의 학생을 찾을 수 없습니다.")


class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentManagerImpl()

    def add_student(self, student): # 학생 추가
        self.__student_repo.add_student(student)

    def list_student(self): # 전체 학생 조회
        return self.__student_repo.list_student()

    def search_student(self, name): # 학생 조회
        return self.__student_repo.search_student(name)

    def delete_student(self, name): # 학생 제거
        self.__student_repo.delete_student(name)

    def update_student(self, name, student): # 학생 수정
        self.__student_repo.update_student(name, student)

