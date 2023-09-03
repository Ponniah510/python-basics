#return type in python
#we have an usname and password and get input for uname and password from func and check uname and password same or not
set_s_username="EMC"
s_password="123"
def validate():
    a=str(input())
    b=str(input())
    if(a==set_s_username or b==s_password):
        return True
    else:
        return False
c=validate()
print(c)