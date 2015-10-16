# This file is part of JST.
#
# JST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with JST.  If not, see <http://www.gnu.org/licenses/>.

import sys


class Logger(object):
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    CRITICAL = 'CRITICAL'
    IMPLEMENT_ME = 'IMPLEMENT_ME'
    TOKEN = 'TOKEN'
    PRODUCTION = 'PRODUCTION'

    def __init__(self, file = sys.stdout, switches = set()):
        self.switches = switches.union({Logger.IMPLEMENT_ME})
        self.file = file

    def add_switch(self, switch):
        self.switches.add(switch)

    def remove_switch(self, switch):
        self.switches.discard(switch)

    def log(self, level, message):
        if level in self.switches:
            self.file.write(level + ': ' + message + '\n')

    def info(self, message):
        self.log(Logger.INFO, message)

    def debug(self, message):
        self.log(Logger.DEBUG, message)

    def critical(self, message):
        self.log(Logger.CRITICAL, message)

    def implement_me(self, method_name):
        self.log(Logger.IMPLEMENT_ME, method_name)

    def production(self, message):
        self.log(Logger.PRODUCTION, message)

    def token(self, message):
        self.log(Logger.TOKEN, message)

    def move_to_file(self, file):
        self.finalize()
        self.file = file

    def finalize(self):
        if self.file not in {sys.stdout, sys.stderr}:
            self.file.close()
        self.file = None
