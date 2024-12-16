#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        p2pCommMapApp.py
#
# Purpose:     This module will create a topographic map to show deployed gateway 
#              devices communication situation. It is is a sub-project of the 
#              'QSG-Manager dashboard' (Quantum Safe Gateway Manager) project. 
#              
# Author:      Liu Yuancheng
#
# version:     v_0.3.1
# Created:     2020/05/22
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------

# import python built in modules.
import os

# import pip installed modules.
from flask import Flask, render_template, request
# Install flask socketio library: pip3 install flask_socketio
from flask_socketio import SocketIO

# import project local modules.
import p2pCommMapGlobal as gv
import p2pCommMapDataMgr as dm
import Log


# Set this module execution flags.
TEST_MODE = True    # Test mode flag - True: test on local computer.
LOG_FLAG = True     # log information display flag.


# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG'] = True  
gv.iSocketIO = SocketIO(app)

gv.iDataMgr = dm.DataMgr(None, 0, "server thread")
gv.iDataMgr.loadNodesData()
gv.iDataMgr.start()

#----------------------------------------------------------------------------------------------------
# Server setup function
@app.route('/', methods=['GET', 'POST'])
def home():
    gv.gDebugPrint("flask app: route request.", logType=gv.LOG_INFO)
    if request.method == 'POST':
        gv.gPeriod = int(request.form['rate-uptake'])
        for idx, data in enumerate(gv.gMapFilter):
            gv.gMapSetting[idx] = 1 if request.form.get(data) != None else 0
        if gv.iDataMgr: gv.iDataMgr.setUpdateRate(gv.gPeriod)
    return render_template("index.html", 
                            gateway=gv.iDataMgr.getMarkersJSON(), 
                            period=gv.gPeriod, 
                            setting=gv.gMapSetting)

@gv.iSocketIO.on('connect', namespace='/test')
def test_connect():
    gv.gDebugPrint("SocketIO: Client connected.", logType=gv.LOG_INFO)

@gv.iSocketIO.on('disconnect', namespace='/test')
def test_disconnect():
    gv.gDebugPrint("SocketIO: Client disconnected.", logType=gv.LOG_INFO)

#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    gv.iSocketIO.run(app, host=gv.gflaskHost, port=gv.gflaskPort)
    print('End of __main__')

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#if __name__ == '__main__':
#    #app.run(host="0.0.0.0", port=5000,  debug=False, threaded=True)
#    app.run(host=gv.gflaskHost,
#        port=gv.gflaskPort,
#        debug=gv.gflaskDebug,
#        threaded=gv.gflaskMultiTH)
