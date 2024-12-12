'''
    Altspell  Lytspel plugin for altspell.
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

from altspell.plugin import PluginBase
from lytspel.conv import Converter


converter = Converter()

class Plugin(PluginBase):
    def convert_to_altspell(self, tradspell_text: str) -> str:
        return converter.convert_para(tradspell_text)

    def convert_to_tradspell(self, altspell_text: str) -> str:
        raise NotImplementedError
