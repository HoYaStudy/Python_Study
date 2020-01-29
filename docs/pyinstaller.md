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

## Options

### General Options

* `-h`, `--help` : Show help message
* `-v`, `--version` : Show version information
* `--distpath DIR` : Where to put the bundled app
* `--workpath DIR` : Where to put all the temporary work files
* `-y`, `--noconfirm` : Replace output directory without asking for confirmation
* `--clean` : Clean cache and remove temporary files before building
* `--log-level LEVEL` : Amount of detail in build-time console messages
  + TRACE
  + DEBUG
  + INFO (*Default*)
  + WARN
  + ERROR
  + CRITICAL

### What to generate

* `-F`, `--onefile` : Create a one-file bundled executable
* `--specpath DIR` : Folder to store the generated spec file
* `-n NAME`, `--name NAME` : Name to assign to the bundled app and spec file

### Waht to bundle, where to search

* `--add-data <SRC;DEST or SRC:DEST>` : Additional non-binary files or folders to be added to the executable
* `--add-binary <SRC;DEST or SRC:DEST>` : Additional binary files to be added to the executables
* `-p DIR, --paths DIR` : A path to search for imports
* `--hidden-import MODULE` : Name an import not visible in the code of the script
* `--exclude-module MODULE` : Optional module or package that will be ignored

### Windows and Mac OS X specific options

* `-c`, `--console`, `--nowindowd` : Open a console window for standard i/o
* `-w`, `--windowed`, `--noconsole` : Windows and Mac OS X: Do not provide a console window for standard i/o
* `-i ICON`, `--icon ICON`
  + .ico : Apply that icon to a Windows executable
  + .icns : Apply the icon to the .app bundle on Mac OS X

### Windows specific options

* `--uac-admin` : Using this option creates a Manifest which will request elevation upon application restart

## References

* [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html)
