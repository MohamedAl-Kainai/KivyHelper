from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivymd.icon_definitions import md_icons
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.toast import toast
from kivymd.theming import ThemableBehavior
from kivymd.color_definitions import colors, palette
from kivy.utils import get_hex_from_color

from kivy.base import (
    ExceptionHandler,
    ExceptionManager,)

import os ,threading ,time ,logging ,json

from kivymd.uix.card import MDCardSwipe
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.textfield import MDTextField
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu,RightContent
from kivymd.uix.dialog import MDDialog
from kivy.uix.modalview import ModalView
from kivymd.uix.picker import MDThemePicker
from kivy.uix.screenmanager import (
    Screen,
    ScreenManager,
)
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    RectangularElevationBehavior,
    MagicBehavior,
    SpecificBackgroundColorBehavior,
)
from kivy.uix.behaviors import (
    ButtonBehavior,
)
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.metrics import dp, sp

if platform == 'android':
    from android.permissions import (
    Permission,
    request_permission,
    request_permissions,
    check_permission
    )
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    import android

else:
    run_on_ui_thread = lambda x:x

from app.screens import (
    picker,
    menuscreen,
    iconsscreen,
    hotreloadviewer,
    settingsscreen,
)
Builder.load_string('''
#:import Clipboard kivy.core.clipboard.Clipboard
#:import images_path kivymd.images_path
#:import toast kivymd.toast.toast
#:import Window kivy.core.window.Window
#:import OpenUrl webbrowser.open

# Screens transition...
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import CardTransition kivy.uix.screenmanager.CardTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition

''')
for i in os.listdir('./app/kv'):
    if i.endswith('.kv'):
        Builder.load_file('app/kv/'+i)
