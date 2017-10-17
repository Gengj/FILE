import os
import os.path
import ConfigParser


# --------------
# 1:dump ini
# 2:del section
# 3:del item
# 4:modify item
# 5:add section
# 6:save modify
# --------------

class student_info(object):
    def __init__(self, recordfile):
        self.logfile = recordfile
        self.cfg = ConfigParser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        sectionlst = self.cfg.sections()
        print '--------------------------'
        for se in sectionlst:
            print se
            print self.cfg.items(se)
        print '--------------------------'

    def delete_item(self, section, key):
        self.cfg.remove_section(section, key)

    def delete_section(self, section):
        self.cfg.remove_section(section)

    def add_section(self, section):
        self.cfg.add_section(section)

    def set_item(self, section, key, value):
        self.cfg.set(section, key, value)

    def save(self):
        f = open(self.logfile, 'w')
        self.cfg.write(f)
        f.close()


if __name__ == '__main__':
    info = student_info('config.ini')
    info.cfg_load()
    info.cfg_dump()
    # --------------------
    info.set_item('userinfo', 'pwd', 'qw1212312')
    info.set_item('study', 'macOS', '15')
    info.cfg_dump()
    # --------------------
    info.delete_section('life')
    info.delete_section('live')
    info.cfg_dump()

    # info.cfg.add_section()

    info.add_section('money')
    info.cfg_dump()
    # --------------------
    # info.cfg_dump()
    # --------------------
    info.add_section('finan')
    info.save()
