import typing_extensions

from xkcd_python_sdk.apis.tags import TagValues
from xkcd_python_sdk.apis.tags.info_api import InfoApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.INFO: InfoApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.INFO: InfoApi,
    }
)
