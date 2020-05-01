# Python Types

## CPython

C로 짜여진 python이며 기본적으로 사용하는 python이다.

`GIL`때문에 multi-threading issue가 있다. 이를 피하기 위해, `Stackless Python`이 나왔다.

### GIL (Global Interpreter Lock)

극단적인 형태의 Coarse Grained Lock이다.

어떤 시점에서든 단 한개의 bytecode만이 실행된다.

## Cython

Python의 superset이다.

Python이 동적으로 결정되는 부분이 있어서 interpreting을 해야하기 때문에 느려서 이것을 정적으로 결정하기 위해 compile을 하는 방식으로 해결하려고 나왔다. 즉, 속도에 치명적인 부분만 compile하여 성능 개선을 이룬다는 아이디어로 나온 hybrid 방식이다. `Julia`, `Go`, `Scala` 등이 이런 hybrid 방식을 적용했다.

## PyPy

Python으로 작성된 Python interpreter이다. `JIT` 기술을 도입하여 `CPython`보다 빠르게 만들었다.

이것으로 인하여 `Stackless Python`이 죽었다.

### JIT (Just In Time) Compiler

Python bytecode를 interpreting하다가 자주 사용되는 부분을 compile한다. 따라서 초반에는 느리지만 코드가 실행되면서 점점 빨라진다.

## RPython

`PyPy`를 구현하기 위해 나왔다. `Restricted Python`이란 의미인데 정적 compile이 가능하도록 Python에 제약을 가한 subset이다. Compile에 방해가 되는 동적인 기능을 제거했다.

## Stackless Python

`CPython`을 구현할 때 Python의 함수 호출 stak을 C의 stack에 그대로 얹어 버렸기 때문에 Python에서 C stack을 다 채우면 stack overflow error가 발생한다. 또한, Python의 호출 stack을 `CPython` 스스로 제어할 수 없게되어 coroutine 등의 실행 흐름을 제어하는 기능을 사용할 수 없다는 문제가 있다.

이를 해결하기 위해 `CPython`에서 C stack을 사용하지 않고, 새로 호출 stack을 구현해서 만든 것이다.

## JPython

`Jython`의 조상으로 현재는 사용되지 않는다.

## Jython

`JVM`위에서 돌아가는 Python이다.

## IronPython

`.NET` framework위에서 돌아가는 Python이다.

## IPython

Python interpreter나 compiler가 아닌 추가 기능을 제공하는 interactive shell이다. 즉, Python 기본 interpreter의 upgrade version이라고 볼 수 있다.

### IPython Notebook

`IPython`의 기능 중 하나로 web 기반 shell 환경을 제공한다.
