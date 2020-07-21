import os, sys, traceback
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.uix.scrollview import ScrollView
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string(
    """
<HotReloadErrorText>
    MDLabel:
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Custom"
        text_color:
            root.errors_text_color if root.errors_text_color \
            else root.theme_cls.text_color
        text: root.text
"""
)


class HotReloadErrorText(ThemableBehavior, ScrollView):
    text = StringProperty()
    """Text errors.
    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    errors_text_color = ListProperty()
    """
    Error text color.
    :attr:`errors_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """


class HotReloadHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_any_event(self, event):
        self.callback()

class HotReloadViewer(ThemableBehavior, MDBoxLayout):
    """
    :Events:
        :attr:`on_error`
            Called when an error occurs in the KV-file that the user is editing.
    """

    path = StringProperty()
    """Path to KV file.
    :attr:`path` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    errors = BooleanProperty(False)
    """
    Show errors while editing KV-file.
    :attr:`errors` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    errors_background_color = ListProperty()
    """
    Error background color.
    :attr:`errors_background_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    errors_text_color = ListProperty()
    """
    Error text color.
    :attr:`errors_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    _temp_widget = None

    def __init__(self, **kwargs):
        self.observer = Observer()
        self.error_text = HotReloadErrorText()
        super().__init__(**kwargs)
        self.register_event_type("on_error")

    @mainthread
    def update(self, *args):
        """Updates and displays the KV-file that the user edits."""

        Builder.unload_file(self.path)
        self.clear_widgets()
        try:
            self.padding = (0, 0, 0, 0)
            self.md_bg_color = (0, 0, 0, 0)
            self._temp_widget = Builder.load_file(self.path)
            self.add_widget(self._temp_widget)
        except Exception as error:
            self.show_error(error)
            self.dispatch("on_error", error)
        except:
             self.show_error(sys.exc_info())
             self.dispatch("on_error", sys.exc_info())

    def show_error(self, error):
        """Displays text with a current error."""

        if self._temp_widget and not self.errors:
            self.add_widget(self._temp_widget)
            return
        else:
            if self.errors_background_color:
                self.md_bg_color = self.errors_background_color
            self.padding = ("4dp", "4dp", "4dp", "4dp")
            self.error_text.text = (
                error.message
                if getattr(error, r"message", None)
                else str(error)
            )
            self.add_widget(self.error_text)

    def on_error(self, *args):
        """
        Called when an error occurs in the KV-file that the user is editing.
        """

    def on_errors_text_color(self, instance, value):
        self.error_text.errors_text_color = value

    def on_path(self, instance, value):
        self.observer.schedule(
            HotReloadHandler(self.update, value), os.path.split(value)[0]
        )
        self.observer.start()
        Clock.schedule_once(self.update, 1)
