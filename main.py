from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class DjossabaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text='DJOSSABA Agro', font_size=30, bold=True))
        layout.add_widget(Label(text='Bienvenue ! Votre APK marche !'))
        layout.add_widget(Button(text='Commander', background_color=(0,0.6,0,1)))
        return layout

DjossabaApp().run()
