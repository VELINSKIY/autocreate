:create
@echo off
set /P new_project="Yes Master, the title? "
cd SOME\\PATH
python create.py %new_project%