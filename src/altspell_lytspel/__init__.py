'''
    Altspell-Lytspel  Lytspel plugin for altspell.
    Copyright (C) 2024  Nicholas Johnson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import threading
from lytspel.conv import Converter as FwdConverter
from altspell.plugin import PluginBase
from .reverse import Converter as RevConverter


class Plugin(PluginBase):
    def __init__(self):
        self._fwd_lock = threading.Lock()
        self._fwd_converter = FwdConverter()

        self._rev_lock = threading.Lock()
        self._rev_converter = RevConverter()

    def convert_to_altspell(self, tradspell_text: str) -> str:
        # use a lock to make the function thread-safe
        with self._fwd_lock:
            para = self._fwd_converter.convert_para(tradspell_text)

        return para

    def convert_to_tradspell(self, altspell_text: str) -> str:
        # use a lock to make the function thread-safe
        with self._rev_lock:
            para = self._rev_converter.convert_para(altspell_text)

        return para
