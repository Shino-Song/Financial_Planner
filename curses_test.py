import curses
import shutil
from curses import wrapper
from curses.textpad import rectangle

# Current plan for consideration. Curses appears to be a good terminal based user
# interface. I am looking at making multiple windows and paddings that can store
# and display information on terminal and update with the relevant input.
# Some aspects I'm thinking about is how it will handle various scren resolutions
# and sizings. I would like the interface to scale and fit monitors of all
# resolutions while looking good. I know this will probably be best done with
# a graphical interface reather than a terminal one, but that is later down the
# to-do list. For now, maybe figure out how to force terminal to full screen
# then get the display resolution from the computer and do some math to determin
# positioning based on that? We will see. Overall, hopefully this allows for some
# visually appealing display of information.


def tui_scaling():
    return (f"Your terminal resolution is: columns={terminal_res.columns}, lines={terminal_res.lines}")
    #pass

def curses_screen(stdscr):
    # Coordinate note. addstr - line, column, "text"
    # rectangle(stdscr, L1, C1, L2, C2)
    stdscr.getmaxyx()
    stdscr.clear()
    stdscr.refresh()
    stdscr.box()
    #boundary = rectangle(stdscr, 0, 1, 52, 198)
    uid = rectangle(stdscr, 1, 2, 3, 22) #UID
    stdscr.addstr(2, 3, "User/Company Name")
    active_item = rectangle(stdscr, 1, 58, 3, 138) #Current item/dir/folder thing
    lanky = rectangle(stdscr, 4, 170, 51, 197) #long thin view
    infobox = rectangle(stdscr, 4, 2, 48, 169) #main infobox
    inputbox = rectangle(stdscr, 49, 2, 51, 169) #text input
    date_time = rectangle(stdscr, 1, 170, 3, 197) #date/time

    stdscr.getch()

wrapper(curses_screen)