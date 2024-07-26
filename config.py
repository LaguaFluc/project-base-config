import sys
from dynaconf import Dynaconf
from pathlib import Path

# 获取当前工作目录
BASE_DIR = Path.cwd()
import yaml

def load_config():
    with open('settings.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# 将配置加载到模块变量中
config = load_config()

# 导出配置变量
__all__ = ['config']