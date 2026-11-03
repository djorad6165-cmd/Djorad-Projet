[[[app]
title = DJOSSABA Agro
package.name = djossabaagro
package.domain = com.djossaba.agro
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreement = True
