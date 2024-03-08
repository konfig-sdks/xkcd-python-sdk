import typing_extensions

from xkcd_python_sdk.paths import PathValues
from xkcd_python_sdk.apis.paths.info_0_json import Info0Json
from xkcd_python_sdk.apis.paths.comic_id_info_0_json import ComicIdInfo0Json

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.INFO_0_JSON: Info0Json,
        PathValues.COMIC_ID_INFO_0_JSON: ComicIdInfo0Json,
    }
)

path_to_api = PathToApi(
    {
        PathValues.INFO_0_JSON: Info0Json,
        PathValues.COMIC_ID_INFO_0_JSON: ComicIdInfo0Json,
    }
)
