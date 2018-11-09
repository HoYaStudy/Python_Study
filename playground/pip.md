# pip

`pip`는 파이썬의 패키지 관리를 도와주는 패키지 관리 시스템이다. 파이썬 2.x와 3.x가 함께 설치된 경우 버전의 구별을 위해 pip3과 같이 사용하기도 한다.

패키지가 설치되었는지 다음과 같이 확인해볼 수 있다.

> $ python3 -c 'import <package_name>'

### Install

패키지를 설치한다.

> $ pip3 install <package_names>
>
> $ pip3 install -r requirements.txt

### List

현재 환경에 설치된 모든 패키지를 확인한다.

> $ pip3 list

### Show

해당 패키지의 의존성을 확인한다.

> $ pip3 show <package_name>

### Freeze

현재 환경의 모든 패키지 의존성을 확인한다.

> $ pip3 freeze > requirements.txt
