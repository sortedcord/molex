from pathlib import Path
from utils import get_platform
import os
import json


class Config():

    class ConfigItem():
        def __init__(self, default, current=None) -> None:
            self.default = default
            if current is None:
                self.current = default
            else:
                self.current = current


    def save():
        pass

    def load():
        pass