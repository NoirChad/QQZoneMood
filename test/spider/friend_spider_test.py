import unittest

from src.spider.QQZoneFriendSpider import QQZoneFriendSpider
from src.util.constant import BASE_DIR

class FriendSpiderTest(unittest.TestCase):

    def test_init(self):
        QQZoneFriendSpider()

    def test_get_friend_list(self):
        fs = QQZoneFriendSpider(use_redis=False, analysis=False)
        fs.get_friend_list()

    def test_get_friend_detail(self):
        fs = QQZoneFriendSpider(use_redis=False, analysis=False)
        fs.get_friend_detail()

    def test_clean_friend_data(self):
        fs = QQZoneFriendSpider(use_redis=False, analysis=True, export_csv=False)
        fs.clean_friend_data()
        print("friend df:", fs.friend_df.shape)

    def test_get_first_friend_info(self):
        fs = QQZoneFriendSpider(use_redis=False, analysis=True)
        fs.get_first_friend_info()
        print(fs.user_info.first_friend, fs.user_info.first_friend_time)

    def test_download_friend_header(self):
        fs = QQZoneFriendSpider(use_redis=True, analysis=True)
        fs.download_head_image()
