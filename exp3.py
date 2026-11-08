# A1‑1 Thoroughbred良种马
class Thoroughbred:
    def __init__(self, mother: str, father: str, birthyear: int):
        self.__mother = mother
        self.__father = father
        self.__birthyear = birthyear

    def getCurrentAge(self) -> int:
        return 2026 - self.__birthyear

    def getFather(self) -> str:
        return self.__father

    def getMother(self) -> str:
        return self.__mother


# A1‑2 College、Building、Course
class Building:
    pass

class Course:
    pass

class College:
    def __init__(self):
        self.buildings: list[Building] = []   #聚合
        self.courses: list[Course] = []       #组合

    def add_building(self, b: Building):
        self.buildings.append(b)

    def add_course(self, c: Course):
        self.courses.append(c)


# A1‑3 School、Department、Instructor、Subject、Student
class Department:
    pass

class Instructor:
    pass

class Subject:
    pass

class Student:
    pass

class School:
    def __init__(self):
        self.departments: list[Department] = []
        self.students: list[Student] = []


# A1‑4 网上购物系统
from enum import Enum

class OrderStatus(Enum):
    CREATE = "CREATE"
    PAID = "PAID"
    SHIPPING = "SHIPPING"
    DELIVERED = "DELIVERED"
    CANCEL = "CANCEL"


class Customer:
    def __init__(self, name: str, contact: str, deliveryAddress: str, active: bool):
        self.__name = name
        self.__contact = contact
        self.__deliveryAddress = deliveryAddress
        self.__active = active


class Product:
    def __init__(self, title: str, weight: float, description: str):
        self.__title = title
        self.__weight = weight
        self.__description = description

    def getPriceForQuantity(self, qty: int) -> float:
        return 0.0

    def getWeight(self) -> float:
        return self.__weight


class OrderDetail:
    def __init__(self, quantity: int):
        self.__quantity = quantity

    def calculateSubTotal(self) -> float:
        return 0.0

    def calculateWeight(self) -> float:
        return 0.0


class Order:
    def __init__(self, createDate: str, status: OrderStatus):
        self.__createDate = createDate
        self.__status = status
        self.order_details: list[OrderDetail] = []


# Payment父类与5个子类
class Payment:
    pass

class Credit(Payment):
    def __init__(self, number: str, type: str, expireDate: str):
        self.__number = number
        self.__type = type
        self.__expireDate = expireDate

class Cash(Payment):
    def __init__(self, cashTendered: float):
        self.__cashTendered = cashTendered

class WireTransfer(Payment):
    def __init__(self, bankID: str, bankName: str):
        self.__bankID = bankID
        self.__bankName = bankName

class AliPay(Payment):
    def __init__(self, number: str):
        self.__number = number

class WeixinPay(Payment):
    def __init__(self, number: str):
        self.__number = number


#简单测试
if __name__ == "__main__":
    horse = Thoroughbred("母马A","公马B",2020)
    print(horse.getMother())
