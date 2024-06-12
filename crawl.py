import json
import requests
from extract import Extract

class Crawl(object):
    def repost_crawl(self, uid, page):
        """
        Crawl reposts for a given Weibo post.

        Parameters:
        uid (str): The UID of the Weibo post.
        page (int): The page number to crawl.

        Returns:
        str: The response text containing the reposts.
        """
        id = self.__id_crawl(uid)
        cookies, headers = self.__crawl_setting()
        params = {
            'id': id,
            'page': page,
            'moduleID': 'feed',
            'count': '20',
        }
        response = requests.get('https://weibo.com/ajax/statuses/repostTimeline', params=params, cookies=cookies, headers=headers)
        return response.text

    def __id_crawl(self, uid):
        """
        Get the internal ID of a Weibo post based on its UID.

        Parameters:
        uid (str): The UID of the Weibo post.

        Returns:
        str: The internal ID of the Weibo post.
        """
        cookies, headers = self.__crawl_setting()
        params = {
            'id': uid,
            'locale': 'zh-CN',
        }
        resp = requests.get('https://www.weibo.com/ajax/statuses/show', params=params, cookies=cookies, headers=headers)

        id_info = json.loads(resp.text)
        id = id_info.get('id')
        return id

    def __crawl_setting(self):
        """
        Set the cookies and headers for Weibo requests.

        Returns:
        tuple: Cookies and headers for the request.
        """
        self.cookies = {
            'SINAGLOBAL': '9501109656994.648.1715309424073',
            'UOR': ',,cn.bing.com',
            'SUB': '_2A25LZfm4DeRhGeFG6FQZ8CvMzDSIHXVoG3NwrDV8PUNbmtAGLVDGkW9Nebxey2NdTtXiYNGN84ovx42ociESFJte',
            'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWNwX7z0VwFSicgpSNL.Oeo5JpX5KzhUgL.FoMRe0qReh-7S0n2dJLoI7_iqcHL9Kz7ehn7SBtt',
            'ALF': '02_1720260329',
            'PC_TOKEN': 'fc4831871d',
            '_s_tentry': 'weibo.com',
            'Apache': '2286212657060.6465.1717668765870',
            'ULV': '1717668765943:3:1:1:2286212657060.6465.1717668765870:1716037998864',
        }
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://weibo.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
        return self.cookies, self.headers

