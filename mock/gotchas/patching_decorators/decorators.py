def noise_logger(func):
    def wrapped(self):
        result = func(self)
        # In a real-world scenario, the decorator would access an external
        # resource which we don't want our tests to depend on, such as a
        # caching service.
        print "Pet made noise: ", result
        return result
    return wrapped
