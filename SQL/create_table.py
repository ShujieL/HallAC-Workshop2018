from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


# ---------------
# please midify
# --------------
user = ''
pswd = ''

#--------------------
TABLES = {}
TABLES['runinfo'] = (
    "CREATE TABLE `runinfo` ("
    "`run_number` int(10) unsigned NOT NULL,"
    "`run_type` tinytext,"
    "`start_time` datetime DEFAULT NULL,"
    "`end_time` datetime DEFAULT NULL,"
    "`time_mins` float(8,3) DEFAULT NULL,"
    "`note` text NOT NULL DEFAULT NULL,"
    "`target` tinytext,"
    "`beam_energy` float(10,3) DEFAULT NULL,"
    "`momentum` float(10,4) DEFAULT NULL,"
    "`angle` float(8,3) DEFAULT NULL,"
    "`charge` float(10,2) DEFAULT NULL,"
    "`event_count` int(10) unsigned DEFAULT NULL,"
    "`raster_x` float(3,2) DEFAULT NULL,"
    "`raster_y` float(3,2) DEFAULT NULL,"
    "`prescale_T1` int(10) unsigned DEFAULT NULL,"
    "`prescale_T2` int(10) unsigned DEFAULT NULL,"
    "`prescale_T3` int(10) unsigned DEFAULT NULL,"
    "`prescale_T4` int(10) unsigned DEFAULT NULL,"
    "`prescale_T5` int(10) unsigned DEFAULT NULL,"
    "`prescale_T6` int(10) unsigned DEFAULT NULL,"
    "`prescale_T7` int(10) unsigned DEFAULT NULL,"
    "`prescale_T8` int(10) unsigned DEFAULT NULL,"
    "`T1_count` int(10) DEFAULT NULL,"
    "`T2_count` int(10) DEFAULT NULL,"
    "`T3_count` int(10) DEFAULT NULL,"
    "`T4_count` int(10) DEFAULT NULL,"
    "`T5_count` int(10) DEFAULT NULL,"
    "`T6_count` int(10) DEFAULT NULL,"
    "`T7_count` int(10) DEFAULT NULL,"
    "`T8_count` int(10) DEFAULT NULL,"
    "`comment` text,"
    "`end_comment` text,"
    "`modify_time` datetime DEFAULT NULL,"
    "PRIMARY KEY (`run_number`)"
    ") ENGINE=InnoDB")

TABLES['cerL'] = (
    "CREATE TABLE `cerL` ("
    "`run_number` int(10) unsigned NOT NULL,"
    "`pmt_id` smallint(6) NOT NULL,"
    "`pedestal` float(8,3) NOT NULL,"
    "`gain` float(8,3) NOT NULL,"
    "PRIMARY KEY (`run_number`,`pmt_id`)"
    ") ENGINE=InnoDB")



try:
    cnx = mysql.connector.connect(user=user,host='localhost',
                                database='workshop', password=pswd)
    cursor = cnx.cursor()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
# else:
  # cnx.close()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)



for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else: 
            print(err.msg)
    else:
        print("OK")

# action = "ALTER TABLE cerL ADD COLUMN HV float(10,3) NOT NULL;"
# cursor.execute(action)
cursor.close()
cnx.close()