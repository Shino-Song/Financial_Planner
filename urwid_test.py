from __future__ import annotations

import urwid

# Similar to the curses_test.py, this is to test out the use of urwid and learn
# how to create a TUI using a different system.

def quit(key: str) -> None:
    if key in {"esc"}:
        raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
    def keypress(self, size, key: str) -> str | None:
        if key != "enter":
            return super().keypress(size, key)
        self.original_widget = urwid.Text(
            f"Hello, {edit.edit_text} \npress 'esc' to end test."
        )
        return None



edit = urwid.Edit("Hello, I am Song Financial Accounting Services. Whom am I assisting today?")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=quit)
loop.run()