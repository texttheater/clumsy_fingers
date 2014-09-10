"""
clumsy_fingers.py by Kilian Evang
based on shortcutys.py by Peter Bienstman

This plugin for Mnemosyne 2.x.x [1] reduces the risk of making unintended
input during review by disabling some redundant keyboard shortcuts.

In Mnemosyne, it is possible to show an answer by pressing a number key and to
grade a card (with the currently selected grade) by pressing the space bar.
This behavior is intended to reduce the amount of travel across the keyboard
required, but also frequently leads to unintended actions due to e.g.
accidentally pressing a key twice in a row, with no possibility to undo the
mistake.

This plugin disables those redundant shortcuts so that the number keys are only
for grading and the space bar only for showing the answer. The risk of
unintended actions is thereby greatly reduced.

Note that with current versions of Mnemosyne, only the part that modifies the
space bar behavior is functional. The modified number key behavior is hoped to
work with future versions. [2]

[1] http://mnemosyne-proj.org/
[2] https://code.launchpad.net/~kevang/mnemosyne-proj/number_keys_show_answer
"""

from mnemosyne.libmnemosyne.plugin import Plugin
from mnemosyne.pyqt_ui.review_wdgt import ReviewWdgt


class ClumsyFingersReviewWdgt(ReviewWdgt):

    def __init__(self, component_manager):
        ReviewWdgt.__init__(self, component_manager)
    
        self.auto_focus_grades = False
        self.number_keys_show_answer = False


class ClumsyFingersPlugin(Plugin):

    name = "Clumsy Fingers"
    description = "Disable redundant shortcuts: space bar only shows answer, number keys only grade"
    components = [ClumsyFingersReviewWdgt]


# Register plugin.

from mnemosyne.libmnemosyne.plugin import register_user_plugin
register_user_plugin(ClumsyFingersPlugin)
