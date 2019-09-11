from kivy.app import App
from kivy.lang import Builder


kv = """
AnchorLayout:
	canvas:
		Color:
			
		Rectangle:
			pos:self.pos
			size:self.size
	AsyncImage:
		size_hint:None, None
		size: dp(500), dp(500)
		source:'https://raw.githubusercontent.com/kivy/kivy/master/kivy/data/logo/kivy-icon-256.png'
		anim_delay: 0.2
"""


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()
