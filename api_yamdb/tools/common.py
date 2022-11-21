from django.contrib.auth.tokens import default_token_generator


class DefaultValueFromView:
    """
    Вспомогательный класс для сериализации, извлекает дефолтное значение
    поля из контекста поля.
    """
    requires_context = True

    def __init__(self, context_key):
        self.key = context_key

    def __call__(self, serializer_field):
        if serializer_field.context and serializer_field.context['view']:
            return serializer_field.context.get('view').kwargs.get(self.key)
        raise ValueError('Проверьте контекст поля.')

    def __repr__(self):
        return '%s()' % self.__class__.__name__
