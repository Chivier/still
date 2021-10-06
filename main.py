from clang.cindex import *

def is_function_call(funcdecl, c):
    """ Determine where a call-expression cursor refers to a particular function declaration
    """
    defn = c.get_definition()
    return (defn is not None) and (defn == funcdecl)

def fully_qualified(c):
    """ Retrieve a fully qualified function name (with namespaces)
    """
    res = c.spelling
    c = c.semantic_parent
    while c.kind != CursorKind.TRANSLATION_UNIT:
        res = c.spelling + '::' + res
        c = c.semantic_parent
    return res

def find_funcs_and_calls(tu):
    """ Retrieve lists of function declarations and call expressions in a translation unit
    """
    filename = tu.cursor.spelling
    calls = []
    funcs = []
    for c in tu.cursor.walk_preorder():
        if c.location.file is None:
            pass
        elif c.location.file.name != filename:
            pass
        elif c.kind == CursorKind.CALL_EXPR:
            calls.append(c)
        elif c.kind == CursorKind.FUNCTION_DECL:
            funcs.append(c)
    return funcs, calls

idx = Index.create()
args =  '-x c++ --std=c++11'.split()
tu = idx.parse('tmp.cpp', args=args)
funcs, calls = find_funcs_and_calls(tu)
for f in funcs:
    print(fully_qualified(f), f.location)
    for c in calls:
        if is_function_call(f, c):
            print('-', c.location)
    print()
