import inspect


def introspection_info(obj):

    list_attribute = []
    list_methods = []
    dir_list = dir(obj)
    for attribute in dir_list:
        if callable(getattr(obj, attribute)):
            list_methods.append(attribute)
        else:
            list_attribute.append(attribute)
    return dict([('type', str(type(obj))[8:-2]),
                 ('attributes', list_attribute), ('methods', list_methods), ('modul', inspect.getmodule(obj))])


a = 4

print(introspection_info(a))
