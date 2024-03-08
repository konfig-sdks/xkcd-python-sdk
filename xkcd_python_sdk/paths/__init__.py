# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from xkcd_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    INFO_0_JSON = "/info.0.json"
    COMIC_ID_INFO_0_JSON = "/{comicId}/info.0.json"
