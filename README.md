# wechat_say

A simple demo of the following librarys/features:

- [Telegram Bots](https://core.telegram.org/bots)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Python Pillow](https://python-pillow.org/)

How to use:

1. Create a bot on Telegram([instructions](https://core.telegram.org/bots#3-how-do-i-create-a-bot)) and get your token.
2. Replace your token with '\<token\>' in the source code of [tg_bot.py](https://github.com/bb7133/wechat_say/blob/main/tg_bot.py#L15).
3. Run 'python tg_bot.py' to start the service for your bot(you may need to 'get over the wall').

TODO(Current limitations):

- Add configuration files.
- Make avatar and user name of WeChat configurable.
- Support very-short and multi-line sentences.
