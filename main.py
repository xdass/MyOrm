import sqlite3


class Field:
    def __init__(self):
        print("Field init: ", self)

    def __get__(self, instance, instance_type=None):
        if instance is not None:
            return instance.__data__.get(self.name)
        return self.field

    def __set__(self, instance, value):
        instance.__data__[self.name] = value
        #instance._dirty.add(self.name)
        # if not isinstance(value, str):
        #     raise TypeError("Type Error")
        # setattr(instance, self.__data__[self.name], value)


class CharField(Field):
    def __init__(self):
        Field.__init__(self)


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        meta = class_dict.get('Meta', None)
        meta_options = {}
        if meta:
            for k, v in meta.__dict__.items():
                if not k.startswith('_'):
                    meta_options[k] = v
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = "_" + key
        cls = super().__new__(mcs, name, bases, class_dict)
        cls.__data__ = {}
        cls._meta = meta_options
        return cls


class Model(metaclass=Meta):
    def __init__(self, *args, **kwargs):

        for k, v in kwargs.items():
            setattr(self, k, v)

    def create_table(self):
        print(self._meta)

    def save(self):
        pass


class BetterCustomer(Model):
    id = CharField()
    name = CharField()

    class Meta:
        database = sqlite3.connect('test_db')


d = BetterCustomer(id='123', name='asdd')
print(d.create_table())