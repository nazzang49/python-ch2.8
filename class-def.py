class MyString:
    pass

s = MyString()
print(type(s))
# 부모
print(MyString.__bases__)

s2 = str()
print(type(s2))
# 부모
print(str.__bases__)