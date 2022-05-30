import ParamSwitcher from 'param_switcher'

class ParamManager:
    def __init__(self):
        self.switcher = ParamSwitcher()

    def current(self):
        """
        Get current set of parameters from switcher
        """
        return self.switcher.current_detector()

    def next(self, info):
        """
        Iterate to next set of parameters from switcher (in place)
        then return them

        Arguments:
            info -- error information from blob detection to better compute
                    next set of parameters (unused for now). schema TBD
        """
        return self.switcher.next_detector(info)

    def save(self):
        """
        Iterate to next set of parameters from switcher (in place)
        then return them

        Arguments:
            info -- error information from blob detection to better compute
                    next set of parameters (unused for now). schema TBD
        """
        self.switcher.save()

    # Need to fit in API here
