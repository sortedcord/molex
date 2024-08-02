from config import Config

def test_config_save_defaults():
    _ = Config()
    _.save_config('/home/aditya/.config/molex/config.json')

test_config_save_defaults()