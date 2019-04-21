# pyenv

Python의 version 관리를 도와주는 tool이다.

## Installation

```sh
# on MAC
$ brew install pyenv
```

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
