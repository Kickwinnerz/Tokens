import requests
import json

_banner_ = '''
      .o8                         o8o  
     "888                         `"'  
 .oooo888   .ooooo.  oooo    ooo oooo  
d88' `888  d88' `88b  `88.  .8'  `888  
888   888  888ooo888   `88..8'    888  
888   888  888    .o    `888'     888  
`Y8bod88P" `Y8bod8P'     `8'     o888o 
                                       
                                       
                                       
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  +++=== GET TOKEN FACEBOOK ===+++   
 ++== Tools Get Token Facebook ==++
+= No Spam Dettect Server Facebook =+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

# author : Devi
# contact: 03263342276
'''
user=raw_input('username/email: ')
passw=raw_input('password: ')
get = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

up = get.content
pu = json.loads(up)
if "session_key" in up:
    print
    print _banner_
    print 'username:' + pu['identifier']
    print 'token:' + pu["access_token"]
    open(user+'-token.txt', 'a').write(pu["access_token"])
    print
    print 'saved file to '+user+'-token.txt'
else:
    print 'maaf username/password salah'
