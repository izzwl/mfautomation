import datetime
import os
import xlwt
import decimal

class xlsExport(object):
    MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
    MFXLS_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
    outlist = ''
    filename = ''
    header = []
    firstlinedata = 0
    popotongan = []
    date_col0 = []
    text_col0 = []
    num_col0 = []
    date_format = [
        "%d%b%y","%y%m%d","%d %b %y","%d%m%y"
    ]
    pivot_year = 1969
    wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
    ws = wb.add_sheet('Sheet 1')
    date_style = xlwt.easyxf(num_format_str="D-MMM-YY")
    num_style = xlwt.easyxf(num_format_str="#,##0.00")
    font_style = xlwt.XFStyle()
    font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
    font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
    
    def __init__(self,outlist,filename):
        self.outlist = os.path.join(self.MFOUTLIST_DIR,outlist)
        self.filename = filename

    def set_pivot_year(self,pivot_year):
        self.pivot_year = pivot_year

    def set_mfoutlistdir(self,directory):
        self.MFOUTLIST_DIR = directory

    def set_mfxlsdir(self,directory):
        self.MFXLS_DIR = directory

    def set_header(self,header):
        self.header = header

    def set_firstlinedata(self,data):
        self.firstlinedata = data   

    def set_popotongan(self,popotongan):
        self.popotongan = popotongan

    def set_date_format(self,date_format=[]):
        self.date_format = date_format
    
    def set_date_col0(self,date_col0):
        self.date_col0 = date_col0
    
    def set_text_col0(self,text_col0):
        self.text_col0 = text_col0

    def set_num_col0(self,num_col0):
        self.num_col0 = num_col0

    def write_header(self):
        row_num = 0
        # font_style.font.bold = True
        for col_num in range(len(self.header)):
            self.ws.write(row_num, col_num, self.header[col_num], self.font_header_style)
    
    def write_body(self):
        no = 0
        row = 1
        f = open(self.outlist, "r")
        s = 0
        lines = f.readlines()
        for i,l in enumerate(lines):
            if i > self.firstlinedata:
                for col,p in enumerate(self.popotongan):
                    if col < len(self.popotongan) - 1:
                        style = self.font_style
                        data = l[p:self.popotongan[col+1]].strip()
                        try:
                            if col in self.date_col0:
                                for df in self.date_format:
                                    try:
                                        data = datetime.datetime.strptime(data,df) if data else ''
                                        break
                                    except:
                                        pass
                                    
                                try:
                                    if data.year > (self.pivot_year+100):
                                        # print(self.pivot_year)
                                        # data = data.replace(year=data.year-100)
                                        data = datetime.datetime(data.year-100,data.month,data.day)
                                except:
                                    pass
                            
                                style = self.date_style
                            if col in self.text_col0:
                                data = str(data)
                            if col in self.num_col0:
                                data = data.replace(',','')
                                if data == '' :
                                    data = decimal.Decimal(0) 
                                else:
                                    data = decimal.Decimal(data) 
                                style = self.num_style
                        except Exception as e:
                            print(e)
                        cobalagi = 0
                        try:
                            self.ws.write(row, col, data ,style) 
                            cobalagi = 0
                        except:
                            cobalagi = 1
                        if cobalagi:
                            try:
                                self.ws.write(row, col, data.decode('utf8') ,style) 
                                cobalagi = 0
                            except:
                                cobalagi = 1     
                        # print(data)
                row += 1

    def export(self):
        # Sheet header, first row
        self.write_header()
        self.write_body()
        return self.wb.save(os.path.join(self.MFXLS_DIR, self.filename))