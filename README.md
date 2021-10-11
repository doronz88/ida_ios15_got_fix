# Description

Apple changed their MachO format once more so iOS 15.x executables cannot be reversed both using IDA and Ghidra. Until
the next version is released, we can use this simple IDAPython script to fix the broken `.got` entries.

Python 2:

```python
import urllib2; exec urllib2.urlopen('https://github.com/doronz88/ida_ios15_got_fix/raw/stable/fix_ios15_got.py').read()
```

Python 3:

```python
import urllib.request; exec(urllib.request.urlopen('https://github.com/doronz88/ida_ios15_got_fix/raw/stable/fix_ios15_got.py').read())
```

Thanks to @skochinsky for helping me figure out the bug and a quick workaround.
