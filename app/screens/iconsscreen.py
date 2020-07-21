from app.libs import *

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class IconsScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''
        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                }
            )
        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

    def menu(self):
        self.manager.current='menuscreen'

    def close_search(self):
        if self.ids.Toolbar.title == '':
            self.ids.Toolbar.title = 'Kivymd icons'
            self.ids.Toolbar.right_action_items = [
            ['magnify',lambda x: self.search(self.ids.Toolbar,self.ids.search_field)]
            ]

            self.ids.search_field.size_hint = (None,None)
            self.ids.search_field.size = (0,0)
            self.ids.search_field.opacity = 0

    def search(self,Toolbar,TextField):
        Toolbar.title = ''
        Toolbar.right_action_items = []

        TextField.size_hint = (.8,1)
        TextField.opacity = 1
