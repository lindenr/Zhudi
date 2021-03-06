# coding: utf-8
''' Zhudi provides a Chinese - language dictionnary based on the
    C[E|F]DICT project Copyright - 2011 - Ma Jiehong

    Zhudi is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Zhudi is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
    License for more details.

    You should have received a copy of the GNU General Public License
    If not, see <http://www.gnu.org/licenses/>.

'''

import os

class Data(object):
    """ Data contains all the data used by Zhudi.
    """

    def __init__(self, simp, trad, trans,
                 wubi86, wubi86_short,
                 array30, array30_short,
                 cangjie5, cangjie5_short,
                 pinyin, zhuyin=None):
        """
        hanzi          : set of characters to use ("" by default)
        romanisation   : romanisation to use ("" by default)
        simp           : a list of simplified forms
        trad           : a list of traditional forms
        trans          : a list of translations
        wubi86         : a dictionary of wubi86 codes
        wubi86_short   : a dictionary of short wubi86 codes
        array30        : a dictionary of array30 codes
        array30_short  : a dictionary of short array30 codes
        cangjie5       : a dictionary of cangjie5 codes
        cangjie5_short : a dictionary of short cangjie5 codes
        pinyin         : a list of pinyin
        zhuyin         : a list of zhuyin (default = [])

        """

        self.hanzi = ""
        self.romanisation = ""
        self.set_of_chinese_chars = set()
        self.simplified = simp
        self.traditional = trad
        self.translation = trans
        self.pinyin = pinyin
        if zhuyin is None:
            self.zhuyin = []
        else:
            self.zhuyin = zhuyin
        self.wubi86 = wubi86
        self.wubi86_short = wubi86_short
        self.array30 = array30
        self.array30_short = array30_short
        self.cangjie5 = cangjie5
        self.cangjie5_short = cangjie5_short
        self.pinyin_to_zhuyin = [('zhuang', 'ㄓㄨㄤ'),
                                 ('shuang', 'ㄕㄨㄤ'),
                                 ('chuang', 'ㄔㄨㄤ'),
                                 ('zhuan', 'ㄓㄨㄢ'),
                                 ('zhuai', 'ㄓㄨㄞ'),
                                 ('zhong', 'ㄓㄨㄥ'),
                                 ('zheng', 'ㄓㄥ'),
                                 ('zhang', 'ㄓㄤ'),
                                 ('xiong', 'ㄒㄩㄥ'),
                                 ('xiang', 'ㄒㄧㄤ'),
                                 ('shuan', 'ㄕㄨㄢ'),
                                 ('shuai', 'ㄕㄨㄞ'),
                                 ('sheng', 'ㄕㄥ'),
                                 ('shang', 'ㄕㄤ'),
                                 ('qiong', 'ㄑㄩㄥ'),
                                 ('qiang', 'ㄑㄧㄤ'),
                                 ('niang', 'ㄋㄧㄤ'),
                                 ('liang', 'ㄌㄧㄤ'),
                                 ('kuang', 'ㄎㄨㄤ'),
                                 ('jiong', 'ㄐㄩㄥ'),
                                 ('jiang', 'ㄐㄧㄤ'),
                                 ('huang', 'ㄏㄨㄤ'),
                                 ('guang', 'ㄍㄨㄤ'),
                                 ('chuan', 'ㄔㄨㄢ'),
                                 ('chuai', 'ㄔㄨㄞ'),
                                 ('chong', 'ㄔㄨㄥ'),
                                 ('cheng', 'ㄔㄥ'),
                                 ('chang', 'ㄔㄤ'),
                                 ('zuan', 'ㄗㄨㄢ'),
                                 ('zong', 'ㄗㄨㄥ'),
                                 ('zhuo', 'ㄓㄨㄛ'),
                                 ('zhun', 'ㄓㄨㄣ'),
                                 ('zhui', 'ㄓㄨㄟ'),
                                 ('zhua', 'ㄓㄨㄚ'),
                                 ('zhou', 'ㄓㄡ'),
                                 ('zhen', 'ㄓㄣ'),
                                 ('zhei', 'ㄓㄟ'),
                                 ('zhao', 'ㄓㄠ'),
                                 ('zhan', 'ㄓㄢ'),
                                 ('zhai', 'ㄓㄞ'),
                                 ('zeng', 'ㄗㄥ'),
                                 ('zang', 'ㄗㄤ'),
                                 ('yuan', 'ㄩㄢ'),
                                 ('yong', 'ㄩㄥ'),
                                 ('ying', 'ㄧㄥ'),
                                 ('yang', 'ㄧㄤ'),
                                 ('xuan', 'ㄒㄩㄢ'),
                                 ('xing', 'ㄒㄧㄥ'),
                                 ('xien', 'ㄒㄧㄢ'),
                                 ('xiao', 'ㄒㄧㄠ'),
                                 ('xian', 'ㄒㄧㄢ'),
                                 ('wong', 'ㄨㄥ'),
                                 ('weng', 'ㄨㄥ'),
                                 ('wang', 'ㄨㄤ'),
                                 ('tuan', 'ㄊㄨㄢ'),
                                 ('tong', 'ㄊㄨㄥ'),
                                 ('ting', 'ㄊㄧㄥ'),
                                 ('tien', 'ㄊㄧㄢ'),
                                 ('tiao', 'ㄊㄧㄠ'),
                                 ('tian', 'ㄊㄧㄢ'),
                                 ('teng', 'ㄊㄥ'),
                                 ('tang', 'ㄊㄤ'),
                                 ('suan', 'ㄙㄨㄢ'),
                                 ('song', 'ㄙㄨㄥ'),
                                 ('shuo', 'ㄕㄨㄛ'),
                                 ('shun', 'ㄕㄨㄣ'),
                                 ('shui', 'ㄕㄨㄟ'),
                                 ('shua', 'ㄕㄨㄚ'),
                                 ('shou', 'ㄕㄡ'),
                                 ('shen', 'ㄕㄣ'),
                                 ('shei', 'ㄕㄟ'),
                                 ('shao', 'ㄕㄠ'),
                                 ('shan', 'ㄕㄢ'),
                                 ('shai', 'ㄕㄞ'),
                                 ('seng', 'ㄙㄥ'),
                                 ('sang', 'ㄙㄤ'),
                                 ('ruan', 'ㄖㄨㄢ'),
                                 ('rong', 'ㄖㄨㄥ'),
                                 ('reng', 'ㄖㄥ'),
                                 ('rang', 'ㄖㄤ'),
                                 ('quan', 'ㄑㄩㄢ'),
                                 ('qing', 'ㄑㄧㄥ'),
                                 ('qien', 'ㄑㄧㄢ'),
                                 ('qiao', 'ㄑㄧㄠ'),
                                 ('qian', 'ㄑㄧㄢ'),
                                 ('ping', 'ㄆㄧㄥ'),
                                 ('pien', 'ㄆㄧㄢ'),
                                 ('piao', 'ㄆㄧㄠ'),
                                 ('pian', 'ㄆㄧㄢ'),
                                 ('peng', 'ㄆㄥ'),
                                 ('pang', 'ㄆㄤ'),
                                 ('nuan', 'ㄋㄨㄢ'),
                                 ('nong', 'ㄋㄨㄥ'),
                                 ('ning', 'ㄋㄧㄥ'),
                                 ('nien', 'ㄋㄧㄢ'),
                                 ('niao', 'ㄋㄧㄠ'),
                                 ('nian', 'ㄋㄧㄢ'),
                                 ('neng', 'ㄋㄥ'),
                                 ('nang', 'ㄋㄤ'),
                                 ('ming', 'ㄇㄧㄥ'),
                                 ('mien', 'ㄇㄧㄢ'),
                                 ('miao', 'ㄇㄧㄠ'),
                                 ('mian', 'ㄇㄧㄢ'),
                                 ('meng', 'ㄇㄥ'),
                                 ('mang', 'ㄇㄤ'),
                                 ('luen', 'ㄌㄩㄢ'),
                                 ('luan', 'ㄌㄨㄢ'),
                                 ('long', 'ㄌㄨㄥ'),
                                 ('ling', 'ㄌㄧㄥ'),
                                 ('lien', 'ㄌㄧㄢ'),
                                 ('liao', 'ㄌㄧㄠ'),
                                 ('lian', 'ㄌㄧㄢ'),
                                 ('leng', 'ㄌㄥ'),
                                 ('lang', 'ㄌㄤ'),
                                 ('kuan', 'ㄎㄨㄢ'),
                                 ('kuai', 'ㄎㄨㄞ'),
                                 ('kong', 'ㄎㄨㄥ'),
                                 ('keng', 'ㄎㄥ'),
                                 ('kang', 'ㄎㄤ'),
                                 ('juan', 'ㄐㄩㄢ'),
                                 ('jing', 'ㄐㄧㄥ'),
                                 ('jien', 'ㄐㄧㄢ'),
                                 ('jiao', 'ㄐㄧㄠ'),
                                 ('jian', 'ㄐㄧㄢ'),
                                 ('huan', 'ㄏㄨㄢ'),
                                 ('huai', 'ㄏㄨㄞ'),
                                 ('hong', 'ㄏㄨㄥ'),
                                 ('heng', 'ㄏㄥ'),
                                 ('hang', 'ㄏㄤ'),
                                 ('guan', 'ㄍㄨㄢ'),
                                 ('guai', 'ㄍㄨㄞ'),
                                 ('gong', 'ㄍㄨㄥ'),
                                 ('geng', 'ㄍㄥ'),
                                 ('gang', 'ㄍㄤ'),
                                 ('fong', 'ㄈㄨㄥ'),
                                 ('fiao', 'ㄈㄧㄠ'),
                                 ('feng', 'ㄈㄥ'),
                                 ('fang', 'ㄈㄤ'),
                                 ('duan', 'ㄉㄨㄢ'),
                                 ('dong', 'ㄉㄨㄥ'),
                                 ('ding', 'ㄉㄧㄥ'),
                                 ('dien', 'ㄉㄧㄢ'),
                                 ('diao', 'ㄉㄧㄠ'),
                                 ('dian', 'ㄉㄧㄢ'),
                                 ('deng', 'ㄉㄥ'),
                                 ('dang', 'ㄉㄤ'),
                                 ('cuan', 'ㄘㄨㄢ'),
                                 ('cong', 'ㄘㄨㄥ'),
                                 ('chuo', 'ㄔㄨㄛ'),
                                 ('chun', 'ㄔㄨㄣ'),
                                 ('chui', 'ㄔㄨㄟ'),
                                 ('chua', 'ㄔㄨㄚ'),
                                 ('chou', 'ㄔㄡ'),
                                 ('chen', 'ㄔㄣ'),
                                 ('chao', 'ㄔㄠ'),
                                 ('chan', 'ㄔㄢ'),
                                 ('chai', 'ㄔㄞ'),
                                 ('ceng', 'ㄘㄥ'),
                                 ('cang', 'ㄘㄤ'),
                                 ('bing', 'ㄅㄧㄥ'),
                                 ('bien', 'ㄅㄧㄢ'),
                                 ('biao', 'ㄅㄧㄠ'),
                                 ('bian', 'ㄅㄧㄢ'),
                                 ('beng', 'ㄅㄥ'),
                                 ('bang', 'ㄅㄤ'),
                                 ('zuo', 'ㄗㄨㄛ'),
                                 ('zun', 'ㄗㄨㄣ'),
                                 ('zui', 'ㄗㄨㄟ'),
                                 ('zou', 'ㄗㄡ'),
                                 ('zhu', 'ㄓㄨ'),
                                 ('zhi', 'ㄓ'),
                                 ('zhe', 'ㄓㄜ'),
                                 ('zha', 'ㄓㄚ'),
                                 ('zen', 'ㄗㄣ'),
                                 ('zei', 'ㄗㄟ'),
                                 ('zao', 'ㄗㄠ'),
                                 ('zan', 'ㄗㄢ'),
                                 ('zai', 'ㄗㄞ'),
                                 ('yun', 'ㄩㄣ'),
                                 ('yue', 'ㄩㄝ'),
                                 ('you', 'ㄧㄡ'),
                                 ('yin', 'ㄧㄣ'),
                                 ('yao', 'ㄧㄠ'),
                                 ('yan', 'ㄧㄢ'),
                                 ('yai', 'ㄧㄞ'),
                                 ('xun', 'ㄒㄩㄣ'),
                                 ('xue', 'ㄒㄩㄝ'),
                                 ('xiu', 'ㄒㄧㄡ'),
                                 ('xin', 'ㄒㄧㄣ'),
                                 ('xie', 'ㄒㄧㄝ'),
                                 ('xia', 'ㄒㄧㄚ'),
                                 ('wen', 'ㄨㄣ'),
                                 ('wei', 'ㄨㄟ'),
                                 ('wan', 'ㄨㄢ'),
                                 ('wai', 'ㄨㄞ'),
                                 ('tuo', 'ㄊㄨㄛ'),
                                 ('tun', 'ㄊㄨㄣ'),
                                 ('tui', 'ㄊㄨㄟ'),
                                 ('tou', 'ㄊㄡ'),
                                 ('tie', 'ㄊㄧㄝ'),
                                 ('tao', 'ㄊㄠ'),
                                 ('tan', 'ㄊㄢ'),
                                 ('tai', 'ㄊㄞ'),
                                 ('suo', 'ㄙㄨㄛ'),
                                 ('sun', 'ㄙㄨㄣ'),
                                 ('sui', 'ㄙㄨㄟ'),
                                 ('sou', 'ㄙㄡ'),
                                 ('shu', 'ㄕㄨ'),
                                 ('shi', 'ㄕ'),
                                 ('she', 'ㄕㄜ'),
                                 ('sha', 'ㄕㄚ'),
                                 ('sen', 'ㄙㄣ'),
                                 ('sei', 'ㄙㄟ'),
                                 ('sao', 'ㄙㄠ'),
                                 ('san', 'ㄙㄢ'),
                                 ('sai', 'ㄙㄞ'),
                                 ('ruo', 'ㄖㄨㄛ'),
                                 ('run', 'ㄖㄨㄣ'),
                                 ('rui', 'ㄖㄨㄟ'),
                                 ('rou', 'ㄖㄡ'),
                                 ('ren', 'ㄖㄣ'),
                                 ('rao', 'ㄖㄠ'),
                                 ('ran', 'ㄖㄢ'),
                                 ('qun', 'ㄑㄩㄣ'),
                                 ('que', 'ㄑㄩㄝ'),
                                 ('qiu', 'ㄑㄧㄡ'),
                                 ('qin', 'ㄑㄧㄣ'),
                                 ('qie', 'ㄑㄧㄝ'),
                                 ('qia', 'ㄑㄧㄚ'),
                                 ('pou', 'ㄆㄡ'),
                                 ('pin', 'ㄆㄧㄣ'),
                                 ('pie', 'ㄆㄧㄝ'),
                                 ('pen', 'ㄆㄣ'),
                                 ('pei', 'ㄆㄟ'),
                                 ('pao', 'ㄆㄠ'),
                                 ('pan', 'ㄆㄢ'),
                                 ('pai', 'ㄆㄞ'),
                                 ('nuo', 'ㄋㄨㄛ'),
                                 ('nüe', 'ㄋㄩㄝ'),
                                 ('nou', 'ㄋㄡ'),
                                 ('niu', 'ㄋㄧㄡ'),
                                 ('nin', 'ㄋㄧㄣ'),
                                 ('nie', 'ㄋㄧㄝ'),
                                 ('nen', 'ㄋㄣ'),
                                 ('nei', 'ㄋㄟ'),
                                 ('nao', 'ㄋㄠ'),
                                 ('nan', 'ㄋㄢ'),
                                 ('nai', 'ㄋㄞ'),
                                 ('mou', 'ㄇㄡ'),
                                 ('miu', 'ㄇㄧㄡ'),
                                 ('min', 'ㄇㄧㄣ'),
                                 ('mie', 'ㄇㄧㄝ'),
                                 ('men', 'ㄇㄣ'),
                                 ('mei', 'ㄇㄟ'),
                                 ('mao', 'ㄇㄠ'),
                                 ('man', 'ㄇㄢ'),
                                 ('mai', 'ㄇㄞ'),
                                 ('luo', 'ㄌㄨㄛ'),
                                 ('lun', 'ㄌㄨㄣ'),
                                 ('lüe', 'ㄌㄩㄝ'),
                                 ('lou', 'ㄌㄡ'),
                                 ('liu', 'ㄌㄧㄡ'),
                                 ('lin', 'ㄌㄧㄣ'),
                                 ('lie', 'ㄌㄧㄝ'),
                                 ('lia', 'ㄌㄧㄚ'),
                                 ('lei', 'ㄌㄟ'),
                                 ('lao', 'ㄌㄠ'),
                                 ('lan', 'ㄌㄢ'),
                                 ('lai', 'ㄌㄞ'),
                                 ('kuo', 'ㄎㄨㄛ'),
                                 ('kun', 'ㄎㄨㄣ'),
                                 ('kui', 'ㄎㄨㄟ'),
                                 ('kua', 'ㄎㄨㄚ'),
                                 ('kou', 'ㄎㄡ'),
                                 ('ken', 'ㄎㄣ'),
                                 ('kao', 'ㄎㄠ'),
                                 ('kan', 'ㄎㄢ'),
                                 ('kai', 'ㄎㄞ'),
                                 ('jun', 'ㄐㄩㄣ'),
                                 ('jue', 'ㄐㄩㄝ'),
                                 ('jiu', 'ㄐㄧㄡ'),
                                 ('jin', 'ㄐㄧㄣ'),
                                 ('jie', 'ㄐㄧㄝ'),
                                 ('jia', 'ㄐㄧㄚ'),
                                 ('huo', 'ㄏㄨㄛ'),
                                 ('hun', 'ㄏㄨㄣ'),
                                 ('hui', 'ㄏㄨㄟ'),
                                 ('hua', 'ㄏㄨㄚ'),
                                 ('hou', 'ㄏㄡ'),
                                 ('hen', 'ㄏㄣ'),
                                 ('hei', 'ㄏㄟ'),
                                 ('hao', 'ㄏㄠ'),
                                 ('han', 'ㄏㄢ'),
                                 ('hai', 'ㄏㄞ'),
                                 ('guo', 'ㄍㄨㄛ'),
                                 ('gun', 'ㄍㄨㄣ'),
                                 ('gui', 'ㄍㄨㄟ'),
                                 ('gua', 'ㄍㄨㄚ'),
                                 ('gou', 'ㄍㄡ'),
                                 ('gen', 'ㄍㄣ'),
                                 ('gei', 'ㄍㄟ'),
                                 ('gao', 'ㄍㄠ'),
                                 ('gan', 'ㄍㄢ'),
                                 ('gai', 'ㄍㄞ'),
                                 ('fou', 'ㄈㄡ'),
                                 ('fen', 'ㄈㄣ'),
                                 ('fei', 'ㄈㄟ'),
                                 ('fan', 'ㄈㄢ'),
                                 ('eng', 'ㄥ'),
                                 ('duo', 'ㄉㄨㄛ'),
                                 ('dun', 'ㄉㄨㄣ'),
                                 ('dui', 'ㄉㄨㄟ'),
                                 ('dou', 'ㄉㄡ'),
                                 ('diu', 'ㄉㄧㄡ'),
                                 ('die', 'ㄉㄧㄝ'),
                                 ('dei', 'ㄉㄟ'),
                                 ('dao', 'ㄉㄠ'),
                                 ('dan', 'ㄉㄢ'),
                                 ('dai', 'ㄉㄞ'),
                                 ('cuo', 'ㄘㄨㄛ'),
                                 ('cun', 'ㄘㄨㄣ'),
                                 ('cui', 'ㄘㄨㄟ'),
                                 ('cou', 'ㄘㄡ'),
                                 ('chu', 'ㄔㄨ'),
                                 ('chi', 'ㄔ'),
                                 ('che', 'ㄔㄜ'),
                                 ('cha', 'ㄔㄚ'),
                                 ('cen', 'ㄘㄣ'),
                                 ('cao', 'ㄘㄠ'),
                                 ('can', 'ㄘㄢ'),
                                 ('cai', 'ㄘㄞ'),
                                 ('bin', 'ㄅㄧㄣ'),
                                 ('bie', 'ㄅㄧㄝ'),
                                 ('ben', 'ㄅㄣ'),
                                 ('bei', 'ㄅㄟ'),
                                 ('bao', 'ㄅㄠ'),
                                 ('ban', 'ㄅㄢ'),
                                 ('bai', 'ㄅㄞ'),
                                 ('ang', 'ㄤ'),
                                 ('zu', 'ㄗㄨ'),
                                 ('zi', 'ㄗ'),
                                 ('ze', 'ㄗㄜ'),
                                 ('za', 'ㄗㄚ'),
                                 ('yu', 'ㄩ'),
                                 ('yo', 'ㄧㄛ'),
                                 ('yi', 'ㄧ'),
                                 ('ye', 'ㄧㄝ'),
                                 ('ya', 'ㄧㄚ'),
                                 ('xu', 'ㄒㄩ'),
                                 ('xi', 'ㄒㄧ'),
                                 ('wu', 'ㄨ'),
                                 ('wo', 'ㄨㄛ'),
                                 ('wa', 'ㄨㄚ'),
                                 ('tu', 'ㄊㄨ'),
                                 ('ti', 'ㄊㄧ'),
                                 ('te', 'ㄊㄜ'),
                                 ('ta', 'ㄊㄚ'),
                                 ('su', 'ㄙㄨ'),
                                 ('si', 'ㄙ'),
                                 ('se', 'ㄙㄜ'),
                                 ('sa', 'ㄙㄚ'),
                                 ('ru', 'ㄖㄨ'),
                                 ('ri', 'ㄖ'),
                                 ('re', 'ㄖㄜ'),
                                 ('qu', 'ㄑㄩ'),
                                 ('qi', 'ㄑㄧ'),
                                 ('pu', 'ㄆㄨ'),
                                 ('po', 'ㄆㄛ'),
                                 ('pi', 'ㄆㄧ'),
                                 ('pa', 'ㄆㄚ'),
                                 ('ou', 'ㄡ'),
                                 ('nü', 'ㄋㄩ'),
                                 ('nu', 'ㄋㄨ'),
                                 ('ni', 'ㄋㄧ'),
                                 ('ne', 'ㄋㄜ'),
                                 ('na', 'ㄋㄚ'),
                                 ('mu', 'ㄇㄨ'),
                                 ('mo', 'ㄇㄛ'),
                                 ('mi', 'ㄇㄧ'),
                                 ('me', 'ㄇㄜ'),
                                 ('ma', 'ㄇㄚ'),
                                 ('lü', 'ㄌㄩ'),
                                 ('lu', 'ㄌㄨ'),
                                 ('li', 'ㄌㄧ'),
                                 ('le', 'ㄌㄜ'),
                                 ('la', 'ㄌㄚ'),
                                 ('ku', 'ㄎㄨ'),
                                 ('ke', 'ㄎㄜ'),
                                 ('ka', 'ㄎㄚ'),
                                 ('ju', 'ㄐㄩ'),
                                 ('ji', 'ㄐㄧ'),
                                 ('hu', 'ㄏㄨ'),
                                 ('he', 'ㄏㄜ'),
                                 ('ha', 'ㄏㄚ'),
                                 ('gu', 'ㄍㄨ'),
                                 ('ge', 'ㄍㄜ'),
                                 ('ga', 'ㄍㄚ'),
                                 ('fu', 'ㄈㄨ'),
                                 ('fo', 'ㄈㄛ'),
                                 ('fa', 'ㄈㄚ'),
                                 ('er', 'ㄦ'),
                                 ('en', 'ㄣ'),
                                 ('ei', 'ㄟ'),
                                 ('du', 'ㄉㄨ'),
                                 ('di', 'ㄉㄧ'),
                                 ('de', 'ㄉㄜ'),
                                 ('da', 'ㄉㄚ'),
                                 ('cu', 'ㄘㄨ'),
                                 ('ci', 'ㄘ'),
                                 ('ce', 'ㄘㄜ'),
                                 ('ca', 'ㄘㄚ'),
                                 ('bu', 'ㄅㄨ'),
                                 ('bo', 'ㄅㄛ'),
                                 ('bi', 'ㄅㄧ'),
                                 ('ba', 'ㄅㄚ'),
                                 ('ao', 'ㄠ'),
                                 ('an', 'ㄢ'),
                                 ('ai', 'ㄞ'),
                                 ('o', 'ㄛ'),
                                 ('e', 'ㄜ'),
                                 ('a', 'ㄚ'),
                                 ('5', '˙'),
                                 ('4', 'ˋ'),
                                 ('3', 'ˇ'),
                                 ('2', 'ˊ'),
                                 ('1', '')]

    def create_set_chinese_characters(self):
        """
        Create the set of all Chinese characters, for later

        """

        chinese_characters = []
        # Han # So [26] CJK RADICAL REPEAT, CJK RADICAL RAP
        chinese_characters += [x for x in range(0x2E80, 0x2E9A)]
        # Han # So [89] CJK RADICAL CHOKE, CJK RADICAL C-SIMPLIFIED TURTLE
        chinese_characters += [x for x in range(0x2E9B, 0x2EF4)]
        # Han # So [214] KANGXI RADICAL ONE, KANGXI RADICAL FLUTE
        chinese_characters += [x for x in range(0x2F00, 0x2FD6)]
        # Han # Lm IDEOGRAPHIC ITERATION MARK
        chinese_characters.append(0x3005)
        # Han # Nl IDEOGRAPHIC NUMBER ZERO
        chinese_characters.append(0x3007)
        # Han # Nl [9] HANGZHOU NUMERAL ONE, HANGZHOU NUMERAL NINE
        chinese_characters += [x for x in range(0x3021, 0x302A)]
        # Han # Nl [3] HANGZHOU NUMERAL TEN, HANGZHOU NUMERAL THIRTY
        chinese_characters += [x for x in range(0x3038, 0x303B)]
        # Han # Lm VERTICAL IDEOGRAPHIC ITERATION MARK
        chinese_characters.append(0x303B)
        # Han # Lo [6582] CJK UNIFIED IDEOGRAPH-3400, CJK UNIFIED IDEOGRAPH-4DB5
        chinese_characters += [x for x in range(0x3400, 0x4DB6)]
        # Han # Lo [20932] CJK UNIFIED IDEOGRAPH-4E00, CJK UNIFIED IDEOGRAPH-9FC3
        chinese_characters += [x for x in range(0x4E00, 0x9FC4)]
        # Han # Lo [302] CJK COMPATIBILITY IDEOGRAPH-F900, CJK COMPATIBILITY IDEOGRAPH-FA2D
        chinese_characters += [x for x in range(0xF900, 0xFA2E)]
        # Han # Lo [59] CJK COMPATIBILITY IDEOGRAPH-FA30, CJK COMPATIBILITY IDEOGRAPH-FA6A
        chinese_characters += [x for x in range(0xFA30, 0xFA6B)]
        # Han # Lo [106] CJK COMPATIBILITY IDEOGRAPH-FA70, CJK COMPATIBILITY IDEOGRAPH-FAD9
        chinese_characters += [x for x in range(0xFA70, 0xFADA)]
        # Han # Lo [42711] CJK UNIFIED IDEOGRAPH-20000, CJK UNIFIED IDEOGRAPH-2A6D6
        chinese_characters += [x for x in range(0x20000, 0x2A6D7)]
        # Han # Lo [542] CJK COMPATIBILITY IDEOGRAPH-2F800, CJK COMPATIBILITY IDEOGRAPH-2FA1D
        chinese_characters += [x for x in range(0x2F800, 0x2FA1E)]

        self.set_of_chinese_chars = set(chinese_characters)

    def load_config(self):
        """ Reads the config file, if it exists, and set the right values for
        hanzi and romanisation

        """
        saved_values = {}
        try:
            open(os.environ["HOME"] + "/.zhudi/config", "r")
        except IOError:
            # If no config file found
            print("No config file found. Use defaults")
            saved_values['hanzi'] = 'traditional'
            saved_values['romanisation'] = 'zhuyin'
            return saved_values
        with open(os.environ["HOME"]+"/.zhudi/config", "r") as config_file:
            lines = config_file.readlines()
            for n_line in range(len(lines)):
                if (lines[n_line][0] != "#") or (lines[n_line][0] != ""):
                    if lines[n_line][:-1].lower() == "romanisation:":
                        saved_values['romanisation'] = lines[n_line+1][:-1].lower()
                    if lines[n_line][:-1].lower() == "hanzi form:":
                        saved_values["hanzi"] = lines[n_line+1][:-1].lower()
        # Default values or gibberish in config file
        if saved_values['hanzi'] == '' or saved_values['hanzi'] not in ['traditional', 'simplified']:
            self.hanzi = 'traditional'
        elif saved_values['hanzi'] != '':
            self.hanzi = saved_values['hanzi']
        if saved_values['romanisation'] == '' or saved_values['romanisation'] not in ['zhuyin', 'pinyin']:
            self.romanisation = 'zhuyin'
        elif saved_values['romanisation'] != '':
            self.romanisation = saved_values['romanisation']

    def save_config(self):
        """
        This function saves values to the config file. The config file is
        overwritten if it already exists.
        """
        with open(os.environ["HOME"] + "/.zhudi/config", "w") as config_file:
            config_file.write("# This file is the configuration file" +
                              " used by Zhudi in order to remember\n")
            config_file.write("# user's configuration choices.\n")
            config_file.write("# This file has been created automatically" +
                              "by Zhudi.\n\n")
            config_file.write("romanisation:\n")
            config_file.write(self.romanisation + "\n\n")
            config_file.write("hanzi form:\n")
            config_file.write(self.hanzi + "\n\n")
