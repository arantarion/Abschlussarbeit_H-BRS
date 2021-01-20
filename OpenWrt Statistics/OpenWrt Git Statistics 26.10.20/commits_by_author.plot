set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Felix Fietkau" w lines, 'commits_by_author.dat' using 1:3 title "Gabor Juhos" w lines, 'commits_by_author.dat' using 1:4 title "John Crispin" w lines, 'commits_by_author.dat' using 1:5 title "Florian Fainelli" w lines, 'commits_by_author.dat' using 1:6 title "Jo-Philipp Wich" w lines, 'commits_by_author.dat' using 1:7 title "Hauke Mehrtens" w lines, 'commits_by_author.dat' using 1:8 title "Nicolas Thill" w lines, 'commits_by_author.dat' using 1:9 title "Imre Kaloz" w lines, 'commits_by_author.dat' using 1:10 title "Rafał Miłecki" w lines, 'commits_by_author.dat' using 1:11 title "Jonas Gorski" w lines, 'commits_by_author.dat' using 1:12 title "Steven Barth" w lines, 'commits_by_author.dat' using 1:13 title "Adrian Schmutzler" w lines, 'commits_by_author.dat' using 1:14 title "Luka Perkov" w lines, 'commits_by_author.dat' using 1:15 title "Mathias Kresin" w lines, 'commits_by_author.dat' using 1:16 title "Mike Baker" w lines, 'commits_by_author.dat' using 1:17 title "Waldemar Brodkorb" w lines, 'commits_by_author.dat' using 1:18 title "Hans Dedecker" w lines, 'commits_by_author.dat' using 1:19 title "Koen Vandeputte" w lines, 'commits_by_author.dat' using 1:20 title "Daniel Golle" w lines, 'commits_by_author.dat' using 1:21 title "Christian Lamparter" w lines
