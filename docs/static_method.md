# Static Method

정적 method는 class에서 직접 접근할 수 있는 method이다. Python에서는 2가지 종류가 있다.

다음의 예를 보자. `class method`의 경우 첫 번째 인자로 class를 입력해야하고, `static method`의 경우 특별히 입력해야하는 것이 없다.

```python
class TestClass:
  def instance_method(self, a, b):
    return a + b

  @classmethod
  def class_method(cls, a, b):
    return a + b

  @staticmethod
  def static_method(a, b):
    return a + b
```

이제 instance를 생성하여 test를 해보자.

```python
test_cls = TestClass()
print(test_cls.instance_method(2, 3))
print(test_cls.class_method(2, 3))
print(test_cls.static_method(2, 3))
```

모든 함수가 instance를 통하여 호출할 수 있다.

이제 class를 통하여 바로 호출해보자.

```python
test_cls = TestClass()
# print(TestClass.instance_method(2, 3))  Error !!
print(TestClass.instance_method(test_cls, 2, 3))
print(TestClass.class_method(2, 3))
print(TestClass.static_method(2, 3))
```

instance method의 경우는 object를 인자로 주어야만 하지만, `class method`와 `static method`의 경우는 class로 직접 호출이 가능하다.

그렇다면, 이 둘의 차이점은 무엇일까? 바로 상속에서 드러난다!

```python
class ParentClass:
    test_variable = "Parent"

    def __init__(self):
        self.show = "Who am I? " + self.test_variable

    @classmethod
    def class_method(cls):
        return cls()

    @staticmethod
    def static_method():
        return ParentClass()

    def print_class(self):
        print(self.show)


class ChildClass(ParentClass):
    test_variable = "Child"


class_variable = ChildClass.class_method()
class_variable.print_class()
#> Child

static_variable = ChildClass.static_method()
static_variable.print_class()
#> Parent
```

`class method`의 경우 cls 인자를 통하여 class 속성을 가져오는 반면, `static method`의 경우 부모 class의 class 속성을 가져온다.
