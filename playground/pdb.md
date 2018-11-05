# The Python Debugger

Python debugger를 사용하려면 다음과 같이 `pdb` module을 포함하여 실행한다.

> $ python -m pdb xxx.py

Debugging 시에는 다음의 key를 사용한다.

* `c` : continue
* `s` : step (step into)
* `n` : next (step over)
* `l` : list
* `b` : break point
* `p` : print

Break point를 설정할 때는 다음과 같이 한다.

> `b 6` : line 6에 break point를 설정한다.
