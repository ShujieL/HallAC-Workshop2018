import urllib2, json
import subprocess
import sys
import requests # python3 preferred
import mysql.connector
from mysql.connector import errorcode

# -----------------
#  please modify this.
log_user   = ''
log_pswd   = ''
db_user= 'workshop'
db_pswd= ''
db_name= 'workshop'
db_host= 'localhost'
runnum = sys.argv[1]


# -----------------
def read_log(flag):

  author  = "adaq"
  LOGBOOK = "HALOG"
  EFILE   =''

  prefix  =  'https://logbooks.jlab.org/entry/'  # Logbook entry URL prefix
  url     =  'https://logbooks.jlab.org/api/elog/entries'   # Base query url
  url     += "?book="+LOGBOOK                           # specify Logbook
  url     += '&limit=0'                                    # return all entries

  ## Constrain date (default is -180 days. ex. look back ~6 months)
     #$url .= '&startdate=-2 days';
     #$url .= '&enddate=-540 days';
  url       += '&startdate=2017-12-01'  ## 2015-01-01
     #$url .= '&enddate=2016-09-01';   ## 2016-09-01 00:00

  ## Constrain search to a Tag
  if flag   == 'start':
    url     += '&tag=StartOfRun'
    url     += "&title=Start_Run_"+runnum

  elif flag == 'end':
    url     += '&tag= EndOfRun'
    url     += "&title=End_of_Run_"+runnum


  ## Output fields
  url += '&field=attachments'
  url += '&field=lognumber&field=created&field=title'
  url += '&field=body&field=author&field=entrymakers'

  ## Append query fields
  # $url .= "&title=${mode}%20Start_Run_${run}";
  
  url += "&author="+author
  response = requests.get(url,auth=(log_user,log_pswd))
  response = response.json()
  print "==Found run "+flag+" log entry=="
  print prefix+response['data']['entries'][0]['lognumber']
  content =  response['data']['entries'][0]['body']['content']
  content = content.split("\n")
  # print content
  if (flag=='start'):
    content = content[10:]
  # response = requests.get(url)
  # print(response.content)

  return content

def read_var(f, name, delim=":"):
  # ss=f.split("\n")
  ss = f
  # print ss
  ii=0
  for line in ss:

    s = line.strip().split(delim)
    if name in s[0]:#.lower():
      # print s
      if len(s[1])>0:
        return delim.join(s[1:])
      else:
        return ss[ii+1]
    ii+=1

  print name+" not found"
  return -1


# def read_hv(f, detector):
#   LR=['S2m','PRL1','PRL2'] # left and right side
#   try:
#     flag=0
#     lines = [x for x in f if x]
#     i=0
#     for line in lines:
#       i=i+1
#       if 'Detector High Voltage' in line:
#         block=lines[i:]
#         i=0
#         for ll in block:
#           i+=1
#           if ll==detector:
#             index        = block[i].strip().split()
#             set_hv       = block[i+1].strip().split()[3:]
#             read_hv      = block[i+2].strip().split()[3:]
#             current      = block[i+3].strip().split()[2:]
            
#             if detector in LR:
#               index   += block[i+4].strip().split()
#               set_hv  += block[i+5].strip().split()[3:]
#               read_hv += block[i+6].strip().split()[3:]
#               current += block[i+7].strip().split()[2:]

#         return index, set_hv, read_hv, current

#     return 'Error: missing hv info'
#   except:
#     return 'Unexpected Error: check the content'



fstart  =read_log('start')
fend    =read_log('end'  )
# index,set_hv,read_hv,current= read_hv(fend, 'Cherenkov')

start_comment =  read_var(fstart,'comment_text',"=")
end_comment   =  read_var(fend,'End of Run Comment')
run_type      =  read_var(fstart,'Run_type',"=")
target        =  read_var(fstart,'target_type',"=") # whatever shift worker selected
Ebeam         =  read_var(fstart,'Tiefenbach 6GeV Beam energy')

if float(runnum)<90000:
  angle       =  read_var(fstart,'HacL_CalcAngle')
  momentum    =  read_var(fstart,'Left Arm Q1 momentum')
else:
  angle       =  read_var(fstart,'HacR_CalcAngle')
  momentum    =  read_var(fstart,'Right Arm Q1 momentum')

counts        =  read_var(fend,'EVENTS')
time_mins     =  read_var(fend,'TIME')
time_mins     =  time_mins.split()[0]


command_txt   = ( "insert into `runinfo`("  \
+"`run_number`,"\
+"`run_type`,"\
# +"`start_time`,"\
# +"`end_time`," \
+"`time_mins`,"  \
+"`target`,"  \
+"`beam_energy`,"\
+"`momentum`," \
+"`angle`,"\
+"`event_count`," \
+"`note`," \
+"`comment`,"\
+"`end_comment`," \
+"`modify_time`" \
+") values ("\
+runnum +","\
+"'"+run_type+"',"\
+time_mins+","\
+"'"+target+"',"\
+Ebeam+","\
+momentum+","\
+angle+","\
+counts+","\
+"'created from logbook',"
+"'"+start_comment+"',"\
+"'"+end_comment+"',"+"now())"
)

try:
    cnx = mysql.connector.connect(user=db_user,host=db_host,
                                database=db_name, password=db_pswd)
    cursor = cnx.cursor()
    cursor.execute(command_txt)
    cnx.commit()


except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor.close()
  cnx.close()


