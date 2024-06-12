import json
import datetime
import pytz

class Extract(object):
    def repost_extract(self, page_info):
        """
        Extract repost information from the JSON response of a Weibo post.

        Parameters:
        page_info (str): The JSON response text containing repost information.

        Returns:
        list: A list of dictionaries containing extracted repost information.
        """
        data = json.loads(page_info)

        all_extracted_info = []

        for item in data['data']:
            extracted_info = {
                "微博ID": str(item.get('idstr', '')),
                "微博文本内容": item.get('text_raw', ''),
                "创建时间": self.__convert_time(item.get('created_at', '')),
                "用户ID": str(item['user'].get('idstr', '') if 'user' in item else ''),
                "用户昵称": item['user'].get('screen_name', '') if 'user' in item else '',
                "是否认证用户": item['user'].get('verified', False) if 'user' in item else False,
                "点赞数": str(item.get('attitudes_count', 0)),
                "转发数": str(item.get('reposts_count', 0)),
                "评论数": str(item.get('comments_count', 0)),
            }

            all_extracted_info.append(extracted_info)

        return all_extracted_info

    def __convert_time(self, created_str):
        """
        Convert the created time string to a formatted string in Beijing time.

        Parameters:
        created_str (str): The created time string in the format '%a %b %d %H:%M:%S %z %Y'.

        Returns:
        str: The formatted time string in Beijing time.
        """
        # Parse the created time string
        created_at = datetime.datetime.strptime(created_str, '%a %b %d %H:%M:%S %z %Y')

        # Set the time zone to Beijing time
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = created_at.astimezone(beijing_tz)

        # Format the time as a string in the desired format
        formatted_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        return formatted_time
