class ParamSwitcher:
    def __init__(self):
        # TODO: implement default parameters
        self.detector =
        self.current = Params();

    def current(self):
        """
        Get current parameters
        """
        return self.current

    def next(self, info):
        """
        Compute new parameters

        Arguments:
            info -- error information from blob detection to better compute
                    next set of parameters (unused for now). schema TBD
        """
        print("NOT IMPLEMENTED")
        return self.current
