"""Retry a call a fixed number of times."""
from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(fn: Callable[[], T], times: int) -> T:
    if times < 1:
        raise ValueError("次数至少为 1")
    last: Exception | None = None
    for _ in range(times):
        try:
            return fn()
        except Exception as exc:
            last = exc
    assert last is not None
    raise last


def attempt_of(fn: Callable[[], T], times: int) -> tuple[T, int]:
    if times < 1:
        raise ValueError("次数至少为 1")
    last: Exception | None = None
    for n in range(1, times + 1):
        try:
            return fn(), n
        except Exception as exc:
            last = exc
    assert last is not None
    raise last


def try_retry(fn: Callable[[], T], times: int) -> tuple[bool, T | Exception]:
    try:
        return True, retry(fn, times)
    except Exception as exc:
        return False, exc
