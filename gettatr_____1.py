class MyClass:
    def __init__(self, data):
        self.data = data

    def __getattr__(self, name):
        if name.startswith('get_'):
            try:
                key = name[4:]
                return self.data[key]
            except KeyError:
                raise AttributeError(f'No such attribute: {name}')
            else:
                raise AttributeError(f'No such attrbute: {name}')

obj = MyClass({'a':1, 'b':2})
print(obj.get_a)
print(obj.get_b)
        
        
