def create_function_with_arguments(func,arguments):
    def new_func():
        return func(arguments)
    return new_func
