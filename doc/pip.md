# pip

`pip`는 Python의 package 관리를 도와주는 package 관리 시스템이다. Python 2.x와 3.x가 함께 설치된 경우 version의 구별을 위해 `pip3`와 같이 사용하기도 한다.

Package가 설치되었는지 다음과 같이 확인해볼 수 있다.

```sh
$ python3 -c 'import <package_name>'
```

### Install

Package를 설치한다.

```sh
$ pip3 install <package_names>
```

특정 version의 package를 설치한다.

```sh
$ pip3 install <package_name==version>
```

최소 version의 package를 설치한다.

```sh
$ pip3 install 'package-name>=minimum_version'
```

* Single-quote는 shell에서 `>`기호가 redirection으로 동작하는 것을 방지한다.

File에 명시된 package를 설치한다.

```sh
$ pip3 install -r requirements.txt
```

### List

현재 환경에 설치된 모든 package를 확인한다.

```sh
$ pip3 list
```

### Show

해당 package의 의존성을 확인한다.

```sh
$ pip3 show <package_name>
```

### Freeze

현재 환경의 모든 package 의존성을 확인한다.

```sh
$ pip3 freeze > requirements.txt
```
