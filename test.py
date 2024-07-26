

from config import config

database_config = config['database']
logging_config = config['logging']
print(f"Database Host: {database_config['host']}")
print(f"Logging Level: {logging_config['level']}")

import logging
from log import init_yml_log, init_logger

def main():
    # 初始化日志配置
    # init_yml_log()

    # 获取日志记录器
    # logger = logging.getLogger(__name__)
    logger = init_logger(__name__)

    # 使用日志记录器记录日志
    logger.debug("这是一条debug级别的日志")
    logger.info("这是一条info级别的日志")
    logger.warning("这是一条warning级别的日志")
    logger.error("这是一条error级别的日志")
    logger.critical("这是一条critical级别的日志")

if __name__ == "__main__":
    main()