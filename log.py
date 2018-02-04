# coding:utf-8
import logging
import logging.handlers


class Logger(logging.Logger):

    def __init__(self, filename=None):
        super(Logger, self).__init__(self)
        if filename is None:
            filename = "./logs/pt.log"
        # 创建handler用于写入日志文件（每天生成一个保留30天的日志）
        loghandler = logging.handlers.TimedRotatingFileHandler(filename, 'D', 1, 30)
        loghandler.suffix = "%Y%m%d-%H%M.log"
        loghandler.setLevel(logging.WARNING)

        # 创建handler用于终端打印日志
        terminalhandler = logging.StreamHandler()
        terminalhandler.setLevel(logging.DEBUG)

        # 定义handler日志输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-'
                                      '[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        loghandler.setFormatter(formatter)
        terminalhandler.setFormatter(formatter)

        # 将logger添加到handler管理
        self.addHandler(loghandler)
        self.addHandler(terminalhandler)


if __name__ == "__main__":
    log = Logger()
    log.warning('测试一下')