#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2021/4/13 12:58
@Author  ：维斯
@File    ：stock_base_data.py
@Version ：1.0
@Function：股票相关基础数据
"""
import json
import time

import requests
from stock.comon.jx_jquery_result import jx_jquery_result

base = {
    'f1': '',
    'f2': '最新价',  # 如31.42，则此字段为：31.42
    'f3': '涨幅',  # 如3.89%，则此字段为：3.89
    'f4': '',
    'f5': '',
    'f6': '',
    'f7': '振幅',  # 如5.36%，则此字段为：5.36
    'f8': '换手率',  # 如3.73%，则此字段为：3.72
    'f9': '市盈率',  # 如9.26，则此字段为：9.26
    'f10': '量比',  # 如1.76，则此字段为：1.76
    'f12': '',
    'f13': '',
    'f14': '',
    'f15': '',
    'f16': '',
    'f17': '',
    'f18': '昨收',  # 如31.3，则此字段为：31.3
    'f19': '',
    'f20': '',
    'f21': '流通市值',  # 如50亿，则此字段为：5000000000 （备注：此字段有可能为“-”）
    'f23': '市净率',  # 如9.26，则此字段为：9.26
    'f24': '60日涨跌幅',  # 如24.34%，则此字段为：24.34
    'f25': '',
    'f26': '',
    'f22': '',
    'f33': '',
    'f43': '',
    'f44': '当日交易日最高价',
    'f46': '',
    'f50': '当日交易日量比',
    'f51': '当日交易日涨停值',  # 如5.49，则此字段为：5.49
    'f52': '当日交易日跌停值',  # 如4.49，则此字段为：4.49
    'f11': '',
    'f62': '',
    'f128': '',
    'f136': '',
    'f115': '',
    'f152': '',
    'f124': '',
    'f107': '',
    'f104': '',
    'f105': '',
    'f140': '',
    'f141': '',
    'f207': '',
    'f208': '',
    'f209': '',
    'f222': ''
}


def get_hang_ye():
    """
    获取行业板块数据
    """
    url = 'http://81.push2.eastmoney.com/api/qt/clist/get?'
    params = {
        "cb": "jQuery112408297466168838283_1620571811003",
        "pn": "1",
        "pz": "10000",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f3",
        "fs": "m:90+t:2+f:!50",
        "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107,f104,f105,f140,f141,f207,f208,f209,f222",
        "_": "1620571811004"
    }
    result = requests.get(url, params=params).content.decode('utf-8')
    result = jx_jquery_result(result)
    # print(result)
    result = result['data']
    if result["total"] == len(result["diff"]):
        print(f'行业数据已全部获取：{result["total"]}条')
    else:
        print(f'行业数据获取不全：预期{result["total"]}条，实际{len(result["diff"])}条')
    return result


def get_a_all_stock():
    """
    获取沪深A股所有股票（预计：4488只 21.5.27日统计）
    :return:
    """
    url = 'http://35.push2.eastmoney.com/api/qt/clist/get?'
    params = {
        "cb": f"jQuery112408618214212067554_{str(int(time.time() * 1000))}",
        "pn": "1",  # 第n页
        "pz": "8000",  # 每页数量
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f3",
        "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23",
        # "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152",
        "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70,f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99,f100,f101,f102,f103,f104,f105,f106,f107,f108,f109,f110,f111,f112,f113,f114,f115,f116,f117,f118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128,f129,f130,f131,f132,f133,f134,f135,f136,f137,f138,f139,f140,f141,f142,f143,f144,f145,f146,f147,f148,f149,f150,f151,f152,f153,f154,f155,f156,f157,f158,f159,f160,f161,f162,f163,f164,f165,f166,f167,f168,f169,f170,f171,f172,f173,f174,f175,f176,f177,f178,f179,f180,f181,f182,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f193,f194,f195,f196,f197,f198,f199,f200,f201,f202,f203,f204,f205,f206,f207,f208,f209,f210,f211,f212,f213,f214,f215,f216,f217,f218,f219,f220,f221,f222,f223,f224,f225,f226,f227,f228,f229,f230,f231,f232,f233,f234,f235,f236,f237,f238,f239,f240,f241,f242,f243,f244,f245,f246,f247,f248,f249,f250,f251,f252,f253,f254,f255,f256,f257,f258,f259,f260,f261,f262,f263,f264,f265,f266,f267,f268,f269,f270,f271,f272,f273,f274,f275,f276,f277,f278,f279,f280,f281,f282,f283,f284,f285,f286,f287,f288,f289,f290,f291,f292,f293,f294,f295,f296,f297,f298,f299,f300,f301,f302,f303,f304,f305,f306,f307,f308,f309,f310,f311,f312,f313,f314,f315,f316,f317,f318,f319,f320,f321,f322,f323,f324,f325,f326,f327,f328,f329,f330,f331,f332,f333,f334,f335,f336,f337,f338,f339,f340,f341,f342,f343,f344,f345,f346,f347,f348,f349,f350,f351,f352,f353,f354,f355,f356,f357,f358,f359,f360,f361,f362,f363,f364,f365,f366,f367,f368,f369,f370,f371,f372,f373,f374,f375,f376,f377,f378,f379,f380,f381,f382,f383,f384,f385,f386,f387,f388,f389,f390,f391,f392,f393,f394,f395,f396,f397,f398,f399,f400,f401,f402,f403,f404,f405,f406,f407,f408,f409,f410,f411,f412,f413,f414,f415,f416,f417,f418,f419,f420,f421,f422,f423,f424,f425,f426,f427,f428,f429,f430,f431,f432,f433,f434,f435,f436,f437,f438,f439,f440,f441,f442,f443,f444,f445,f446,f447,f448,f449,f450,f451,f452,f453,f454,f455,f456,f457,f458,f459,f460,f461,f462,f463,f464,f465,f466,f467,f468,f469,f470,f471,f472,f473,f474,f475,f476,f477,f478,f479,f480,f481,f482,f483,f484,f485,f486,f487,f488,f489,f490,f491,f492,f493,f494,f495,f496,f497,f498,f499,f500",
        "_": str(int(time.time() * 1000))
    }
    result = requests.get(url, params=params).content.decode('utf-8')
    result = jx_jquery_result(result)
    result = result['data']
    if result["total"] == len(result["diff"]):
        print(f'沪深A股所有股票已全部获取：{result["total"]}条')
    else:
        print(f'沪深A股股票数据获取不全：预期{result["total"]}条，实际{len(result["diff"])}条')
    return result


if __name__ == '__main__':
    dict_result = get_a_all_stock()
    stock_id = '300887'
    data_alone = {}
    for i in dict_result['diff']:
        if i['f12'] == stock_id:
            data_alone = i
    print(json.dumps(data_alone, ensure_ascii=False))
    # f1,f2,f3,f4,f5,f6,f7,
    # count = 500
    # ss = ''
    # for i in range(count):
    #     ss += f'f{i + 1}'
    #     if i != count - 1:
    #         ss += ','
    # print(ss)
