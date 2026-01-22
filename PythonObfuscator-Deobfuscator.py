import re
import sys
import base64
import codecs

def rot13(s):
    return codecs.decode(s, "rot_13")

def unpack(code):
    p1 = re.search(r"magic\s*=\s*'([^']*)'", code)
    p2 = re.search(r"love\s*=\s*'([^']*)'", code)
    p3 = re.search(r"god\s*=\s*'([^']*)'", code)
    p4 = re.search(r"destiny\s*=\s*'([^']*)'", code)
    if not all([p1, p2, p3, p4]):
        return None
    data = p1.group(1) + rot13(p2.group(1)) + p3.group(1) + rot13(p4.group(1))
    return base64.b64decode(data).decode("utf-8", errors="ignore")

def main():
    if len(sys.argv) < 2:
        return
    with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
    res = unpack(code)
    if res is None:
        return
    out = sys.argv[1].replace(".py", ".unpacked.py")
    with open(out, "w", encoding="utf-8") as f:
        f.write(res)

if __name__ == "__main__":
    main()
