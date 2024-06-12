import json

from crawl import Crawl
from extract import Extract
from store import Store

class Main(object):
    def __init__(self):
        self.crawl = Crawl()
        self.extract = Extract()
        self.store = Store()

    def __str__(self):
        return '-Building crawl, extract, and store modules-'

    def get_repost_info(self, uid):
        """
        Get repost information for a given Weibo post and store it in a MySQL database.

        Parameters:
        uid (str): The UID of the Weibo post.

        Returns:
        None
        """
        num = 0
        has_more = True
        while has_more:
            print(f'-Current page progress: {num} page')
            page = self.crawl.repost_crawl(uid, num)
            page_info = self.extract.repost_extract(page)
            print(f'-Extracted information: {page_info}')
            self.store.store_post_mode_mysql('WeiboRepost', uid, page_info)

            data = json.loads(page)
            all_page = data.get('max_page')

            if int(num) >= int(all_page):
                has_more = False
                print(f'-Extraction complete')
            else:
                num += 1

if __name__ == '__main__':
    main = Main()
    main.get_repost_info('OgFXw9LJp')
