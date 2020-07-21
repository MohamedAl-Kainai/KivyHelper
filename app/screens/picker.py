from app.libs import *

class ColorSelector(MDIconButton):
    color_name = OptionProperty("Indigo", options=palette)

    def rgb_hex(self, col):
        return get_color_from_hex(colors[col][self.theme_cls.accent_hue])


class MDThemePicker(
    ThemableBehavior,
    FloatLayout,
    ModalView,
    SpecificBackgroundColorBehavior,
    RectangularElevationBehavior,
):
    pass
