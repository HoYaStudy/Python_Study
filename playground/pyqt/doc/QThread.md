# QThread

The `QThread` class provides a platform-independent way to manage threads.

A `QThread` object manages one thread of control within the program.

`QThread` begins executing in `run()`. By default, `run()` starts the event loop by calling `exec()` and runs a Qt event loop inside the thread.

You can use worker objects by moving them to the thread using `moveToThread()`.

## Reference

* https://doc.qt.io/qtforpython/PySide2/QtCore/QThread.html
