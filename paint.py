# 클래스 객체 임포트
from point import Point

def main():
    # bound_class_method()
    # test_unbound_class_method()
    test_other_method()

def bound_class_method():
    p = Point()
    p.set_x(10)
    p.set_y(10)
    p.show()

def test_unbound_class_method():
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    Point.show(p)

def test_other_method():
    print(Point.class_method())
    print(Point.static_method())

if __name__ == '__main__':
    main()
