import datetime
import os
import xlwt
import decimal
import re

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
    int_col0 = []
    num_col0_remove_zero = []
    date_format = [
        "%d%b%y","%y%m%d","%Y-%m-%d","%d %b %y","%d%m%y"
    ]
    pivot_year = 1969
    panjang = {}
    wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
    ws = None
    date_style = xlwt.easyxf(num_format_str="D-MMM-YY")
    num_style = xlwt.easyxf(num_format_str="#,##0.00")
    percentage_style = xlwt.easyxf(num_format_str="0%")
    num_bold_style = xlwt.easyxf('font: bold true;',num_format_str="#,##0.00")
    percentage_bold_style = xlwt.easyxf('font: bold true;',num_format_str="0%")
    font_style = xlwt.XFStyle()
    font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
    font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
    font_bold_style = xlwt.easyxf('font: bold true;')
    first_line_regex = None
    end_line_regex = None
    first_line_regex_offset = 0
    end_line_regex_offset = 0
    data_regex = None
    raw_lines = []                
    override_raw_lines = []                
    data = []
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
    
    def set_int_col0(self,int_col0):
        self.int_col0 = int_col0

    def auto_width(self):
        panjang = self.panjang
        for k,v in self.panjang.items():
            try:
                self.ws.col(k).width = 256 * ( v + 5 )
            except:
                pass
                
    def write_header(self):
        row_num = 0
        # font_style.font.bold = True
        if self.header:
            for col_num in range(len(self.header)):
                self.ws.write(row_num, col_num, self.header[col_num], self.font_header_style)
    
    def get_raw_lines(self):
        f = open(self.outlist, "r")
        s = 0
        lines = f.readlines()
        panjang = self.panjang
        
        awal = self.firstlinedata or 0
        akhir = len(lines)
        if self.first_line_regex:
            for i,l in enumerate(lines):
                x = re.search(self.first_line_regex,l)
                if x:
                    awal = i + self.first_line_regex_offset
                    break
        
        if self.end_line_regex:
            for i,l in enumerate(lines):
                x = re.search(self.end_line_regex,l)
                if x:
                    akhir = i + self.end_line_regex_offset
                    break
        self.raw_lines = []                
        for i,l in enumerate(lines):
            if i > int(awal) and i < int(akhir) :
                self.raw_lines.append(l)
            # if is_linedata(i,self.firstlinedata,awal,akhir):

    def write_body(self,row=1):
        self.data = []
        panjang = self.panjang
        no = 0
        row = row
        s = 0
        for i,l in enumerate(self.raw_lines):
            d = {}    
            for col,p in enumerate(self.popotongan):
                if col < len(self.popotongan) - 1:
                    style = self.font_style
                    data = l[p:self.popotongan[col+1]].strip()
                    pjg = panjang.get(col,0)
                    if pjg == 0 or len(data) > pjg:
                        panjang.update({col:len(data)})
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
                            if data == '' and col in self.num_col0_remove_zero:
                                data = '' 
                            elif data == '':
                                data = decimal.Decimal(0)
                            else:
                                data = decimal.Decimal(data) 
                            if data == '' and col in self.num_col0_remove_zero:
                                style = self.font_style
                            else:
                                style = self.num_style
                        if col in self.int_col0:
                            data = data.replace(',','')
                            if data == '' :
                                data = int(0) 
                            else:
                                data = int(data) 
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
                    d[col] = data    
            self.data.append(d) 
            row += 1

    def export(self):
        # Sheet header, first row
        self.ws = self.wb.add_sheet('Sheet 1')
        self.write_header()
        if self.override_raw_lines:
            self.raw_lines = self.override_raw_lines
        else:
            self.get_raw_lines()
        self.write_body()
        self.auto_width()
        return self.wb.save(os.path.join(self.MFXLS_DIR, self.filename))

    def export_ws(self,ws):
        self.ws = self.wb.add_sheet(ws)
        self.write_header()
        # if not self.raw_lines:
        if self.override_raw_lines:
            self.raw_lines = self.override_raw_lines
        else:
            self.get_raw_lines()
        self.write_body()
        self.auto_width()

    def save_export(self):
        return self.wb.save(os.path.join(self.MFXLS_DIR, self.filename))