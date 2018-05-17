# coding: utf-8

import re
from datetime import datetime
from datetime import timedelta

class WordToDate:

    def __init__(self):
        self.tomorrow_words = '明日|翌日|あした|アシタ|あす|tomorrow'
        self.today_words = '今日|きょう|today'
        self.dat_words = '明後日|あさって'
        self.tda_words = '明々後日|しあさって'
        self.day_words = '{0}|{1}|{2}|{3}'.format(
                self.today_words, self.tomorrow_words, self.dat_words,
                self.tda_words)
        self.today = datetime.today()

    def getDaywords(self):
        return self.day_words

    def getTomorrowwords(self):
        return self.tomorrow_words

    def getDatwords(self):
        return self.dat_words

    def getTdawords(self):
        return self.tda_words

    def getTodaywords(self):
        return self.today_words

    def findDaywords(self, msg, getall = False):
        day_words = re.findall(self.day_words, msg)
        if getall:
            return day_words
        else:
            return day_words[0]

    def wordToAfterday(self, day_word):
        if day_word == '今日' or day_word=='きょう':
            today += timedelta(days=0)
            date_str = "{0:02d}{1:02d}".format(
                    today.month, today.day
                    )
            md_str = "{0}月{1}日".format(today.month, today.day)
            if datetime.today().hour >= 21:
                message.reply(
                        "21時以降は当日の天気予報情報を取得できません。" \
                        + "ごめんなさい。"
                        )
                return
        elif day_word == '明日' or day_word== 'あす' \
                or day_word=='あした' or day_word=='アシタ':
            today += timedelta(days=1)
            date_str = "{0:02d}{1:02d}".format(
                    today.month, today.day
                    )
            md_str = "{0}月{1}日".format(today.month, today.day)
        elif day_word == '明後日' or day_word == 'あさって':
            today += timedelta(days=2)
            date_str = "{0:02d}{1:02d}".format(
                    today.month, today.day
                    )
            md_str = "{0}月{1}日".format(today.month, today.day)
        elif day_word == '明々後日' or day_word == 'しあさって':
            today += timedelta(days=3)
            date_str = "{0:02d}{1:02d}".format(
                    today.month, today.day
                    )
            md_str = "{0}月{1}日".format(today.month, today.day)