import configparser
import os

#  实例化configParser对象
config = configparser.ConfigParser()
parent_dir = os.path.dirname(os.path.abspath(__file__))
config.read(parent_dir+'/config.ini', encoding='utf-8')


def get_config(section, option):
    return config.get(section, option)


def write_config(section, option, value):
    with open('config.ini', 'w') as f:
        config.set(section, option, value)
        config.write(f)


def get_config_obj():
    return config


if __name__ == "__main__":
    value = get_config("baidu", "username")
    print(value)
    sections = config.sections()
    print(sections)
    keys = config.options('qqmail')
    print(keys)
