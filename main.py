import sys
from tkinter.messagebox import showerror
from time import sleep

import keysym
from idle_time import get_idle_time
from window import Window
from displays import get_display_positions


def get_args() -> tuple[int, str, bool] | tuple[None, None, None]:
    """Gets values from the command line arguments"""

    args = sys.argv[1:]

    # Idle time
    if len(args) > 0:
        try:
            idle_time = int(args[0])
        except:
            showerror("Error", "Invalid idle time: " + args[0])
            return None, None, None
    else:
        idle_time = 60  # 1 minute

    # Close key
    if len(args) > 1:
        close_key = args[1]

        if close_key not in keysym.names:
            showerror("Error", "Invalid close key: " + args[0])
            return None, None, None
    else:
        close_key = "Delete"

    # Show now
    if len(args) > 2:
        show_now = True
    else:
        show_now = False

    return idle_time, close_key, show_now


def main():
    idle_time, close_key, show_now = get_args()
    if idle_time is None: return

    # Set up vars
    do_exit = False
    windows = []
    displays = get_display_positions()

    # Create windows
    for display in displays:
        window = Window(display[0], display[1], close_key)
        window.hide = lambda: [Window.hide(win) for win in windows]
        windows.append(window)

        if show_now:
            window.show()

    # Event loop
    while not do_exit:
        for win in windows:

            # Update windows
            win.update()
            win.update_idletasks()

            # Check if it was closed
            try:
                win.winfo_exists()
            except:
                # Exit
                do_exit = True
                break

            # Show if past idle time
            if get_idle_time() > idle_time:
                win.show()

        sleep(1)  # Don't kill the CPU

    # Close all windows
    for win in windows:
        try:
            win.destroy()
        except:
            pass


if __name__ == "__main__":
    main()
