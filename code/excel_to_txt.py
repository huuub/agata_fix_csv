import pandas as pd
import os as os

headerfile='/Users/jeroenhouben/GIT/aagata_fix_csv/code/header'
indir='/Users/jeroenhouben/GIT/aagata_fix_csv/data'
exceldir=indir+"/excel"

for excelfile in os.listdir(exceldir):
    if excelfile.endswith(".xlsx"):
        csvfile=excelfile + '.csv'
        df = pd.read_excel(exceldir+'/'+excelfile,index_col=None)
        dfr=df[1:]
       
        dfr.iloc[:,0]=dfr.iloc[:,0].astype(str).str.ljust(15,' ')
        dfr.iloc[:,1]=dfr.iloc[:,1].astype(str).str.ljust(40,' ')
        dfr.iloc[:,2]=dfr.iloc[:,2].astype(str).str.ljust(3,' ')
        dfr.iloc[:,3]=dfr.iloc[:,3].astype(str).str.ljust(4,' ')
        dfr.iloc[:,4]=dfr.iloc[:,4].astype(str).str.ljust(8,' ')
        dfr.iloc[:,5]=dfr.iloc[:,5].astype(str).str.ljust(30,' ')
        dfr.iloc[:,6]=dfr.iloc[:,6].astype(str).str.rjust(9,' ')
        dfr.iloc[:,7]=dfr.iloc[:,7].astype(str).str.rjust(8,' ')
        dfr.iloc[:,8]=dfr.iloc[:,8].astype(str).str.rjust(9,' ')
        dfr.iloc[:,9]=dfr.iloc[:,9].astype(str).str.rjust(9,' ')
        dfr.iloc[:,10]=dfr.iloc[:,10].astype(str).str.rjust(9,' ')
        dfr.iloc[:,11]=dfr.iloc[:,11].astype(str).str.rjust(8,' ')
        dfr.iloc[:,12]=dfr.iloc[:,12].astype(str).str.rjust(9,' ')
        dfr.iloc[:,13]=dfr.iloc[:,13].astype(str).str.rjust(9,' ')
        dfr.iloc[:,14]=dfr.iloc[:,14].astype(str).str.rjust(9,' ')
        dfr.iloc[:,15]=dfr.iloc[:,15].astype(str).str.rjust(8,' ')
        dfr.iloc[:,16]=dfr.iloc[:,16].astype(str).str.rjust(9,' ')
        dfr.iloc[:,17]=dfr.iloc[:,17].astype(str).str.rjust(9,' ')
        dfr.iloc[:,18]=dfr.iloc[:,18].astype(str).str.rjust(6,' ')
        dfr.iloc[:,19]=dfr.iloc[:,19].astype(str).str.rjust(6,' ')
        dfr.iloc[:,20]=dfr.iloc[:,20].astype(str).str.rjust(6,' ')
        dfr.iloc[:,21]=dfr.iloc[:,21].astype(str).str.rjust(6,' ')
        dfr.iloc[:,22]=dfr.iloc[:,22].astype(str).str.rjust(1,' ')
        
        dfr.to_csv(exceldir+'/'+csvfile,sep='|',index=False, header=False)
        
        fi = open(exceldir+'/'+csvfile, 'r')
        data = fi.read()
        fi.close()          
        data=data.replace('|', ' ')
        data=data.replace('\n', ' \n')
        # for line in data.splitlines():

        #add header
        fh = open(headerfile, 'r')
        header= fh.read()
        data= header + data
        fh.close()
	
        fo = open(exceldir+'/'+csvfile, 'w')
        fo.write(data)
        fo.close()

