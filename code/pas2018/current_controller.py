#!/usr/bin/env python3
'''Current controller for PAS20-18 combined with DFR DAC'''
import numpy as np
from time import sleep
from argparse import ArgumentParser
from .dac import DAC


class CurrentController:
    '''Current controller.'''
    def __init__(self, current_max=18.0):
        self._current_max = current_max
        self._dac = DAC()

    def set_current(self, current):
        '''Set current limit to the power supply.

        Parameter
        ---------
        current : float
            Current in A.
        '''
        self._dac.set_voltage(current/self._current_max*10)

    def ramp_from_to(self, from_current, to_current, step=0.1, wait=0.0):
        '''Ramp up/down to given target current.
        
        Parameters
        ---------
        from_current : float
            Inital value of the current in A.
        to_current : float
            Target value of the current in A.
        step : float, optional
            Step value in A. Default to 0.1.
        wait : float, optional
            Time to sleep between steps in seconds.
            Default to 0.
        '''
        if from_current > to_current:
            step = -np.abs(step)

        currents = np.arange(from_current, to_current, step)
        for current in currents:
            self.set_current(current)
            sleep(wait)
            print(current)
        self.set_current(to_current)


def main():
    '''Set current.'''
    parser = ArgumentParser()
    parser.add_argument('current', help='Current in A', type=float)
    args = parser.parse_args()

    c_con = CurrentController()
    c_con.set_current(args.current)


if __name__ == '__main__':
    main()
