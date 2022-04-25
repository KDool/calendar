from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import pandas as pd
import os
from datetime import date,datetime

class MyLibrary:
    """Give this library a proper name and document it."""

    def example_python_keyword(self):
        logger.info("This is Python!")

    def readFile(self):
        path = self.FileLocation()
        if path == '':
            path = os.getcwd()
        file = pd.read_excel(path,sheet_name='Sheet1',skiprows=[0],usecols="A,B,C")
        file.rename(columns = {'Unnamed: 0' : 'STT','SÁNG':'AM','CHIỀU':'PM'}, inplace = True)
        range_len = len(file)

        for i in range(range_len):
            # print(file.loc[i,'STT'])
            if pd.isnull(file['STT'].iloc[i]):
                file.at[i,'STT'] = file.loc[i-1,'STT']
        file = file.dropna(subset=['AM','PM'],how='all')
        df1 = file[['STT','AM']].dropna(subset=['AM'],how='all')
        df2 = file[['STT','PM']].dropna(subset=['PM'],how='all')
        df1.rename(columns = {'AM':'infor'}, inplace = True)
        df2.rename(columns = {'PM':'infor'}, inplace = True)
        df = pd.concat([df1,df2],axis=0)
        df = df.reset_index(drop=True)
        print(df)
        list_infor = self.extractData(df)
        # print(list_infor)
        return list_infor

    def extractData(self,df: pd.DataFrame):
        num_events = int(len(df)/2)
        print(num_events)
        
        total_list = []

        for i in range(num_events):
            print(i)
            date = ''
            time = ''
            title = ''
            location = ''
            des = ''

            date = self.extract_date(df,i*2)
            time,title =  self.extract_f1(df,i*2)
            location,des = self.extract_f2(df,i*2+1)
            list_info = [date,time,title,location,des]
            total_list.append(list_info)
        return total_list


    def extract_f1(self,df,i):
        text = df['infor'].iloc[i]
        a,time,title = text.split(':',2)
        time = a +':'+ time
        title = title.strip()

        return time,title

    def extract_f2(self,df,i):
        text = df['infor'].iloc[i]
        location,des = text.split('\n',1)
        s1,location = location.split(':',1)
        return location.strip(),des

    def extract_date(self,df,i):
        s = df['STT'].iloc[i]
        res = s[s.find('(')+1:s.find(')')]
        current_year = str(date.today().year)
        day,month = res.split('/',1)
 
        datetime_object = datetime.strptime(month, "%m")
        month_name = datetime_object.strftime("%b")

        res = month_name + ' ' + day + ', ' + current_year
        return res
    
    def FileLocation(self,path='.\FileCalendarLocation.txt'):
        with open(path, 'r') as f:
            first_line = f.readline()
        
        txt= first_line.split("=",1)[1]
        return txt