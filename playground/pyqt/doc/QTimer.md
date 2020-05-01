# QTimer

The `QTimer` class provides repetitive and single-shot timers.

The `QTimer` class provides a high-level programming interface for timers.

To use it, create a `QTimer`, connect its `timeout()` signal to the appropriate slots, and call `start()`. From then on, it will emit the `timeout()` signal at constant intervals.

You can set a timer to time out only once by calling `setSingleShot(true)`. You can also use the static `singleShot()` function to call a slot after a specified interval.

## Reference

* https://doc.qt.io/qtforpython/PySide2/QtCore/QTimer.html
