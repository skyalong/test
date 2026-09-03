[app]
title = Hello World
package.name = helloworld
package.domain = org.test

source.dir = .
source.include_exts = py

version = 1.0.0

requirements = python3,kivy

android.permissions = INTERNET
android.api = 33
android.ndk = 25c
android.sdk = 33
android.minapi = 21

android.enable_androidx = True
fullscreen = 0
orientation = portrait

log_level = 2
warn_on_root = 0

[buildozer]
log_level = 2