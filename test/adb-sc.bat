@echo off
SET SC=%1%
adb shell screencap -p /sdcard/%SC%
adb pull /sdcard/%SC% %SC%

echo save %SC% success