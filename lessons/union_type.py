"""Union type gives flexability to single vars."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """info can be sre or int!"""
    if insinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int": {info}")


log("hello")
log(110)