from app.libs import *

class KivyHelper(MagicBehavior,ButtonBehavior,MDFloatLayout):

    def __init__(self, *args, **kwargs):
        super(KivyHelper, self).__init__(*args, **kwargs)

class MenuScreen(Screen):
    iconsscreen = ObjectProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ADD(self):
        data = {
        'BUTTONS':'buttons.png',
        'TOOLBAR':'toolbar.png',
        }
        for name,image in data.items():
            box = KivyHelper()
            box.text_widgets=name
            box.manager = self.manager
            box.image_path='app/images/'+image
            self.ids.widgets.add_widget(box)
