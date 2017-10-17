import ConfigParser

cfg = ConfigParser.ConfigParser()

cfg.read('config.ini')

for se in cfg.sections():
    print se
    print cfg.items(se)

cfg.set('userinfo', 'pwd', 'abc')
cfg.set('userinfo', 'email', '123@qq.com')

cfg.remove_option('userinfo', 'email')

for se in cfg.sections():
    print se
    print cfg.items(se)
