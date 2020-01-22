import mechanize

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
response = br.open("[link]")

    user = "user"
password = "pw"
for i in range(10000):
    print(user + format(i, '04'))
    br.select_form("LoginActionForm")
    br.form['login'] = user + format(i, '04')
    br.form['password'] = password

    response = br.submit()
