@echo off

:start

::set d="auto" 
set t=%date%%time%
set /p d=git commit: 

git add . && git commit -m "%d%" && git push 

::pause
::echo -----------------------------------------------------------------
::goto start
