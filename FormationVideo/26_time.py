#coding:utf-8

"""
Epoch (Unix): 1er Janvier 1970 à 00h00m00s GMT

.sleep(<time>)      : time in sec
.time()             : return Epoch time in sec

.localtime():
    tm_year     = année
    tm_mon      = mois
    tm_mday     = jour
    tm_hour     = heure
    tm_min      = minute
    tm_sec      = seconde
    tm_wday     = jour de la semaine (lundi=0, mardi=1, etc...)
    tm_yday     = jour de l'année
    tm_isdst    = decalage horraire (bool)

.mktime(<var>):
    convert date format (localtime) to timestamp format (time)

.strftime():
    %d : jour (00:31)
    %A : jour de la semaines 
    %a : jour abrégé

    %m : mois (01:12)
    %B : mois
    %b : mois abrégé

    %Y : année (2021)
    %y : année (21)

    %H : heures (24) (00:23)
    %I : heures (12) (00:12)
    %p : AM/PM

    %M : minutes (00:59)

    %S : secondes (00:59)

    %f : microsecondes

    %z : UTC offset in the form +HHMM or -HHMM
    %Z : time zone name

    %w : jour de la semaine (0,1..6)
    %j : jour de l'année (001..366)
    %W : semaines de l'année (00.55)

    %c : standard date and time (Mon Sep 30 07:06:05 2013)
    %x : standard date (09/30/13)
    %X : standard time (07:06:05)
    %% : un "%"
"""

import time

"""
count = 0

while True:
    count += 1
    print(f"{count} sec")
    time.sleep(1)
"""

# Profiling : temps d'execution
"""
begin = time.time()
print("Début")
time.sleep(5)
end = time.time()
print("Fin")
print(f"Temps Exécuté ; {end - begin}s")
"""

# localtime()
"""
def printDate():
    date = time.localtime()

    print(date)

    for k, v in enumerate(date):
        print(k,v)

    print(f"{date[3]}:{date[4]}:{date[5]} {date[2]}/{date[1]}/{date[0]}")

printDate()
"""
