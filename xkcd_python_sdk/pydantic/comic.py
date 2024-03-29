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
from pydantic import BaseModel, Field, RootModel


class Comic(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    alt: typing.Optional[str] = Field(None, alias='alt')

    day: typing.Optional[str] = Field(None, alias='day')

    img: typing.Optional[str] = Field(None, alias='img')

    link: typing.Optional[str] = Field(None, alias='link')

    month: typing.Optional[str] = Field(None, alias='month')

    news: typing.Optional[str] = Field(None, alias='news')

    num: typing.Optional[typing.Union[int, float]] = Field(None, alias='num')

    safe_title: typing.Optional[str] = Field(None, alias='safe_title')

    transcript: typing.Optional[str] = Field(None, alias='transcript')

    year: typing.Optional[str] = Field(None, alias='year')
    class Config:
        arbitrary_types_allowed = True
