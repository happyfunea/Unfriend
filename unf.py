#!/usr/bin/python2.7.x
#-*-coding:utf-8-*-
try:
    import json
    from colorama import Fore
except ImportError as er:
    print (er)
    os.system('pip2 install colorama')
try:
    from requests import get, post, session
    import sys, re, logging as log
    import subprocess as sub
    from time import sleep as turu
    from getpass import getpass
except ImportError as a:
    print 'Module Error : {}'.format(a);sys.exit()
def _x_():
    print '''
     fungsi tools: untuk menghapus daftar teman lu(BY MARK)
     version: (BETA)
     author: Agung
     info!: gunakan dengan bijak takut di begal akaun lu ama (MARK)
    '''
class color:
    green = Fore.LIGHTGREEN_EX
    red = Fore.LIGHTRED_EX
    yellow = Fore.LIGHTYELLOW_EX
    withe = Fore.WHITE
class leaf:
    count = 0
    url = ['https://free.facebook.com/login/?ref=dbl&fl&refid=8']
    def __init__(self):
        self.nick = raw_input(color.red+'('+color.yellow+'Username/Email'+color.red+')'+color.withe+' : ')
        self.pw = getpass(prompt=color.red+'('+color.yellow+'Password'+color.red+')'+color.withe+' : ')
        try:
            self.login()
        except:
            pass
    def login(self):
        self.s = session()
        self.pos = {'email':self.nick,
                    'pass':self.pw,
                    'login':'masuk'}
        self.get = self.s.post(leaf.url[0], data = self.pos)
        try:
            self.getid = get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={0}&locale=en_US&password={1}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(self.nick, self.pw)).text
            self.js = json.loads(self.getid)
            self.token = self.js['access_token']
            self.friend = get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token={}'.format(self.token)).text
            self.fj = json.loads(self.friend)
            self.saved = open('idlist.txt','w')
            for c in self.fj['friends']['data']:
                try:
                    self.saved.write(c['id']+'\n')
                except KeyError:
                    continue
            log.warning(' Mengambil Id Success!')
            self.saved.close
        except KeyError:
            log.error(' Akun Terkena Checkpoint');sys.exit()
        if 'home.php' in self.get.url:
            log.warning(' Login Success!')
            self.findnick = re.findall(r'>Keluar (.*?)</a>', self.get.content)
            print '(INFO): Welcome {}'.format(self.findnick[0])
            print '(INFO): Membuka https://free.facebook.com'
        elif 'checkpoint' in self.get.url:
            log.error(' Akun Terkena Checkpoint');sys.exit
        else:
            log.error(' Gagal Login...');sys.exit()
        try:
            self.ex()
        except Exception as bebeb:
            print (bebeb)
            sys.exit()
    def ex(self):
        self.ask = raw_input('(Tekan Enter Ea Untuk Melanjutkan)')
        self.op = open('idlist.txt', 'r').readlines()
        log.warning(color.withe+'Total List ID : {}'.format(len(self.op)))
        for c in self.op:
            try:
                leaf.count+=1
                self.x = c.strip()
                self.url = 'https://free.facebook.com/removefriend.php?friend_id='+self.x+'&unref=profile_gear&ref=dbl'
                self.ambil = self.s.get(self.url).text
                self.bacd = re.findall(r'value="(.*?)"', self.ambil)
                self.param = {'fb_dtsg':self.bacd[4],
                              'jazoest':self.bacd[5],
                              'friend_id':self.bacd[6],
                              'unref':'None',
                              'confirm':'Konfirmasi'}
                self._fck_ = self.s.post('https://free.facebook.com/a/removefriend.php', data = self.param)
                if 'Anda tidak lagi berteman dengan' in self._fck_.content:
                    print leaf.count,'.','(INFO): Unfriend Success!|{}'.format(self.x);turu(3)
                else:
                    log.error(' (GAGAL): {}'.format(self.x));continue
            except KeyboardInterrupt:
                log.warning(' [!]Stopped!');sys.exit()

if __name__=='__main__':
    sub.call('clear', shell=True)
    print 'INFO: Jika Sudah Cukup Harap Tekan CTRL+C\nDi Karenakan Jika Terlalu banyak Unfriend Maka (MARK) Curiga'
    leaf()
    inp = raw_input('(a)bout&Exit(OR)(e)xit: ')
    if inp == 'a' or inp == 'A':
       _x_();turu(4)
    elif inp == 'e' or inp == 'E':
       log.error(' (Exiting)!');sys.exit()
