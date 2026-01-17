import os
import certifi

os.environ.pop("SSL_CERT_FILE", None)
os.environ["SSL_CERT_FILE"] = certifi.where()

import asyncio
from googletrans import Translator


class GoogleTranslator:
    def __init__(self):
        self.translator = Translator()

    async def convert(self, text, src_language, dest_language):
        translated = await self.translator.translate(
            text, src="ja", dest="en"
        )
        return translated.text


async def main():
    trans = GoogleTranslator()
    result = await trans.convert("私の名前は佐藤です.", "日本語", "英語")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
