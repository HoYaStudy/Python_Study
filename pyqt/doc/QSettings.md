# QSettings

The QSettings class provides persistent platform-independent application settings.

## Basic Usage

```python
settings = QSettings("Organization", "Application")

# Save
settings.setValue("key", value)

# Load
if settings.contains("key"):
    value = settings.value("key"))
```

## Group

Grouping을 사용하여 설정들을 묶어서 관리할 수 있다.

### `beginGroup()`

```python
settings = QSettings("Organization", "Application")

# Save
settings.beginGroup("Group")
settings.setValue("key", value)
settings.endGroup()

# Load
settings.beginGroup("Group")
value = settings.value("key")
settings.endGroup()
```

### `beginWriteArray()` and `beginReadArray()`

```python
settings = QSettings("Organization", "Application")

# Save
settings.beginWriteArray("Array")
for i in range(size):
    settings.setArrayIndex(i)
    settings.setValue("key", value[i])
settings.endArray()

# Load
if settings.contains("Array/size"):
size = settings.beginReadArray("Array")
for i in range(size):
    settings.setArrayIndex(i)
    value[i] = settings.value("key"))
settings.endArray()
```

## Saved Location

### Unix System (Native Format)

1. $HOME/.config/Organization/Application.conf
    (Qt for Embedded Linux: $HOME/Settings/Organization/Application.conf)
2. $HOME/.config/Organization.conf
    (Qt for Embedded Linux: $HOME/Settings/Organization.conf)
3. for each directory \<dir> in $XDG_CONFIG_DIRS:
    \<dir>/Organization/Application.conf
4. for each directory \<dir> in $XDG_CONFIG_DIRS:
    \<dir>/Organization.conf

### MacOSX (Native Format)

1. $HOME/Library/Preferences/com.Organization.Application.plist
2. $HOME/Library/Preferences/com.Organization.plist
3. /Library/Preferences/com.Organization.Application.plist
4. /Library/Preferences/com.Organization.plist

### Windows (Native Format)

1. HKEY_CURRENT_USER\Software\Organization\Application
2. HKEY_CURRENT_USER\Software\Organization\OrganizationDefaults
3. HKEY_LOCAL_MACHINE\Software\Organization\Application
4. HKEY_LOCAL_MACHINE\Software\Organization\OrganizationDefaults

## Reference

* https://doc.qt.io/qtforpython/PySide2/QtCore/QSettings.html
