#-----------------------------------------------------------------------------
# Name:        p2pCommMapGlobal.py
#
# Purpose:     This module is used as a project global config file to set the 
#              constants, parameters and instances which will be used in the 
#              other modules in the project.
#              
# Author:      Yuancheng Liu
#
# Created:     2020/11/24
# Version:     v_0.3.1
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------
"""
For good coding practice, follow the below naming convention:
    1) Global variables should be defined with initial character 'g'.
    2) Global instances should be defined with initial character 'i'.
    3) Global CONSTANTS should be defined with UPPER_CASE letters.
"""

import os
import sys
import platform

print("Current working directory is : %s" % os.getcwd())
DIR_PATH = dirpath = os.path.dirname(os.path.abspath(__file__))
print("Current source code location : %s" % dirpath)
APP_NAME = ('p2pCommMap', 'App')

TOPDIR = 'src'
LIBDIR = 'lib'

#-----------------------------------------------------------------------------
# find the lib folder for importing the library modules
idx = dirpath.find(TOPDIR)
gTopDir = dirpath[:idx + len(TOPDIR)] if idx != -1 else dirpath   # found it - truncate right after TOPDIR
# Config the lib folder 
gLibDir = os.path.join(gTopDir, LIBDIR)
if os.path.exists(gLibDir): sys.path.insert(0, gLibDir)

#-----------------------------------------------------------------------------
# load the config file.
import ConfigLoader
CONFIG_FILE_NAME = 'config.txt'
gGonfigPath = os.path.join(dirpath, CONFIG_FILE_NAME)
iConfigLoader = ConfigLoader.ConfigLoader(gGonfigPath, mode='r')
if iConfigLoader is None:
    print("Error: The config file %s is not exist.Program exit!" %str(gGonfigPath))
    exit()
CONFIG_DICT = iConfigLoader.getJson()

#-----------------------------------------------------------------------------
# Init the logger
import Log
Log.initLogger(gTopDir, 'Logs', APP_NAME[0], APP_NAME[1], 
               historyCnt=100, fPutLogsUnderDate=True)

# Init the log type parameters.
DEBUG_FLG   = False
LOG_INFO    = 0
LOG_WARN    = 1
LOG_ERR     = 2
LOG_EXCEPT  = 3

def gDebugPrint(msg, prt=True, logType=None):
    if prt: print(msg)
    if logType == LOG_WARN:
        Log.warning(msg)
    elif logType == LOG_ERR:
        Log.error(msg)
    elif logType == LOG_EXCEPT:
        Log.exception(msg)
    elif logType == LOG_INFO or DEBUG_FLG:
        Log.info(msg)

APP_SEC_KEY = 'secrete-key-goes-here'
UPDATE_PERIODIC = 15
COOKIE_TIME = 30

#------<CONSTANTS>-------------------------------------------------------------
DB_PATH = os.path.join(dirpath , CONFIG_DICT['DB_NAME'])
NODES_FILE = os.path.join(dirpath, CONFIG_DICT['NODES_INFO'])

# Google map API billing key:
MAP_API_KEY = CONFIG_DICT['MAP_API_KEY'] # replace this with your own key.
# Comm HUB GPS location
CH_GPS = (float(CONFIG_DICT['HUB_LAT']), float(CONFIG_DICT['HUB_LONG'])) 

#-------<GLOBAL VARIABLES (start with "g")>------------------------------------
# VARIABLES are the built in data type.
gPeriod = 10
gMapFilter = ['show-inactive', 'show-gateway', 'show-control']
gMapSetting = [1, 1, 1] # Inactive, gateway, control hub communications respectively
gDevNode = []   
gLatestTime = 0.0

# Flask App parameters : 
gflaskHost = '0.0.0.0'
gflaskPort = int(CONFIG_DICT['FLASK_SER_PORT']) if 'FLASK_SER_PORT' in CONFIG_DICT.keys() else 5000
gflaskDebug = CONFIG_DICT['FLASK_DEBUG_MD']
gflaskMultiTH =  CONFIG_DICT['FLASK_MULTI_TH']

#-------<GLOBAL INSTANCES (start with "i")>-----------------------------------------------------
# INSTANCES are the object. 
iDataMgr = None
iSocketIO = None