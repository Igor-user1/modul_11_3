import inspect


def introspection_info(obj):

    list_attribute = []
    list_methods = []
    dict_info = {}
    for attribute in dir(obj):
        if callable(getattr(obj, attribute)):
            list_methods.append(attribute)
        else:
            list_attribute.append(attribute)

    dict_info['type'] = type(obj)
    dict_info['attributes'] = list_attribute
    dict_info['methods'] = list_methods
    dict_info['module'] = type(inspect.getmodule(obj))

    return dict_info


a = 4

print(inspect.getmodule(a))
print(introspection_info(a))
