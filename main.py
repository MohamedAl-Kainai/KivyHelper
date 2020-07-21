from kivymd.app import MDApp
from app.libs import *

if platform == 'android':
    Color = autoclass("android.graphics.Color")
    WindowManager = autoclass('android.view.WindowManager$LayoutParams')
    activity = autoclass('org.kivy.android.PythonActivity').mActivity


class E(ExceptionHandler):
    def handle_exception(self, inst):
        print(inst)
        return ExceptionManager.PASS
ExceptionManager.add_handler(E())

if platform != 'android':
    Window.size = (400,1000)
    Window.left = True

ROOT = '''
ScreenManager:
    transition:NoTransition()
    id:RootManager

    MenuScreen:
        id:menuscreen
        iconsscreen:iconsscreen
        name:'menuscreen'

    IconsScreen:
        id:iconsscreen
        menuscreen:menuscreen
        name:'iconsscreen'

    _HotReloadViewer:
        id:hotreloadviewer
        name:'hotreloadviewer'

    AboutScreen: # and settings
        name:'aboutscreen'

    ButtonsScreen:
        name:'BUTTONS'

    ToolbarScreen:
        name:'TOOLBAR'
'''

class KivyHelpApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = self.LoadSettings()['AppTheme']['Style']
        self.theme_cls.primary_palette = self.LoadSettings()['AppTheme']['Primary']


        self.root = Builder.load_string(ROOT)
        self.root.ids.menuscreen.ADD()

    @run_on_ui_thread
    def statusbar(self,color):
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color))
        window.setNavigationBarColor(Color.parseColor(color))

    def check_android_permission(self):
        if platform == 'android':
            return check_permission(Permission.WRITE_EXTERNAL_STORAGE)
        else:
            return False

    def get_android_permission(self):
        if platform == 'android':
            if (status:=check_permission(Permission.WRITE_EXTERNAL_STORAGE)): pass
            else:
                request_permissions([
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE,
                ])

    def back_to_menu(self,manager):
        manager.current = 'menuscreen'

    def show_theme_picker(self):
        theme_dialog = picker.MDThemePicker()
        theme_dialog.open()

    def show_alert_dialog(self,text):
        MDDialog(
                title="code {}",
                text=text,
            ).open()

    def DumpSettings(self,db):
        with open('app/settings.json','w') as f:
            f.write(json.dumps(db,indent=2))

    def LoadSettings(self):
        with open('app/settings.json','r') as f:
            data = f.read()
        return json.loads(data)

    def UpdateSettings(self,type=None):
        if type == 'Color':
            db = self.LoadSettings()
            db['AppTheme']['Primary'] = self.theme_cls.primary_palette
            db['AppTheme']['Style'] = self.theme_cls.theme_style
            self.DumpSettings(db)

    def on_stop(self):
        self.UpdateSettings(type='Color')


if __name__ == '__main__':
    KivyHelpApp().run()
