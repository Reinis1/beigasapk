from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')


class AnchorLayoutEx(AnchorLayout):
    pass


class WidgetsLayout(GridLayout):
    my_text = StringProperty("1")
    count = 1
    count_enabled = BooleanProperty(False)
    text_input_str = StringProperty("type here")
    # slider_value_txt = StringProperty("50")

    def on_button_c(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, me):
        if me.state == "normal":
            me.text = "OFF"
            self.count_enabled = False
        else:
            me.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        pass

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


class Canvas1(Widget):
    pass


class Canvas2(Widget):
    pass


class Canvas4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 100, 500), width=2)
            Color(1, 1, 0)
            Line(circle=(400, 200, 100), width=1)
            Line(rectangle=(700, 500, 150, 100), width=5)
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))

    def on_button_move_press(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x, y)


class Canvas5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(dp(self.ball_size), dp(self.ball_size)))
        Clock.schedule_interval(self.update, 1/144)

    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx
        self.ball.pos = (x+1, y+1)

class Canvas6(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
