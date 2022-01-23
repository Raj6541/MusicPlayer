"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("8179798", None)
        self.API_HASH: str = os.environ.get("78a1bfb49887007ad2760a2394b063c4", None)
        self.SESSION: str = os.environ.get(
            "AQA9ilIMBB_Ib7cNUnMnqQcbtBxvK0IWH8JFZ9-7SgVJOqiP7GHnXmrO4DfdEsv1aQTu2-RgQOrtVAM_8gHMradTiRHQr9FGP3cKspBxvclc_68ISzxkHd9fazkWtP-6iUvNxaaEgmKL1HDxDewH95oGmvFN0P5SxpMtla2ClNIJIdwO3j2j--oRoyxavJODUV8FJEucAs4W3Z-aCqqNTEYH0jUV4YGTisYINKdfVOf9FmYb7gXspKlN4o82BYMSWSf3rs8L_XeodI2ntcXb7sOZ86eSxVs-feTiufqZqHIy20WIvlWfOb3wPWL45rIxys6-fHRYbdFH15dVBc9Mv0HLcAU0PAA",
            None,
        )
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("901527936", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.QUALITY: str = os.environ.get("low").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()


config = Config()
