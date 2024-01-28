#!/usr/bin/env python3
from .current_controller import CurrentController

def ramp_up():
    c_con = CurrentController()
    c_con.ramp_from_to(0, 8, wait=0.2)
