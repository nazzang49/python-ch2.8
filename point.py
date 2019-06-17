# 클래스 객체(인스턴스 from 클래스 객체 = 인스턴스 객체)
class Point:
    # 클래스 멤버
    count_of_instance = 1000
    # self = this
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def show(self):
        print('점[{0}, {1}]'.format(self.get_x(), self.get_y()))

    @staticmethod
    def static_method():
        return 'static method called'

    @classmethod
    def class_method(cls):
        return cls.count_of_instance