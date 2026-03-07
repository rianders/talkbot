#!/usr/bin/env python3
"""Check DNS and HTTPS reachability for TalkBot dependencies."""

from __future__ import annotations

import argparse
import socket
import subprocess
import sys
import urllib.request


DEFAULT_HOSTS = [
    "huggingface.co",
    "pypi.org",
    "openrouter.ai",
]

DEFAULT_URLS = [
    "https://huggingface.co",
    "https://pypi.org/simple/",
    "https://openrouter.ai/api/v1/models",
]


def _run(cmd: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except Exception as exc:
        return 1, str(exc)
    output = (p.stdout or "") + (p.stderr or "")
    return p.returncode, output.strip()


def _check_getent(host: str) -> bool:
    code, out = _run(["getent", "hosts", host])
    if code == 0 and out:
        print(f"[OK] getent {host}: {out.splitlines()[0]}")
        return True
    print(f"[FAIL] getent {host}: {out or 'no result'}")
    return False


def _check_socket(host: str) -> bool:
    try:
        ip = socket.gethostbyname(host)
    except Exception as exc:
        print(f"[FAIL] socket {host}: {exc}")
        return False
    print(f"[OK] socket {host}: {ip}")
    return True


def _check_curl(url: str, timeout_s: int) -> bool:
    code, out = _run(
        ["curl", "-I", "--max-time", str(timeout_s), "-sS", url]
    )
    if code == 0:
        first = next((ln for ln in out.splitlines() if ln.strip()), "(no headers)")
        print(f"[OK] curl {url}: {first}")
        return True
    print(f"[FAIL] curl {url}: {out or f'exit {code}'}")
    return False


def _check_urllib(url: str, timeout_s: int) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=timeout_s) as resp:
            print(f"[OK] urllib {url}: HTTP {resp.status}")
            return True
    except Exception as exc:
        print(f"[FAIL] urllib {url}: {exc}")
        return False


def _print_dns_config() -> None:
    print("\n=== DNS Config ===")
    code, out = _run(["resolvectl", "status"])
    if code == 0 and out:
        lines = out.splitlines()[:120]
        print("\n".join(lines))
    else:
        print("resolvectl unavailable or failed")
    code, out = _run(["cat", "/etc/resolv.conf"])
    if code == 0 and out:
        print("\n/etc/resolv.conf")
        print(out)
    else:
        print("\n/etc/resolv.conf unavailable")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", action="append", default=[], help="Host to test (repeatable)")
    parser.add_argument("--url", action="append", default=[], help="URL to test (repeatable)")
    parser.add_argument("--timeout", type=int, default=15, help="HTTP timeout seconds")
    parser.add_argument("--no-dns-config", action="store_true", help="Skip DNS config dump")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    hosts = args.host or DEFAULT_HOSTS
    urls = args.url or DEFAULT_URLS

    print("=== DNS Checks ===")
    dns_ok = True
    for host in hosts:
        dns_ok = _check_getent(host) and dns_ok
    for host in hosts:
        dns_ok = _check_socket(host) and dns_ok

    print("\n=== HTTPS Checks ===")
    https_ok = True
    for url in urls:
        https_ok = _check_curl(url, args.timeout) and https_ok
    for url in urls:
        https_ok = _check_urllib(url, args.timeout) and https_ok

    if not args.no_dns_config:
        _print_dns_config()

    print("\n=== Summary ===")
    print(f"DNS:   {'PASS' if dns_ok else 'FAIL'}")
    print(f"HTTPS: {'PASS' if https_ok else 'FAIL'}")
    overall = dns_ok and https_ok
    print(f"Overall: {'PASS' if overall else 'FAIL'}")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
