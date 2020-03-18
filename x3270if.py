import datetime
import subprocess,sys

def conv_date(date):
    command = "date -d "+date+" +%Y-%m-%d"
    if date:
	try:
            return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].strip()
        except:
    	    return ''
    else:
        return ''

def conv_date_py(date):
    try:
        result = datetime.datetime.strptime(date,"%d%b%y")
        return result
    except:
        return None

def enter(port):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" 'enter()' ; wait",shell=True).wait()
        print("%s Enter Success" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print("%s Enter Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("GAGAL")

def tab(port):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" 'tab()' ; wait",shell=True).wait()
        print("%s Tab Success" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print("%s Tab Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("GAGAL")

def pf(port,i):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" 'pf("+str(i)+")' ; wait",shell=True).wait()
        print("%s PF%s key Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(i)))
    except Exception as e:
        print("%s PF%s key Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(i),str(e)))
        return sys.exit("GAGAL")

def string(port,string):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" \"string(\\\""+string+"\\\")\" ; wait",shell=True).wait()
        print("%s String %s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(string)))
    except Exception as e:
        print("%s String %s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(string),str(e)))
        return sys.exit("GAGAL")

def movecursor(port,r,c):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" 'movecursor("+str(r)+","+str(c)+")' ; wait",shell=True).wait()
        print("%s Movecursor %s,%s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(r),str(c)))
    except Exception as e:
        print("%s Movecursor %s,%s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(r),str(c),str(e)))
        return sys.exit("GAGAL")

def transfer(port,filename):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" \"transfer(hostfile=mpmcs99.transfer,localfile="+filename+",exist=replace)\" ; wait",shell=True).wait()
        print("%s Transfer %s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename)))
    except Exception as e:
        print("%s Transfer %s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename),str(e)))
        return sys.exit("GAGAL")

def upload(port,dataset,filename):
    try:
        subprocess.Popen("x3270if -t "+ str(port) +" \"transfer(direction=send,hostfile="+dataset+",localfile="+filename+")\" ; wait",shell=True).wait()
        print("%s Upload %s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename)))
    except Exception as e:
        print("%s Upload %s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename),str(e)))
        return sys.exit("GAGAL")

def cek_konek(port):
    try:
        result = subprocess.Popen("x3270if -t 6000 'ascii()'|grep -i TSO",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
        print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    except Exception as e:
        print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("GAGAL")

    if result[0]:
        print("Connected")
    else:
        return sys.exit("Not Connected")

def cek_logon(port):
    try:
        result = subprocess.Popen("x3270if -t "+ str(port) +" 'ascii()'|grep rejected",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
        print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    except Exception as e:
        print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("GAGAL")

    if result[0]:
      subprocess.Popen("x3270if -t "+ str(port) +" 'disconnect()' ; wait",shell=True).wait()
      return sys.exit("USER Already logon")

def job_info(port):
    try:
        job_info = subprocess.Popen("x3270if -t "+ str(port) +" 'ascii()'|grep SUBMITTED",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
        print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return job_info[0][job_info[0].find("(")+1:job_info[0].find(")")]
    except Exception as e:
        print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("JOB INFO not Found")

def job_result(port,job):
    try:
        jobresult = subprocess.Popen("x3270if -t "+ str(port) +" 'ascii()'|grep "+job,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
        print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return jobresult
    except Exception as e:
        print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("JOB Result Failed")

def sd_h_row(port,job):
    try:
        result = subprocess.Popen("x3270if -t "+ str(port) +" 'ascii()'|grep -n -m1 "+job+"|cut -d \":\" -f1",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
        print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return result
    except Exception as e:
        print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
        return sys.exit("HELD JOB Not Found")
