from configs import auth
from pyyoutube import Api


class __Youtube():
    api = Api(api_key=auth.y2b_api_key)

    async def search_character(self, char: str):
        pass