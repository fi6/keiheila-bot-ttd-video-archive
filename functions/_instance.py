import os
from khl import Bot, Cert
from configs import auth
cert = Cert(client_id=auth.khl_client,
            client_secret=auth.khl_secret,
            token=auth.khl_token)

bot = Bot(cmd_prefix=['.', '。'], cert=cert)


