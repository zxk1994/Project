from biz import qunar
import time
from utils import util

if __name__ == '__main__':
    # while 1:
    util.logger.warning("开始爬取")
    zh = qunar.QuNarBiz()  #实例化对象
    zh.main()
    util.logger.warning("休眠")
