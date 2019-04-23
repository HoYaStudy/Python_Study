# PyInstaller

## Installation

```sh
$ pip install pyinstaller
```

## Usage

실행 file로 만들기를 원하는 python file이 있는 folder로 이동한 후, 다음의 명령을 실행한다.

### With Console Window

```sh
$ pyinstaller <file.py>
```

`dist` folder로 이동한 후, 입력한 file 명으로 된 folder로 이동하면 실행 file이 생성되어 있다.

실행을 해보면 console 창과 함께 실행된다.

### Without Console Window

MAC과 Windows의 specific option이다.

```sh
$ pyinstaller -w <file.py>
$ pyinstaller --windowed <file.py>
```

### Create only 1 Executable File

```sh
$ pyinstaller -w -F <file.py>
$ pyinstaller --windowed --onefile <file.py>
```

만약, image file이 추가되어 있다면 생성된 `<file.exe>` 실행 file이 있는 folder에 같이 넣어준다.
