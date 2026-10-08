[app]
title = FNH 2
package.name = fnah2
package.domain = org.fnah2
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,ico,pem,txt
source.include_patterns = sprites/*,sounds/*,fonts/*,files/*,include/*
version = 1.1.1
requirements = python3,pygame,pyasn1,rsa
orientation = landscape
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.permissions = WAKE_LOCK,INTERNET
android.api = 33
android.min_api = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
icon.filename = icon.ico
presplash.filename = sprites/menu/logos/4.png
[buildozer]
log_level = 2
warn_on_root = 1
