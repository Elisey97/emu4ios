wallused=''
last=''
import urllib.request
def search(group):
    check=0
    for i in range(len(group)):
        scan=group[i-4]+group[i-3]+group[i-2]+group[i-1]+group[i]
        if scan=='post-':
            wall=''
            j=1
            while group[i+j]!='"':
                wall+=group[i+j]
                j+=1
            if wall!='id=' and check<=1:
                if check==1 and 'https://vk.com/wall-'+wall!=wallused:
                    last='https://vk.com/wall-'+wall
                    return last
                else:
                    check+=1
                    if check<1:
                        return 'Nothing'
def send(text):
    urllib.request.urlopen('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+str(text))
token=str(input('Токен бота:\n'))
link=str(input('Группа ВК (Например: http://vk.com/emu4ios | https не использовать!):\n'))
chat_id=str(input('ID чата:\n'))
while True:
    group=str(urllib.request.urlopen(link).read())
    text=search(group)
    if text!=None:
        wallused=text
    if text!='Nothing' and str(text)[0]=='h':
        send(text)
