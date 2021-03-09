import os
from khl import Bot, Cert
from configs import auth
import logging
cert = Cert(client_id=auth.khl_client,
            client_secret=auth.khl_secret,
            token=auth.khl_token)

bot = Bot(cmd_prefix=['.', '。'], cert=cert)


async def async_logging(x):
    try:
        logging.info(x) if x.content == '1' else None
    except Exception as e:
        e


bot.on_text_msg(async_logging)