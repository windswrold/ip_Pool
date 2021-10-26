from fake_useragent import UserAgent
import requests
import re
sdurl = 'https://yw.gangguwang.com/share?id=268314'
ipsource = 'https://ip.jiangxianli.com';
ua = UserAgent()
def run():
    try:
        for f in range(20000):
            f = f + 1
            f = str(f)
            url =ipsource + '/?page=' + f
            heands = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.58'
            }
            iptxt = requests.get(url, headers=heands).text
            pattern = re.compile('(?<=<button class="layui-btn layui-btn-sm btn-copy" data-url=).*(?= data-unique-id=)')
            ip = pattern.findall(iptxt)
            ip = str(ip).replace('"', '')
            pattern = re.compile('[a-zA-z]+://[^\s]*')
            ipps = pattern.findall(ip)
            n = 1
            for x in ipps:
                try:
                    ixp = {'http': ipps[n]}
                    print(ixp)
                    heands = {
                        'User-Agent': ua.random
                    }
                    print(heands)
                    requests.get(sdurl, proxies=ixp, headers=heands, timeout=3)
                    n = n + 1
                    print('成功')

                except:
                    print('代理IP异常')

    except:
        print('IP池获取异常')

def main_handler(event, context):
    run()

if __name__ == '__main__':
    run()
