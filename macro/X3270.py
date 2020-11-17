import datetime
import subprocess,sys

class X3270():
    host = ''
    port = ''
    tso_user = ''
    tso_pass = ''
    filename = ''
    jcl = ''
    _job_info = ''
    _job_result = ''
    _result = ''
    _row = ''
    jcl_class = ''
    jcl_user = ''
    jcl_param = ''
    detail = ''
    scroll = 0

    def __init__(self,host,port,tso_user,filename,jcl):
        self.host = host
        self.port = str(port)
        self.tso_user = tso_user
        self.filename = filename
        self.jcl = jcl
        self.tso_pass = {
            'MPMCS99':'',
            'MPMCS98':'',
            'MPMCS32':'bismilah',
        }.get(self.tso_user.upper(),'')
    
    def set_param(self,jcl_class, jcl_user, jcl_param, detail):
        self.jcl_class = jcl_class
        self.jcl_user = jcl_user
        self.jcl_param = jcl_param
        self.detail = detail

    def conv_date(self,date):
        command = "date -d "+date+" +%Y-%m-%d"
        if date:
            try:
                return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].strip()
            except:
                return ''
        else:
            return ''

    def conv_date_py(self,date):
        try:
            result = datetime.datetime.strptime(date,"%d%b%y")
            return result
        except:
            return None

    def enter(self):
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" 'enter()' ; wait",shell=True).wait()
            print("%s Enter Success" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return self
        except Exception as e:
            print("%s Enter Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("GAGAL")

    def tab(self):
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" 'tab()' ; wait",shell=True).wait()
            print("%s Tab Success" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return self
        except Exception as e:
            print("%s Tab Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("GAGAL")

    def pf(self,i):
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" 'pf("+str(i)+")' ; wait",shell=True).wait()
            print("%s PF%s key Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(i)))
            return self
        except Exception as e:
            print("%s PF%s key Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(i),str(e)))
            return sys.exit("GAGAL")

    def string(self,string):
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" \"string(\\\""+string+"\\\")\" ; wait",shell=True).wait()
            print("%s String %s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(string)))
            return self
        except Exception as e:
            print("%s String %s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(string),str(e)))
            return sys.exit("GAGAL")

    def movecursor(self,r,c):
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" 'movecursor("+str(r)+","+str(c)+")' ; wait",shell=True).wait()
            print("%s Movecursor %s,%s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(r),str(c)))
            return self
        except Exception as e:
            print("%s Movecursor %s,%s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(r),str(c),str(e)))
            return sys.exit("GAGAL")

    def transfer(self,filename=None):
        filename = filename or self.filename
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" \"transfer(hostfile="+ self.tso_user +".transfer,localfile="+filename+",exist=replace)\" ; wait",shell=True).wait()
            print("%s Transfer %s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename)))
            return self
        except Exception as e:
            print("%s Transfer %s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename),str(e)))
            return sys.exit("GAGAL")

    def upload(self,dataset,filename=None):
        filename = filename or self.filename
        try:
            subprocess.Popen("x3270if -t "+ str(self.port) +" \"transfer(direction=send,hostfile="+dataset+",localfile="+filename+")\" ; wait",shell=True).wait()
            print("%s Upload %s Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename)))
            return self
        except Exception as e:
            print("%s Upload %s Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(filename),str(e)))
            return sys.exit("GAGAL")

    def s_tso(self):
        return self.string('TSO '+self.tso_user)
    
    def s_jcl(self):
        return self.string(self.jcl)
    
    def s_p2(self):
        return self.string('P.2')
    
    def s_sdh(self):
        return self.string('SD.H')
    
    def s_res(self):
        return self.string('RES')
    
    def s_sub(self):
        return self.string('SUB')
    
    def s_user(self):
        return self.string(self.tso_user)
    
    def s_juser(self):
        if self.host == 'hercules':
            return self.string(self.tso_user + "                   ")
        elif self.host == 'mainframe':
            return self.string(self.tso_user)
    
    def s_jclear(self):
        return self.string("/\$P JQ,JM=%s*"%self.tso_user)
    
    def s_data_transfer(self):
        return self.string("%s.TRANSFER"%self.tso_user)
    
    def s_remove_hex(self):
        return self.string("c x'00' ' ' all")    
    
    def cek_konek(self):
        try:
            result = subprocess.Popen("x3270if -t "+ str(self.port) +" 'ascii()'|grep -i TSO",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        except Exception as e:
            print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("GAGAL")

        if result[0]:
            print("Connected")
            return self
        else:
            return sys.exit("Not Connected")

    def cek_logon(self):
        try:
            result = subprocess.Popen("x3270if -t "+ str(self.port) +" 'ascii()'|grep rejected",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            return self
        except Exception as e:
            print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("GAGAL")

        if result[0]:
            subprocess.Popen("x3270if -t "+ str(self.port) +" 'disconnect()' ; wait",shell=True).wait()
            return self
        return sys.exit("USER Already logon")

    def job_info(self):
        try:
            job_info = subprocess.Popen("x3270if -t "+ str(self.port) +" 'ascii()'|grep SUBMITTED",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            self._job_info = job_info[0][job_info[0].find("(")+1:job_info[0].find(")")]
            return self
        except Exception as e:
            print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("JOB INFO not Found")

    def get_job_result(self,job=None):
        job = job or self._job_info
        try:
            self._job_result = subprocess.Popen("x3270if -t "+ str(self.port) +" 'ascii()'|grep "+job,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            return self._job_result
        except Exception as e:
            print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("JOB Result Failed")

    def get_sdh_row(self,job=None,row=None):
        job = job if job else self._job_info
        row = row if row else self.jcl_param.get('row_detail',1)
        print(job)
        print(self.jcl_param.get('row_detail',1))
        try:
            rows = subprocess.Popen("x3270if -t "+ str(self.port) +" 'ascii()'|grep -n -m2 "+job+"|cut -d \":\" -f1",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
            print("%s ascii Success" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            # row = int(rows[0])-1
            # row_list =[ x for x in [ int(i)-1 for i in rows[0] if i.replace('\n','').isdigit() ] if x > 0 ]
            row_list = []
            for r in rows[0].split('\n'):
                if r.isdigit():
                    row_list.append(int(r)-1)
            
            self._result = row_list[row-1]
            print (row_list)
            print (row_list[row-1])

            return self._result
        except Exception as e:
            print("%s ascii Failed : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(e)))
            return sys.exit("HELD JOB Not Found")
    
    def sleep(self,s):
        try:
            subprocess.Popen("sleep %s"%str(s),shell=True).wait()
            return self
        except:
            return sys.exit("Command sleep failed")

    def wait_job(self,job=None):
        job = job or self._job_info
        limit = 3*60*60
        start = datetime.datetime.now()
        while True:
            self.enter()
            result = self.get_job_result(job)
            print(result)
            end = datetime.datetime.now()
            if int((end - start).seconds) > limit:
                return sys.exit("wait job reach limit")
            if result[0]:
                break
            subprocess.Popen("sleep 2",shell=True).wait()

        rc_code = result[0].find("MAXCC=0")
        if rc_code > 1:
            print(result[0])
            return self
        else:
            return sys.exit(result[0])

    
    
    def xdc(self):
        detail = self.detail
        mf = self.enter().enter().pf(3).pf(3).pf(3).s_sdh().enter()
        row = self.get_sdh_row()
        mf = mf.movecursor(row,1)
        for d in detail:
            print(d)
            mf = mf.string("?").enter()
            row = self.get_sdh_row(d,1)
            mf = mf.movecursor(row,1)
        mf = mf.string('XDC').enter().enter()
        for d in detail:
            mf = mf.pf(3)
        mf = mf.movecursor(23,20)
        return mf

    def handle(self):
        jcl_class = self.jcl_class
        jcl_user = self.jcl_user
        jcl_param = self.jcl_param
        detail = self.detail
        mf = self.cek_konek()
        mf = mf.s_tso().enter().sleep(5).string(self.tso_pass).enter().sleep(10).enter().enter().enter().cek_logon()
        mf = mf.s_p2().enter().tab().s_jcl().enter().s_res().enter()
        mf = mf.movecursor(*jcl_class['xy']).s_user().string(jcl_class['val'])
        mf = mf.movecursor(*jcl_user['xy']).s_juser()
        # scroll
        for i in range(0,jcl_param.get('scroll',0)):
            mf = mf.movecursor(3,14).pf(8)
        mf = mf.movecursor(*jcl_param['xy']).string(jcl_param['val'])
        mf = mf.movecursor(3,14).s_sub().enter()
        mf = mf.job_info().wait_job().xdc()
        mf = mf.s_jclear().enter().enter().enter().pf(3).pf(3)
        mf = mf.s_p2().enter().tab().s_data_transfer().enter()
        mf = mf.s_res().enter().s_remove_hex().enter().pf(3).pf(3)
        mf = mf.string("6").enter().transfer().pf(3).pf(3).pf(3)
        mf = mf.string("2").enter().string("logoff").enter().sleep(5)
        return "ALHAMDULILLAH"