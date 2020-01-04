# decorator

대상 함수의 위, 아래에 추가 구문들을 덧붙여 wrapping하고, 재사용성을 높여주는 것.

`first class function`과 `closure`를 사용하여 구현한다.

## Example

예로 다음의 함수를 보자.

```python
def function():
  print("Hello Decorator")
```

이 함수의 위, 아래에 다음과 같이 시간을 출력하고 싶다고 하자.

```python
import datetime

def function():
  print("Start: " + str(datetime.datetime.now()))
  print("Hello Decorator")
  print("End: " + str(datetime.datetime.now()))
```

이제 이 code에 `decorator`를 적용시키자.

```python
import datetime

def decorator_func(func):
  def decorated():
    print("Start: " + str(datetime.datetime.now()))
    func()
    print("End: " + str(datetime.datetime.now()))
  return decorated

@decorator_func
def function():
  print("Hello Decorator")
```

해당 기능이 필요한 함수가 많았다면 일일이 typing을 해야 했지만, 이렇게 `decorator`를 이용하면 간편하게 할 수 있다.

다음과 같이 함수의 형태 말고 class의 형태로도 가능하다.

```python
import datetime

class DecoratorClass:
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print("Start: " + str(datetime.datetime.now()))
    self.func(*args, **kwargs)
    print("End: " + str(datetime.datetime.now()))

class TestClass:
  @DecoratorClass
  def function():
    print("Hello Decorator")

test_cls = TestClass()
test_cls.function()
```
