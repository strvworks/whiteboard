# coding: utf-8

from slackbot.bot import respond_to
from openweathermap import Openweather
import re
from datetime import datetime
from datetime import timedelta


@respond_to(r'天気|てんき|テンキ')
def wether_mention(message):
    msg = message.body['text']
    today = datetime.today()
    msg_day = re.findall(
            r'今日|きょう|明日|翌日|あした|アシタ|あす|' \
            + r'明後日|あさって|明々後日|しあさって',
            msg
            )
    weatherapi = Openweather()
    city = weatherapi.getCityname()

    date_str = ''
    if msg_day[0] == '今日' or msg_day[0]=='きょう':
        date_str = "{0:02d}{1:02d}".format(
                datetime.today().month, datetime.today().day
                )
        if datetime.today().hour >= 21:
            message.reply(
                    "21時以降は当日の天気予報情報を取得できません。" \
                    + "ごめんなさい。"
                    )
            return
    elif msg_day[0]=='明日' or msg_day[0]=='あす' or msg_day[0]=='あした' or msg_day[0]=='アシタ':
        today += timedelta(days=1)
        date_str = "{0:02d}{1:02d}".format(
                today.month, today.day
                )
        md_str = "{0}月{1}日".format(today.month, today.day)
    elif msg_day[0] == '明後日' or msg_day[0] == 'あさって':
        today += timedelta(days=2)
        date_str = "{0:02d}{1:02d}".format(
                today.month, today.day
                )
        md_str = "{0}月{1}日".format(today.month, today.day)
    elif msg_day[0] == '明々後日' or msg_day[0] == 'しあさって':
        today += timedelta(days=3)
        date_str = "{0:02d}{1:02d}".format(
                today.month, today.day
                )
        md_str = "{0}月{1}日".format(today.month, today.day)

    reply_str =  "\n" + md_str + "の" + city + "の天気をお伝えします。\n"

    try:
        weatherdata = weatherapi.getOnedayweather(date_str)
        for datum in weatherdata:
            reply_str += datum['time_str'] + "\t"
            reply_str += datum['japanese_main'] + "\n"
    except:
        message.reply(
                "取得中にエラーが発生しました。" \
                + "連続する場合は開発者に連絡ください。"
                )
        return

    message.reply(reply_str)