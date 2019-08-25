
def print_msg(*msg,sign='=',num=50):
    msg_num=len(msg)
    sign=sign*num
    s='~'
    s_num=int(num*1.2)
    s=s*s_num
    print('\n{}'.format(sign))
    if msg_num==1:
        for i in msg:
            one_msg='{}'.format(i)
            print(one_msg)
    elif msg_num>1:
        for i in msg:
            one_msg='{}'.format(i)
            print(one_msg)
            if i!=msg[-1]:
                print(s)
    print('{}'.format(sign))
# print_msg('da的',1,[1,2],(21,21),{1:'21'})
#拼接url
def url_join(*args):
    seq='/'
    url=''
    for i in args:
        i=str(i)
        url=url+i+'/'
    if url[-1]=='/':
        url=url[:-1]
    return url