class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
# 다 가능하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다
print(MyClass.instance_method(instance)) # ('instance method', <__main__.MyClass object at 0x000002D647ADEE20>)
print(MyClass.class_method()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method()) # static method


# 인스턴스가 할 수 있는 것
# 모두 호출되지만 인스턴스 메서드만 사용
print(instance.instance_method()) # ('instance method', <__main__.MyClass object at 0x0000019C7DD40CA0>)
print(instance.class_method()) # ('class method', <class '__main__.MyClass'>)
print(instance.static_method()) # static method