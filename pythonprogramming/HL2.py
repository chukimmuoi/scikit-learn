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


def getInfomation(parent="50KD"):
    statspath = path + parent
    stock_list = [x[0] for x in os.walk(statspath)]

    ticker_list = []

    df = pd.DataFrame(columns=['serial', 'normal_default', 'normal_current', 'cool_default', 'cool_current', 'warm_default', 'warm_current'])

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
                endTime = ""
                if len(starts) >= 2:
                    startTime = starts[0].replace("[", "").replace("]", "").replace(" ", "").replace(
                        "===========Starting=============", "").replace("\n", "")
                    ends01 = starts[1].split("FACT0001")
                    if len(ends01) >= 2:
                        ends02 = ends01[1].split("Receive message[ OK]")
                        if len(ends02) >= 2:
                            endTime = ends02[0].replace("[", "").replace("]", "").replace(" ", "").replace("\n", "")
                if not endTime:
                    ""
                else:
                    serials1 = source.split('RSEN????')
                    if len(serials1) >= 2:
                        serials2 = serials1[1].split("Receive message[")
                        if len(serials2) >= 2:
                            serials3 = serials2[1].split('] compare Spec[] OK')
                            serial = serials3[0]

                    defual = source.split('] Set defual')
                    normal = ""
                    cool = ""
                    warm = ""
                    if len(defual) >= 4:
                        rgbs1 = defual[1].split('to TV OK')
                        if len(rgbs1) > 0:
                            normal = rgbs1[0]
                        rgbs2 = defual[2].split('to TV OK')
                        if len(rgbs2) > 0:
                            cool = rgbs2[0]
                        rgbs3 = defual[3].split('to TV OK')
                        if len(rgbs3) > 0:
                            warm = rgbs3[0]

                    current = source.split('] Current')
                    if len(current) >= 4:
                        current1 = current[1].split('\n')
                        if len(current1) > 0:
                            normal2 = current1[0]
                        current2 = current[2].split('\n')
                        if len(current2) > 0:
                            cool2 = current1[0]
                        current3 = current[3].split('\n')
                        if len(current3) > 0:
                            warm2 = current1[0]

                    df = df.append({'serial': serial, 'normal_default': normal, 'normal_current': normal2, 'cool_default': cool, 'cool_current': cool2, 'warm_default': warm, 'warm_current': warm2}, ignore_index=True)
    save = parent + '2.csv'
    df.to_csv(save)


getInfomation("50KD")
getInfomation("55KD")
getInfomation("55KE")
