# coding: utf-8

"""
    XKCD

    Webcomic of romance, sarcasm, math, and language.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredComic(TypedDict):
    pass

class OptionalComic(TypedDict, total=False):
    title: str

    alt: str

    day: str

    img: str

    link: str

    month: str

    news: str

    num: typing.Union[int, float]

    safe_title: str

    transcript: str

    year: str

class Comic(RequiredComic, OptionalComic):
    pass
