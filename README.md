
# Openspace office organiser 

## Table of Contents  
- [Description](#description)  
- [Installation](#installation)  
- [Usage](#usage)    
- [Contributors](#contributors)  
- [Files](#files)  

## Description

This repository contains the code to organize people in an open office space with customizable tables.

Details provided by the user:<br/>
<li>Number of tables<br/>
<li>Seats per table<br/>
<li>Employees present for the day<br/>
<li>Wishlist : a list with people needing to sit together (optional)<br/>
<li>Latecomers : needing to be seated at the last minute (optional)<br/>

The program automatically adds tables to the workspace if everyone hasn't been seated with the given number of tables.<br/>
The organisation of the office tables is displayed and also saved in [table_layout.xlsx](./Openspace-office-organiser/data/table_layout.xlsx)

## Installation
The packages required to run the program are saved in requirements.txt<br/>
To install them all run<br/>
```bash
pip install -r requirements.txt
```
## Usage
Add all names to an Excel file and enter the name of the Excel file in the config file<br/>
```bash
python .\main.py
```
Example output:<br/><br/>
![image](https://github.com/user-attachments/assets/e01bce9b-ef3d-4531-9c1d-66ac2511e2d7)

## Contributors
[Dhanya Sunil](https://github.com/dha-code/)<br/>
[Therese Debacker](https://github.com/therese-debacker)

## Files

* [data/](./Openspace-office-organiser/data)
  * [bouman_8.xlsx](./Openspace-office-organiser/data/bouman_8.xlsx)
  * [config.yml](./Openspace-office-organiser/data/config.yml)
  * [latecomers.xlsx](./Openspace-office-organiser/data/latecomers.xlsx)
  * [table_layout.xlsx](./Openspace-office-organiser/data/table_layout.xlsx)
  * [wishlist.xlsx](./Openspace-office-organiser/data/wishlist.xlsx)
* [utils/](./Openspace-office-organiser/utils)
  * [file_utils.py](./Openspace-office-organiser/utils/file_utils.py)
  * [openspace.py](./Openspace-office-organiser/utils/openspace.py)
  * [table.py](./Openspace-office-organiser/utils/table.py)
* [main.py](./Openspace-office-organiser/main.py)
* [requirements.txt](./Openspace-office-organiser/requirements.txt)
