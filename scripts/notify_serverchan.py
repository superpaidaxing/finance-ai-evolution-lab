#!/usr/bin/env python3
"""Send a ServerChan notification using SERVERCHAN_SENDKEY."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request


def send_serverchan(title: str, desp: str, short: str | None = None) -> dict:
    sendkey = os.environ.get("SERVERCHAN_SENDKEY")
    if not sendkey:
        raise RuntimeError("Missing SERVERCHAN_SENDKEY environment variable")

    data = {
        "title": title[:32],
        "desp": desp,
        "noip": "1",
    }
    if short:
        data["short"] = short[:64]

    request = urllib.request.Request(
        f"https://sctapi.ftqq.com/{sendkey}.send",
        data=urllib.parse.urlencode(data).encode("utf-8"),
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a ServerChan notification.")
    parser.add_argument("--title", required=True, help="Message title, max 32 chars")
    parser.add_argument("--desp", default="", help="Markdown message body")
    parser.add_argument("--short", default=None, help="Short card summary")
    args = parser.parse_args()

    result = send_serverchan(args.title, args.desp, args.short)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    errno = result.get("errno")
    if errno is None and isinstance(result.get("data"), dict):
        errno = result["data"].get("errno")
    code = result.get("code")
    if errno not in (None, 0) or code not in (None, 0):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
