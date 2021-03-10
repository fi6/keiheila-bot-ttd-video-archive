from khl import Bot, Cert
from configs import auth
import logging
cert = Cert(client_id=auth.khl_client,
            client_secret=auth.khl_secret,
            token=auth.khl_token)

bot = Bot(cmd_prefix=['.', '。'], cert=cert)


async def async_logging(x):
    try:
        logging.info(x)
    except Exception as e:
        logging.exception(e)


bot.on_raw_event(async_logging)

logging.debug('bot on raw event success')