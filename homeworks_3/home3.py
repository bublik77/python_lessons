#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:38:32 2018

@author: band
"""

def compare (one,two,three):
    try:
        if int(one) and int(two) and (three):
            if int(one) > int(two):
                print(one + " is more then "+two)
    except:
        print('cannot')

compare(5,'3',4)