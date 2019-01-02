#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:11:11 2018

@author: band
"""

def genre(genreName=False):
    name = genreName
    if name:
        print (name)
    else:
        print ("There is no name " + str(name))        

def artist(artistName=False):
    name = artistName
    if name:
        print (name)
    else:
        print ("There is no artist name " + str(name))

def year(publishYear=False):
    year = publishYear
    if year:
        print (year)
    else:
        print ("There is no year " + str(year))

genre()
artist()
year()