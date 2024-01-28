#!/usr/bin/env python3
from .current_controller import CurrentController

def ramp_down():
    c_con = CurrentController()
    c_con.ramp_from_to(8, 0, wait=0.2)
