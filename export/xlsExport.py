import datetime
import os
import xlwt
import decimal

class xlsExport(object):
    MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
    MFXLS_DIR = os.path.join(os.path.expanduser("~"),'mfxls')
    outlist = ''
    filename = ''
    header = []
    firstlinedata = 0
    popotongan = []
    date_col0 = []
    num_col0 = []
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

    def set_date_col0(self,date_col0):
        self.date_col0 = date_col0

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
                        if col in self.date_col0:
                            data = datetime.datetime.strptime(data,"%d%b%y") if data else ''
                            style = self.date_style
                        if col in self.num_col0:
                            data = data.replace(',','')
                            if data == '' :
                                data = decimal.Decimal(0) 
                            else:
                                data = decimal.Decimal(data) 
                            style = self.num_style
                        self.ws.write(row, col, data ,style) 
                row += 1

    def export(self):
        # Sheet header, first row
        self.write_header()
        self.write_body()
        return self.wb.save(os.path.join(self.MFXLS_DIR, self.filename))