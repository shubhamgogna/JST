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
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import sys


class BaseLogger(object):
    IMPLEMENT= 'IMPLEMENT_ME'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    CRITICAL = 'CRITICAL'

    def __init__(self, file=sys.stdout, switches=set()):
        self.switches = switches.union({BaseLogger.IMPLEMENT})
        self.file = file

    def finalize(self):
        if self.file not in {sys.stdout, sys.stderr}:
            self.file.close()
        self.file = None

    def move_to_file(self, file):
        self.finalize()
        self.file = file

    def add_switch(self, switch):
        self.switches.add(switch)

    def remove_switch(self, switch):
        self.switches.discard(switch)

    def log(self, level, message):
        if level in self.switches:
            self.file.write(level + ': ' + message + '\n')

    def implement_me(self, method_name):
        self.log(BaseLogger.IMPLEMENT, method_name)

    def info(self, message):
        self.log(BaseLogger.INFO, message)

    def critical(self, message):
        self.log(BaseLogger.DEBUG, message)

    def critical(self, message):
        self.log(BaseLogger.CRITICAL, message)
