###############################################################################
# @brief    Python3 - Function.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.09 - Created.
###############################################################################

'''
Function is a first-class citizen.
'''


def testFunction():
    pass


def printFunction():
    print('Hello World')


def returnFunction():
    return True


def argFunction(_arg):
    return 'Your arg is ' + _arg + '.'


def isNone(_arg):
    if _arg is None:
        print("It's None")
    elif _arg:
        print("It's True")
    else:
        print("It's False")


def multiArgFunction(_arg1, _arg2, _arg3='white'):
    return [_arg1, _arg2, _arg3]


def variableArgFunction(*_args):
    print(_args)


def keywordArgFunction(**_kwargs):
    print(_kwargs)


def docstringFunction():
    '''
    This function prints 'Hello World'.
    '''
    print('Hello World')


def lucky():
    print(7)


def runFunction(_func):
    _func()


def addFunction(_arg1, _arg2):
    print(_arg1 + _arg2)


def runFunctionWithArgs(_func, _arg1, _arg2):
    _func(_arg1, _arg2)


def sumArgFunction(*_args):
    return sum(_args)


def runFunctionWithPositionalArgs(_func, *_args):
    return _func(*_args)


def outerFunction(_arg1, _arg2):
    def innerFunction(_arg3, _arg4):
        return _arg3 + _arg4
    return innerFunction(_arg1, _arg2)


def closureFunction(_name):
    def inner():
        return "My name is '%s'." % _name
    return inner


def lambdaFunction(_words, _func):
    for word in _words:
        print(_func(word))


def decoratorFunction(_func):
    def newFunction(*_args, **_kwargs):
        print('Running function: ', _func.__name__)
        print('Positional arguments: ', _args)
        print('Keyword arguments: ', _kwargs)
        result = _func(*_args, **_kwargs)
        print('Result: ', result)
        return result
    return newFunction


def adder(_arg1, _arg2):
    return _arg1 + _arg2


@decoratorFunction
def subtractor(_arg1, _arg2):
    return _arg1 - _arg2


if __name__ == '__main__':
    # Function ---------------------------------------------------------------#
    print("### Function Study ###")
    testFunction()
    printFunction()
    if returnFunction():
        print("returned")
    print(argFunction('Hi'))
    isNone(None)
    isNone([])
    print(multiArgFunction('red', 'green', 'blue'))
    print(multiArgFunction('purple', _arg3='orange', _arg2='gray'))
    print(multiArgFunction('black', 'navy'))
    variableArgFunction()
    variableArgFunction('a')
    variableArgFunction('a', 'b')
    keywordArgFunction(r='red', g='green', b='blue')
    docstringFunction()
#    help(docstringFunction)
#    print(docstringFunction.__doc__)

    lucky()
    runFunction(lucky)
    addFunction(2, 5)
    runFunctionWithArgs(addFunction, 3, 4)
    print(runFunctionWithPositionalArgs(sumArgFunction, 1, 2, 3, 4))

    print(outerFunction(1, 2))
    h = closureFunction('HoYa')
    print(h())
    weekday = ['mon', 'tue', 'wed', 'thu', 'fri']
    lambdaFunction(weekday, lambda word: word.capitalize() + '!')

    testFunction = decoratorFunction(adder)
    testFunction(2, 5)
    subtractor(5, 3)
