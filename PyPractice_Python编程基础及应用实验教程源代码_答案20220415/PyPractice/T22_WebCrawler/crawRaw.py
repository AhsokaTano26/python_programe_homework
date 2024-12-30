import requests
from requests.exceptions import RequestException
import re
import json


# 获取单个页面
def get_one_page(url):
    try:
        # 添加头部信息，模拟浏览器头部，以免被HTTP服务器拒绝。
        headers = {
            'User-Agent': 'Mo'
        }
        response = requests.get(url, headers=headers)
        # 进行状态码判断，是否正确读取到网页
        # 200        表示请求成功      303        表示重定向        400        表示请求错误
        # 401        表示未授权        403        表示禁止访问      404        表示文件未找到
        # 500        表示服务器错误
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析网页
def parse_one_page(html):
    # 在直接使用字符串表示的正则表达式进行search, match和findall操作时，python会将字符串
    # 转换为正则表达式对象,为避免多次转换，所以一次生成正则表达式对象，提高效率，
    # re.S可实现跨行匹配
    # *匹配0或多个正好在它之前的那个字符。例如正则表达式。*意味着能够匹配任意数量的任何字符。 ? 匹配0或1个正好在它之前的那个字符。注意：这个元字符不是所有的软件都支持的。.*是指任何字符0个或多个，.?是指任何字符0个或1个.
    # .*具有贪婪的性质，首先匹配到不能匹配为止，根据后面的正则表达式，会进行回溯。.* ？则相反，一个匹配以后，就往下进行，所以不会进行回溯，具有最小匹配的性质。
    # ？表示非贪婪模式，即为匹配最近字符    如果不加?就是贪婪模式a. * bc    可以匹配
    pattern = re.compile('<dd>.*?'
                         + 'board-index.*?>(\d+)</i>.*?'
                         + 'href="(.*?)".*?'
                         + 'data-src="(.*?jpg).*?".*?'
                         + 'name"><a.*?>(.*?)</a>.*?'
                         + 'star">(.*?)</p>.*?'
                         + 'releasetime">(.*?)</p>.*?'
                         + 'integer">(.*?)</i>.*?'
                         + 'fraction">(.*?)</i>.*?'
                         + '</dd>', re.S)
    items = re.findall(pattern, html)
    onePageFilmInfo = []
    for item in items:
        eachFilmInfo = {
            'index': item[0],
            'href': "https://maoyan.com" + item[1],
            'image': item[2],
            'title': item[3],
            'actor': item[4].strip()[3:],
            'time': item[5].strip()[5:],
            'score': item[6] + item[7]
        }
        onePageFilmInfo.append(eachFilmInfo)
    return onePageFilmInfo


# 获取评价页面
def get_judge_page(judgeUrl):
    try:
        # 添加头部信息
        headers = {
            'User-Agent': 'Mo'
        }
        response = requests.get(judgeUrl, headers=headers)
        # 进行状态码判断，是否正确读取到网页
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析评价页面
def parse_judge_page(judgeContent):
    print(judgeContent)
    pattern = re.compile('<span.*?'
                         + 'num.*?>(\d+)</span>.*?<div.*?'
                         + 'comment-content.*?>(.*?)</div>', re.S)
    items = re.findall(pattern, judgeContent)
    # 按点赞数倒序排列
    items.sort(key=lambda x: int(x[0]), reverse=True)
    return items


# 将抓取的内容保存到文件
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(topNum):
    for offset in range(0, topNum, 10):
        url = 'http://maoyan.com/board/4?offset=' + str(offset)
        html = get_one_page(url)
        for item in parse_one_page(html):
            judgeContent = get_judge_page(item['href'])  # 爬取评价页面
            item['judgement'] = parse_judge_page(judgeContent)
            print(item)
            write_to_file(item)
            response = requests.get(item['image'])  # 下载图片：
            img = response.content  # 获取的文本实际上是图片的二进制文本
            # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
            with open('./movieImgs/{}.jpg'.format(item['title']),\
                'wb') as f:
                f.write(img)


if __name__ == '__main__':
    num = eval(input("请输入您要在Top100榜单中爬取的电影数量:"))
    print("Please waiting......")
    main(num)
