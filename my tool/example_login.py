import bottle


def check_login(username, password):
    if username == '123' and password == '234':
        return True
    else:
        return False


@bottle.route('/login')
def login():
    return ''' <form action="/login" method="post">
                 Username: <input name="username" type="text" />
                 Password: <input name="password" type="password" />
                 <input value="Login" type="submit">
               </form>
            '''


@bottle.route('/login', method='POST')
def do_login():
    # 第一种方式
    #   username = request.forms.get('username')
    #   password = request.forms.get('password')

    # 第二种方式
    postValue = bottle.request.POST.decode('utf-8')
    username = bottle.request.POST.get('username')
    password = bottle.request.POST.get('password')

    if check_login(username, password):
        return "<p> Your login information was correct.</p>"
    else:
        return "<p>Login failed. </p>"


bottle.run(host='localhost', port=8083)

