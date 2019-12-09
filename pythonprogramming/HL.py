import pandas as pd
import os
import time
from datetime import datetime

from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background")

import re
import urllib

path = "/Users/chukimmuoi/Downloads/WB_LOG_1209/"


def lol(parent="50KD"):
    statspath = path + parent
    stock_list = [x[0] for x in os.walk(statspath)]

    ticker_list = []

    df = pd.DataFrame(columns=['start',
                               'end',
                               'time',
                               'state',
                               'time_out_wb',
                               'other'])
    countPass = 0
    countFail = 0
    sumTime = 0
    errorWb = 0
    errorOther = 0

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("/")[-1]
        ticker_list.append(ticker)

        if len(each_file) > 0:
            for file in each_file:
                full_file_path = each_dir + '/' + file
                # print(full_file_path)
                source = open(full_file_path, 'r', encoding='mac_roman').read()
                starts = source.split('#### Read RFID ####')
                startTime = ""
                endTime = ""
                if len(starts) >= 2:
                    startTime = starts[0].replace("[", "").replace("]", "").replace(" ", "").replace(
                        "===========Starting=============", "").replace("\n", "")
                    ends01 = starts[1].split("FACT0001")
                    if len(ends01) >= 2:
                        ends02 = ends01[1].split("Receive message[ OK]")
                        if len(ends02) >= 2:
                            endTime = ends02[0].replace("[", "").replace("]", "").replace(" ", "").replace("\n", "")

                # print("start", startTime)
                # print("end", endTime)
                dis = 0
                state = "Fail"
                timeOutWb = 0
                other = 0
                if not endTime:
                    state = "Fail"
                    countFail += 1

                    timeouts = source.split('WB Adjust - timeout')
                    if len(timeouts) >= 2:
                        errorWb += 1
                        timeOutWb = 1
                    else:
                        errorOther += 1
                        other = 1
                else:
                    state = "Pass"
                    countPass += 1

                    startTimes = startTime.split(":")
                    endTimes = endTime.split(":")
                    dis = int(endTimes[0]) * 60 + int(endTimes[1]) - int(startTimes[0]) * 60 - int(startTimes[1])
                    # print("dis", dis)
                    if dis > 0:
                        sumTime += dis

                df = df.append({'start': startTime,
                                'end': endTime,
                                'time': dis,
                                'state': state,
                                'time_out_wb': timeOutWb,
                                'other': other}, ignore_index=True)
    # print("Sum time", sumTime)
    print("Model %s: Pass: %d(%f percent), Fail %d(%f percent), Time TB %f, Error WB %d(%f percent), Error Other %d(%f percent)" % (
    parent, countPass, (countPass / (countFail + countPass)) * 100, countFail,
    (countFail / (countFail + countPass)) * 100, sumTime / countPass, errorWb, (errorWb / (errorWb + errorOther)) * 100,
    errorOther, (errorOther / (errorWb + errorOther)) * 100))
    save = parent + '.csv'
    df.to_csv(save)


lol("50KD")
lol("55KD")
lol("55KE")
