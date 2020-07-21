from app.libs import *

class MyOneLineListItem(RectangularRippleBehavior,ButtonBehavior,MDFloatLayout):
    pass

class AboutScreen(Screen):
    def back(self):
        self.manager.current = 'menuscreen'

class SettingsScreen(Screen):
    def back(self):
        self.manager.current = 'aboutscreen'
