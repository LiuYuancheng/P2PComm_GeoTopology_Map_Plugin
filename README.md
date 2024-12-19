# P2PComm_GeoTopology_Map_Plugin

![](doc/img/rm_s00.png)

`Figure-00 P2PComm_GeoTopology_Map program view diagram, version v0.2.1 (2024)`

**Program Design Purpose**: The goal of this project is to develop a Flask-based web App plugin that can be integrated into other Security Information and Event Management (SIEM) system for devices' communication data and state visualization. This plugin is designed to visualize real-time peer-to-peer (P2P) communication status within a distributed system with key metrics such as data flow throughput between encrypted devices and data transmission speed between servers and clients will be displayed alongside the network topology on an interactive geolocation map. This visualization Web-App will enable security administrators to effectively monitor, analyze, and manage real-time P2P communication states, helping to identify potential performance bottlenecks, latency issues, and abnormal communication patterns across the distributed network.

```python
# Version:     v0.2.1
# Created:     2020/05/22
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

**Table of Contents**

[TOC]

- [P2PComm_GeoTopology_Map_Plugin](#p2pcomm-geotopology-map-plugin)
    + [Introduction](#introduction)
      - [System Main Components Introduction](#system-main-components-introduction)
    + [System Design](#system-design)
      - [User Interface Design](#user-interface-design)
    + [Program Setup](#program-setup)
    + [Program Usage](#program-usage)
    + [Reference](#reference)

------

### Introduction

The P2PComm_GeoTopology_Map_Plugin is a Flask-based web application designed to visualize real-time peer-to-peer (P2P) communication diagrams and network topology over an interactive geolocation map. The plugin app use Google Maps API and full customizable configuration settings to provide an all-in-one HTML webpage which can be easily integrated in other into other Security Information and Event Management (SIEM) systems to make it a valuable addition for monitoring and managing distributed network communications. The Web plug UI is shown below:

![](doc/img/map01.gif)

`Figure-01 P2PComm_GeoTopology_Map program web UI view, version v0.2.1 (2024)`

This tool can help the security administrators with enhanced capabilities to monitor and analyze distributed system communications. The four features provided by the program are:

- **P2P Device Data Flow Throughput**: Visualizes the transmission rate and data volume exchanged between encryption devices.
- **Data Transmission Speed**: Tracks connection state, latency between servers, clients, and other network nodes.
- **Network Topology**: Dynamically maps peer-to-peer relationships and data exchange paths.
- **Geolocation Mapping**: Displays the physical locations of nodes and their communication links over an interactive map interface.

#### System Main Components Introduction

The project is structured into three main components:

1. **GeoTopology_Map Front-End Application**: A Flask-based front-end module that integrates with the Google Maps API to render an interactive map for real-time visualization.
2. **Backend Data Database**: A lightweight SQLite3 database backend to store and manage device communication data, making it accessible to the web application.
3. **Data Collection Module**: An interface program that gathers communication data from devices and updates the database in real time.

These components form a system for visualizing and managing P2P communication and network topology, enhancing situational awareness and network security analysis. For the plugin demo, please refer to this video: https://youtu.be/mazMEglxK_U



------

### System Design

The system workflow diagram is shown below:

![](doc/img/rm_s04.png)

`Figure-02 P2PComm_GeoTopology_Map program workflow diagram, version v0.2.1 (2024)`

The system includes four function modules:

**Flask Web Host Application** 

- **Function**: Hosts the web interface and serves data to the user.
- **Key Features**: Interactive map visualization using Google Maps API,  User-configurable settings for customizing the displayed topology and Real-time data updates based on user setting.

**Data Management Module**

- **Purpose**: Coordinates the overall workflow and integrates different modules.
- **Key Features**: Loads initial configurations (e.g., database connections, API keys),  Manages data threads for processing and communication, Queries the database for the latest node and link data and Creates JSON objects for nodes and communication links.

**Database**

- **Function** : Store  the Node metadata (e.g., device IDs, geolocations) and Node metadata (e.g., device IDs, geolocations). Two table are included with below config:

```sqlite
CREATE TABLE IF NOT EXISTS gatewayInfo(id integer PRIMARY KEY, name text NOT NULL,ipAddr text NOT NULL,lat float NOT NULL,lng float NOT NULL, actF integer NOT NULL, rptTo integer NOT NULL,type text NOT NULL)
```

```sqlite
CREATE TABLE IF NOT EXISTS gatewayState(time float PRIMARY KEY,id text NOT NULL, updateInfo text NOT NULL)
```

**Data Collection Module**

- **Function** : Gathers data from monitored devices and updates the database.

#### User Interface Design

In the demo web app, we added a sidebar attached beside the map which allow users to change various map settings. The user can choose the data update rate of the flask webserver calling GET request through a dropdown menu. A filter function is also added to adjust the display certain types of communication links (active, gateway, control hub). 

The design of the control side bar is shown below:

![](doc/img/rm_s05.png)

`Figure-03 P2PComm_GeoTopology_Map control side bar design diagram, version v0.2.1 (2024)`

The design of symbols, icons and links on the map panel is shown below:

![](doc/img/rm_s06.png)

`Figure-04 P2PComm_GeoTopology_Map map symbol icon link detail diagram, version v0.2.1 (2024)`

| Name                      | Type | Description                                                  |
| ------------------------- | ---- | ------------------------------------------------------------ |
| Yellow Marker             | Icon | Control hub node                                             |
| Blue Marker               | Icon | Gateway or device node                                       |
| Red Line Between Makers   | Link | Active link gateway or device report to control hub          |
| Blue Line Between Makers  | Link | Active communication link between two device                 |
| Black Line Between Makers | Link | Inactive communication link between two device               |
| Green Arrow Pointer       | Icon | Animated symbol shows Gateway report to Control Hub regularly |
| Dark Blue Circle          | Icon | Animated symbol for show the data transmission between two device |



------

### Program Setup

**Development Environment**  :  Python3.7.4, HTML+flask, socketIO+eventlet, SQLite3

**Additional Lib/Software Need**

| Lib Module          | Version | Installation                  | Lib link                                                |
| ------------------- | ------- | ----------------------------- | ------------------------------------------------------- |
| **Flask**           | 1.1.2   | `pip install Flask`           | https://flask.palletsprojects.com/en/3.0.x/             |
| **flask-socketIO**  | 4.5.1   | `pip3 install flask-socketio` | https://flask-socketio.readthedocs.io/en/latest/        |
| **SQL Browser**     |         |                               | https://sqlitebrowser.org/blog/version-3-12-2-released/ |
| **python eventlet** |         | pip3 install eventlet         | https://pypi.org/project/eventlet/                      |

**Hardware Needed** : None

**Program Files List** 

| Program File                     | Execution Env | Description                                                  |
| -------------------------------- | ------------- | ------------------------------------------------------------ |
| `src/p2pCommMapApp.py`           | python3       | Main flask web plug-in p2p connection topology diagram over the geolocation map to show devices communication situation. |
| `src/p2pCommMapGlobal.py`        | python3       | This module stores all the global variables used in the flask webserver. |
| `src/node_database.db`           |               | Database file.                                               |
| `src/databaseCreater.py`         | python3       | Module to insert the simulation test data into the data base. |
| `lib/Log.py`                     | python3       | Log generation mode.                                         |
| `src/nodes_record_template.json` | JSON          | File template to save simulation node information.           |
| `lib/ConfigLoader.py`            | python3       | Module to load the node record file.                         |
| `src/templates/index.html`       | HTML          | This file generates the UI of the Topological Maps using Google Maps. |
| `src/static/js/maps.js`          | JavaScript    | This module stores the static JS functions to run the Google Map. |
| `src/static/css/map.css`         | CSS           | This is the stylesheet for the Topological Map.              |
| `src/static/img`                 |               | Image file used by the web page.                             |
| `src/config_template.txt`        |               | The config file template                                     |



------

### Program Usage

Follow the below steps to execute the program

**Step1:Setup the configuration file**

Rename the `src/config_template.txt` to `config.txt` , then fill in the your google map API Key and set the parameters as shown below:

```
# This is the config file template for P2P communication display map
# emulator program <p2pCommMapApp.py>
# Setup the parameter with below format (every line follows <key>:<value> format, the
# key can not be changed):
#-----------------------------------------------------------------------------
# Database file name
DB_NAME:node_database.db
# Node information record
NODES_INFO:nodes_record.json
# Google Map API key
MAP_API_KEY:AIzaSyBoHBPqxFw40DFvCbXrj1IWNcvkzb6WkkI
# Set the Hub GPS location
HUB_LAT:1.2945315
HUB_LONG:103.7746052
#-----------------------------------------------------------------------------
# Init the PLC local web Flask app parameters
FLASK_SER_PORT:5000
FLASK_DEBUG_MD:False
FLASK_MULTI_TH:True
```

Rename the `src/nodes_record_template.json` to `src/nodes_record.txt` and add your node in the json file with below info:

```json
"<Node_ID>": {
    "no": 1,
    "name": "NUS",
    "ipAddr": "10.0.0.1",
    "lat": 1.2964053,
    "lng": 103.7690442,
    "type": "GW",
    "rptTo": 0,
    "actF": 0
}
```

To find the Geolocation GPS of a IP you can use the online tool or this app: https://github.com/LiuYuancheng/IPGeoPosLocater



**Step 2 : Run the test data creator and map P2PComm_GeoTopology_Map App**

Start up the data insert simulation program to add new gateway 
```
python3 databaseCreater.py
```

If you want to link to your system call the module function `updateStateTable(self, gatewayID, infoStr)` to insert the new gateway state in to database.

Run the flask webserver to retrieve data from the QSG-Manager

```
python3 p2pCommMapApp.py
```

**Step3 : View the P2PComm_GeoTopology_Map**

After running step2, wait 10 sec make sure the database thread fully started then do step 3, open web browser and enter URL: http://127.0.0.1:5000, then check the web plug in as shown below:

![](doc/img/UI_view.png)

`Figure-05 Communication map screenshot, version v0.2.1 (2024)`

You can use iframe to integrate the map in your SIEM dashboard, for example in Grafana dashboard you can set the AJAX config as shown below:

![](doc/img/rm_s07.png)

`Figure-06 AJAX config to integrate P2PComm_GeoTopology_Map in Grafana Panel, version v0.2.1 (2024)`

Then you can see the map will show on the Grafana dashboard page:

![](doc/img/rm_s08.png)

`Figure-07 Viiew the P2PComm_GeoTopology_Map in Grafana Dashboard , version v0.2.1 (2024)`

For the problem and solution, please refer to the `Problem and Solution.docx` file in the doc folder.

------

### Reference

- Google Map API: https://mapsplatform.google.com/

------

> Last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) at 21/12/2024, if you have any problem or find anu bug, please send me a message .