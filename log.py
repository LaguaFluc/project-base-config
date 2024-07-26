import datetime
import logging
from logging.config import fileConfig

"""方式一：读取ini"""
def init_ini_log() -> None:
    fileConfig('log.ini')


from logging.config import dictConfig
from yaml import load, safe_load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


"""方式二：读取yml"""
def init_yml_log() -> None:
    with open('log.yml', encoding="utf-8",mode='r') as obj:
        # logging_config = load(obj, Loader=Loader)
        logging_config = safe_load(obj)
    
    # 日志文件的基本名称
    base_log_filename = 'app'
    # 获取今天的日期，格式化为YYYY-MM-DD
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    # 生成今天的日志文件名
    log_filename = f'{base_log_filename}_{today}.log'
    
    # 更新handlers中的filename
    for handler in logging_config.get('handlers', {}).values():
        if 'filename' in handler:
            handler['filename'] = log_filename
    dictConfig(logging_config)


# now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# 获取当前日期


    
def init_logger(name: str) -> logging.Logger:
    """The main purpose of this function is to ensure that loggers are
    retrieved in such a way that we can be sure the root vllm logger has
    already been configured."""
    init_yml_log()
    today = datetime.datetime.now().strftime('%m%d')  # 格式化为MMDD格式
    fileinfo = logging.FileHandler(f"AutoTest_log_{today}.log")
    fileinfo.setLevel(logging.INFO) 
    return logging.getLogger(name)
# logger = logging.getLogger()