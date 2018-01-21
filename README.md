#Zyklus

A simple event loop for executing functions within the loop's thread.

## Usage

### Current thread

```python
from zyklus import Zyklus

def output(what):
    print(what)

zyklus = Zyklus()

zyklus.post(lambda: output(1))
zyklus.post(lambda: output(2))
zyklus.post(lambda: output(3))
zyklus.post_delayed(lambda: output(5), 1)
zyklus.post(lambda: output(4))
zyklus.post_delayed(zyklus.terminate, 1.1)

zyklus.loop()
output("done")
```
output:
```
1
2
3
4
5
done
```
### In background

```python
from zyklus import Zyklus
import threading

def output(what):
    print(what)

zyklus = Zyklus()
zyklusThread = threading.Thread(target=zyklus.loop)
zyklusThread.start()

zyklus.post(lambda: output(1))
zyklus.post(lambda: output(2))
zyklus.post(lambda: output(3))
zyklus.post_delayed(lambda: output(5), 1)
zyklus.post(lambda: output(4))
zyklus.post_delayed(zyklus.terminate, 1.5)

zyklusThread.join()
output("done")
```
output:
```
1
2
3
4
5
done
```

## Installation

```
pip install zyklus
```