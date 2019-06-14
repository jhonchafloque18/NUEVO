from django.conf import settings


class DesarroolloRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'oper_campo':
            return 'ins_desarrollo'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'oper_campo':
            return 'ins_desarrollo'
        return None
