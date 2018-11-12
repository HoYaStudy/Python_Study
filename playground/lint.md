# Lint

## Pylint

코드 품질을 점수로 나타내준다.

```sh
$ pip3 install pylint
$ pylint test.py
```

## Pyflakes

코드의 에러를 체크해준다.

에러가 없다면 아무런 메세지도 출력되지 않는다.

```sh
$ pip3 install pyflakes
$ pyflakes test.py
```

## AutoPEP8

자동으로 PEP8 형식으로 변환해준다.

```
$ pip3 install autopep8
$ autopep8 --in-place --aggressive test.py
```

## PEP8

PEP8 convention을 얼마나 잘 따르는 지 점검해주는 style guide checker이다.

에러가 없다면 아무런 메세지도 출력되지 않는다.

```
$ pip3 install pep8
$ pep8 test.py
```

## Reference

* [pylint](https://www.pylint.org)
* [pyflakes](https://pypi.python.org/pypi/pyflakes)
* [autopep8](https://pypi.org/project/autopep8)
* [pep8](https://pypi.org/pypi/pep8)
