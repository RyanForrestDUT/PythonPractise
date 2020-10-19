@echo off
set cur_path=%~dp0

rd /s /q %cur_path%\OutResults
del /s /q /f %cur_path%\word_dict.txt
echo f|xcopy word_dict_bak.txt word_dict.txt
