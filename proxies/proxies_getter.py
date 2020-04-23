import re
import datetime
import proxies.utils as utils


# 免费代理IP库 https://ip.jiangxianli.com/
def jiangxianli():
    def datetime_trans(time_str):
        minutes = 0
        try:
            day = re.findall(r"(\d+)天", time_str)
            hour = re.findall(r"(\d+)小时", time_str)
            min = re.findall(r"(\d+)分钟", time_str)
            minutes += int(day[0]) * 24 * 60 if day else 0
            minutes += int(hour[0]) * 60 if hour else 0
            minutes += int(min[0]) if min else 0
        finally:
            return minutes

    data = []
    url = "https://ip.jiangxianli.com/?page={}&country=%E4%B8%AD%E5%9B%BD"
    for i in range(1, 21):
        r = utils.get_url(url.format(i))
        rows = r.html.find("tbody>tr")
        for row in rows:
            _tds = row.find('td')
            data.append(
                dict(ip=_tds[0].text,
                     port=_tds[1].text,
                     locate=_tds[4].text,
                     alive=f"{datetime_trans(_tds[8].text)}min",
                     verify=_tds[9].text
                     )
            )
        break
