# Python_Obfuscator1-Deobfuscator
Python_Obfuscator1 https://github.com/TheHellTower/Python_Obfuscator1 - Deobfuscator

Simple Python deobfuscator for scripts obfuscated with **Python_Obfuscator1** by TheHellTower.

---

## Features

* Removes watermark and obfuscation template
* Reverses Base64 and ROT13 encoded sections
* Restores original Python source
* Saves output as `.unpacked.py`

---

## Requirements

* Python 3.x

---

## Usage

```
python PythonObfuscator-Deobfuscator.py obfuscated.py
```

Output:

```
obfuscated.unpacked.py
```

---

## Limitations

* Works only with Python_Obfuscator1 format
* Static unpacking only, no runtime decryption

---

