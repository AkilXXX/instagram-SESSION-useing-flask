#PYTHON code 
#FILE NAME : akil.py
#DESCRIPTION :  Flask , Insatgram Project
#Required libs  : requests, uuid , json ,user_agent 
#* : Telegram : [@Akil828 - @ffffffm] , Github : AKILXXX
#2022/3/20


import requests, uuid , json ,user_agent

def InstaGramLogin(username , password):
    try:
        SsS = {}
        headers = {
           'Host': 'i.instagram.com',
           'Accept': '*/*',
           'Cookie': 'missing',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-IG-Connection-Type': 'WIFI',
           'X-IG-Capabilities': '3brTvw==',
           'User-Agent': 'Instagram 27.0.0.7.97 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)'}
        u = str(uuid.uuid4())                  
        data1 = {
           'uuid': u , 
           'password': password,
           'username': username,            
           'device_id': u , 
           'from_reg': 'false',                
           '_csrftoken': 'missing',                         
           'login_attempt_countn': '0'}                    
        XX = requests.post( 'https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data1)
        print(XX.text)
        if 'bad_password' in XX.text :          
	        SsS['sSs']  = 'bad_password'
	        SsS['X'] = 0
        elif 'challenge_required' in XX.text :
        	SsS['sSs']  = 'challenge_required'
	        SsS['X'] = 0
        elif 'logged_in_user' in XX.text :
        	SsS['sSs']  = 'logged'
	        SsS['X'] = 1
        	SsS['SES'] = XX.cookies['sessionid']		
        	SsS['pk'] = XX.json()['logged_in_user']['pk']
        else :
        	SsS['sSs']  = 'Try Again'
        	SsS['X'] = 0
    except : 
        SsS['sSs']  = 'Try Again'
        SsS['X'] = 0
	    
    return SsS
    