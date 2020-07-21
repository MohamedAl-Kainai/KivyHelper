from app.libs import *

class RightContentCls(RightContent):
    pass

class _HotReloadViewer(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.float = MDFloatLayout()
        # self.float.id = 'float'
        # self.add_widget(self.float)

    def menu(self):
        self.manager.current = 'menuscreen'

    def update_kv_file(self,text):
        with open('app/kv/HotReloadViewerTest.txt','w') as f:
            f.write(text)

    def open_menu_tools(self):
        if self.ids.toolsbox.pos_hint['right'] != 1:
            o = Animation(opacity=1,pos_hint={'right':1},duration=.2)
            o.start(self.ids.toolsbox)
        else:
            o = Animation(opacity=0,pos_hint={'right':1.3},duration=.2)
            o.start(self.ids.toolsbox)

    def plus(self):
        if self.ids.boxcode.font_size < sp(30):
            self.ids.boxcode.font_size += sp(3)
        else:
            toast('max')

    def minus(self):
        if self.ids.boxcode.font_size > sp(12):
            self.ids.boxcode.font_size -= sp(3)
        else:
            toast('max')

    
