# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# 设置背景颜色（可选）
Window.clearcolor = (0.2, 0.6, 0.8, 1)  # 蓝色背景


class HelloApp(App):
    def build(self):
        # 创建一个标签，显示 "Hello, World!"
        return Label(
            text="Hello, World!",
            font_size=50,
            color=(1, 1, 1, 1),  # 白色文字
            halign="center",
            valign="middle"
        )


if __name__ == "__main__":
    HelloApp().run()