from pathlib import Path
from utils import get_platform
import os
import json
import shutil
import yaml

class ConfigItem:
    def __init__(self, name:str, value=None) -> None:
        self.name = name
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

class ConfigGroup:
    def __init__(self, name:str) -> None:
        self.name = name

class Config:
    pass

def save_config(config_file_path:Path, default:bool=False):
    if default:
        shutil.copyfile('molex/default_config.yml', config_file_path)

def load_config(config_path=None) -> Config:
    if config_path is None:
        match get_platform():
            case 'win32':
                config_path = ''
            case _:
                config_path = '.config/molex'
    config_file = Path(config_path)/Path('molex.yml')

    if not os.path.exists(config_path):
        os.makedirs(config_path, exist_ok=True)
        save_config(config_file, default=True)

    with open(config_file, 'r') as raw_file:
        data:list[dict[str:dict]] = yaml.load(raw_file, Loader=yaml.SafeLoader)
        
    config_obj = Config()
    for config_group in data:

        group_name = list(config_group.keys())[0]
        config_group_obj = ConfigGroup(name=group_name)

        for name, value in list(config_group.values())[0].items():
            config_item_obj = ConfigItem(name=name, value=value)

            setattr(config_group_obj, name, config_item_obj)

        setattr(config_obj, group_name, config_group_obj)

    return config_obj

# print(load_config().metadata.DELIMITERS.value['SONG_TITLE'])