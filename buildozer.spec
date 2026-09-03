[app]
title = Hello World
package.name = helloworld
package.domain = org.test

source.dir = .
source.include_exts = py

version = 1.0.0

# 🔑 关键：指定 Python 3.11
requirements = python3==3.11.9,kivy

android.permissions = INTERNET
android.api = 33
android.ndk = 25c
android.sdk = 33
android.minapi = 21

# 🔑 只编译一个架构，节省内存
android.arch = arm64-v8a

android.enable_androidx = True
fullscreen = 0
orientation = portrait

log_level = 2
warn_on_root = 0

[buildozer]
log_level = 2