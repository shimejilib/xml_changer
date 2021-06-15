#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################
import xml.etree.ElementTree as ET
import time
target = "sample.xml"
root = ET.parse(target)
root.write(target + str(time.time()))

config = "config.conf"
with open(config) as f:
    lines = f.readlines()
    for line in lines:
        command, arg = line.replace("\n", "").split(":")
        if command == "path":
            x = root
            for i in arg.split("/"):
                tmp_list = []
                if type(x) == type([]):
                    for x_ele in x:
                        tmp_list.extend(x_ele.findall(i))
                else:
                    tmp_list = x.findall(i)
                x = tmp_list
        if command == "if":
            variable_name, value = arg.split("=")
            for x_i in x:
                if x_i.attrib[variable_name] == value:
                    x = x_i
        if command == "set":
            variable_name, value = arg.split("=")
            x.attrib[variable_name] = value
root.write(target)
