import pandas as pd
import os
from shutil import copyfile

indir='/Users/jeroenhouben/GIT/aagata_fix_csv/data'

exceldir=indir+"/excel"

columns=[(0,15),
(16,56),
(57,60),
(61,65),
(66,74),
(75,105),
(106,115),
(116,124),
(125,134),
(135,144),
(145,154),
(155,163),
(164,173),
(174,183),
(184,193),
(194,202),
(203,212),
(213,222),
(223,229),
(230,236),
(237,243),
(244,250),
(251,252)]

if not os.path.exists(exceldir):
    os.mkdir(exceldir)

for txtfile in os.listdir(indir):
    if txtfile.endswith(".txt") or txtfile.endswith(".TXT"): 
        # remove null
        copyfile(indir+'/'+txtfile,indir+'/'+txtfile+'.ORI')
        fi = open(indir+'/'+txtfile, 'r')
        data = fi.read()
        fi.close()
        
            
        data=data.replace('\x00', '')
        data=data.replace('\x0A\x0A', '\x0A')
        #data = filter(lambda x: not re.match(r'^*$', x), data)
        fo = open(indir+'/'+txtfile, 'w')
        fo.write(data)
        fo.close()
        
for csvfile in os.listdir(indir):
    if csvfile.endswith(".txt") or csvfile.endswith(".TXT"):
        df=pd.read_fwf(indir+'/'+csvfile,columns)
        df=df.fillna(' ')
        excelfile=exceldir +'/'+ os.path.basename(csvfile) + '.xlsx'
        df.to_excel(excelfile, index=False)


