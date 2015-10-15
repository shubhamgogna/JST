class Symbol(object):
    def __init__(self, name, identifier='', type=None):
        self.name = name
        self.__type = ''  # int, float, etc.
        self.__identifier = identifier
        self.__pointer_count = 0
        self.__array_dim_count = 0
        self.__array_dims = []
        self.__storage_specifiers = []  # auto, static, extern, etc.
        self.__type_qualifier = None    # const, volatile

    def __repr__(self):
        return self.__type + (self.__pointer_count * '*') + self.__identifier
        # TODO: add arrays and args


class FunctionSymbol(Symbol):
    def __int__(self, identifier, type=None):
        super(FunctionSymbol, self).__init__(identifier, type)
        self.arguments = []


class ConstantSymbol(Symbol):
    def __int__(self, identifier, value, type=None):
        super(ConstantSymbol, self).__init__(identifier, type)
        self.value = value