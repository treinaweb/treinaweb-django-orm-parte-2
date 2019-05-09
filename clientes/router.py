
class Router(object):
    def db_for_read(self, models, **hints):
        return 'leitura'

    def db_for_write(self, models, **kints):
        return 'escrita'