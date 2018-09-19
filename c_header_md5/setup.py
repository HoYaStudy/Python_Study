from cx_Freeze import setup, Executable

executables = [
    Executable('c_header_md5.py')
]

setup(
    name="c_header_md5",
    version="1.0",
    description="Add MD5 hash to header file",
    executables=executables
)
