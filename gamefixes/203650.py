""" Game fix for Sonic the Hedgehog 4: Episode II
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ lock to 60 fps
    """

    util.set_environment('DXVK_FRAME_RATE', '60')
