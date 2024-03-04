class Router(object):
    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'ArticleOtherDB':
            return 'other'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'ArticleOtherDB':
            return 'other'
        return 'default'
