import ctypes
from time import sleep


def get_display_positions() -> list[tuple[int, int]]:
    """
    Gets the positions for each display on the users system
    
    Returns:
        A list of pairs of X,Y coordinates to the top left of the display
    """

    positions = []

    def _enum_callback(h_monitor, hdc_monitor, lprc_monitor, dw_data) -> True:
        """Call back function for winapi function"""

        # Can get Width with: lprc_monitor.contents.right - lprc_monitor.contents.left
        # Can get Height with: lprc_monitor.contents.bottom - lprc_monitor.contents.top
        positions.append((int(lprc_monitor.contents.left), int(lprc_monitor.contents.top)))

        return True

    ctypes.windll.user32.EnumDisplayMonitors(
        None, None,
        ctypes.WINFUNCTYPE(
            ctypes.c_int,
            ctypes.c_ulong,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.wintypes.RECT),
            ctypes.c_double
        )(_enum_callback),
        0
    )
    sleep(0.1)  # Await EnumDisplayMonitors

    return positions
