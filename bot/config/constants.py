from datetime import datetime

import discord
import pytz

TIME_ZONES = ['ACT', 'ACDT', 'ACST', 'ADT', 'AEDT',
              'AEST', 'AKDT', 'AKST', 'AMT', 'AMST', 'AST', 'AWST',
              'BOT', 'BRT', 'BRST', 'BST', 'CDT', 'CEST', 'CET',
              'CHST', 'CLT', 'CLST', 'COT', 'CST', 'CXT', 'CWST',
              'ECT', 'EDT', 'EEST', 'EST', 'FKST', 'FKT', 'FNT', 'GFT',
              'GMT', 'GMT+1', 'GMT+2', 'GMT+3', 'GMT+4', 'GMT+5', 'GMT+6',
              'GMT+7', 'GMT+8', 'GMT+9', 'GMT+10', 'GMT+11', 'GMT+12',
              'GMT-1', 'GMT-2', 'GMT-3', 'GMT-4', 'GMT-5', 'GMT-6', 'GMT-7',
              'GMT-8', 'GMT-9', 'GMT-10', 'GMT-11', 'GMT-12',
              'GYT', 'HADT', 'HAST', 'HST', 'HKT', 'IST', 'JST', 'KUYT',
              'LHDT', 'LHST', 'MDT', 'MSD', 'MSK', 'MST', 'NDT',
              'NFT', 'NST', 'NZST', 'NZDT', 'PDT', 'PST', 'PET', 'PYT', 'PYST',
              'SAMT', 'SDT', 'SRT', 'SST',
              'UTC', 'UTC+1', 'UTC+2', 'UTC+3', 'UTC+4', 'UTC+5', 'UTC+6',
              'UTC+7', 'UTC+8', 'UTC+9', 'UTC+10', 'UTC+11', 'UTC+12',
              'UTC-1', 'UTC-2', 'UTC-3', 'UTC-4', 'UTC-5', 'UTC-6', 'UTC-7',
              'UTC-8', 'UTC-9', 'UTC-10', 'UTC-11', 'UTC-12',
              'UYST', 'UYT', 'VET', 'WDT', 'WEST', 'WET', 'WST', 'YST', 'YDT']

RELEASE_DATES = [
                 ("PC Release", datetime(2018, 11, 1, tzinfo=pytz.timezone('US/Mountain'))),
                 ("Console Release", datetime(2018, 1, 26, tzinfo=pytz.timezone('US/Mountain'))),
                 ("Deviljho DLC", datetime(2018, 4, 1, tzinfo=pytz.timezone('US/Mountain')))
                ]

PLATFORMS = {'PC': 2, 'Console': 1}
