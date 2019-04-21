# pyenv

Python의 version 관리를 도와주는 tool이다.

## Installation

### on MAC
```sh
$ brew install pyenv
```

### on Windows

```sh
$ pip3 install pyenv-win --target $HOME/.pyenv
```

시스템 환경 변수에서 `PATH` 변수에 다음의 내용을 추가한다.

* ENVIRONMENT PATH :: My Computer -> properties -> Advanced system settings -> Advanced -> Environment Variables -> PATH
	+ %USERPROFILE%\.pyenv\pyenv-win\bin;%USERPROFILE%\.pyenv\pyenv-win\shims;

## Usage

### Show available list

```sh
$ pyenv install -l
```

### Install specific version

```sh
$ pyenv install \<version>
```

### Show installed list

```sh
$ pyenv versions
```

### 특정 folder에서만 특정 version을 사용

```sh
$ pyenv local \<version>
$ eval "$(pyenv init -)"
```
