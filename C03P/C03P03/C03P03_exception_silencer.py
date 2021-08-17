class ExceptionSilencer:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exception_type, *args, **kwargs):
        if exception_type is self.exception:
            return 'Exception silenced'


# with ExceptionSilencer(ValueError):
#     int('aa')
#
# print("We can reach this point, because the exception was not propagated")

# with ExceptionSilencer(KeyError):
#     int("aa")
#
# print("We cannot reach this point, because the exception was propagated")
