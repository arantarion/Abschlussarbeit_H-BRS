# Untersuchung der Sicherheit von OpenWrt anhand der BSI TR-03148 mittels eines OpenWrt betriebenen Heim-Routers
### Bachelorarbeit im Studiengang Informatik der Hochschule Bonn-Rhein-Sieg
##### Prüfer: Prof. Dipl.-Ing. Markus Ullmann und Prof. Dr.-Ing. Norbert Jung
##### Betreuer: Florian Bierhoff
<br>
<br>

## Zielsetzung
<br>
Ziel dieser Arbeit war es, die Technische Richtlinie 03148 des BSI an Version 19.7.04 von OpenWrt durchzuführen und das Router-Betriebssystem auf Konformität zu prüfen. Hierbei wurde ein TP-Link Archer C7 Router genutzt. Es wurden die grundsätzlichen Sicherheitsmerkmale von OpenWrt mittels der Technischen Richtlinie evaluiert. Dabei wurde nur die Funktionalität des Betriebssystems geprüft, welche nach der Installation auf dem Gerät bereitgestellt wurde. Funktionen, welche vom Nutzer zusätzlich installiert und eingerichtet werden mussten, wurden nicht betrachtet. Wenn es der Testfall angeboten hat wurde ein automatischer Test entwickelt, sodass eine wiederholte Durchführung beschleunigt werden kann. Ebenso wurde die Anwendbarkeit der Technischen Richtlinie auf quelloffene Netzwerk-Betriebssysteme ermessen. Darüber hinaus wurden statische Softwaretests einiger quelloffener Router-Betriebssysteme mittels des „Firmware Analysis and Comparison Tools“ als weitere Metrik genutzt, um einen differenzierteren Einblick in die Sicherheitslage solcher Projekte zu gewähren. Die Ergebnisse dieser Analyse wurden darauffolgend mit den Ergebnissen des „Home Router Security Report 2020“ des Fraunhofer-Instituts für Kommunikation, Informationsverarbeitung und Ergonomie verglichen. Abschließend wurde sich kritisch mit den Ergebnissen, sowie der technischen Richtlinie, auseinandergesetzt. Die in dieser wissenschaftlichen Untersuchung genutzte Vorgehensweise kann nicht die vollständige Sicherheit aller Aspekte der Software OpenWrt nachzuweisen. Es muss immer betont werden, dass viele potenziell wichtige Aspekte einer sicheren Software nicht in Betracht gezogen werden. Vielmehr soll eine Grundlage bzw. ein möglicher Einstiegspunkt für weitere Forschung an Methoden und Abläufen zum Testen von Open Source (Router) Software geschaffen werden. Die Ergebnisse der Arbeit können sowohl der Entwicklung von OpenWrt als auch unerfahrenen Endnutzern weitere Einblicke in die Sicherheit des Projektes liefern und somit langfristig die Resilienz der Heim-Netzinfrastruktur stärken.<br><br>

## Ordnerstruktur
📦Abschlussarbeit_H-BRS<br>
 ┣ 📂Bachelorarbeit **↤ Text of thesis / TR Results / Additional Figures**<br>
 ┃ ┣ 📂TR Results **↤ TR results and additional data**<br>
 ┃ ┃ ┣ 📂TR.A **↤ Results of TR.A**<br>
 ┃ ┃ ┣ 📂TR.B<br>
 ┃ ┃ ┣ 📂...<br>
 ┃ ┃ ┣ 📂TR.J<br>
 ┃ ┃ ┣ 📂Test Environment **↤ Graphics describing the test environment** <br>
 ┃ ┃ ┣ 📜ssh-audit-consoleout.png<br>
 ┃ ┃ ┗ 📜ssh-audit_log.json<br>
 ┃ ┗ 📜Openwrt_19.07.4.bin **↤ The firmware that was used**<br>
 ┃ ┗ 📜Weckermann_ICS_and_Test Documentation.xlsx **↤ Filled in excel document for TR**<br>
 ┃<br>
 ┣ 📂Expose **↤ Contains the expose and Gant diagram**<br>
 ┃<br>
 ┣ 📂FACT Analyse **↤ Contains multiple firmware images that were used**<br>
 ┃ ┣ 📂Firmware_Img_OpenWrt_19.07.4 **↤ The images used for the TP-Link router**<br>
 ┃ ┣ 📂Firmware_Img_Other **↤ Contains the images from the FACT corpus**<br>
 ┃ ┣ 📂Linux Kernel CVEs **↤ Contains information about Linux kernel CVEs (CVSS >= 7)**<br>
 ┃ ┣ 📂Results FACT **↤ Results from the FACT analysis**<br>
 ┃ ┃ ┣ 📂AdvancedTomato<br>
 ┃ ┃ ┣ 📂DD-WRT<br>
 ┃ ┃ ┣ 📂Gargoyle<br>
 ┃ ┃ ┣ 📂Gluon<br>
 ┃ ┃ ┣ 📂LibreCMC<br>
 ┃ ┃ ┣ 📂OpenWrt 19.07.4<br>
 ┃ ┃ ┗ 📂OpenWrt 19.07.5<br>
 ┃ ┣ 📜Firmware Downloads and Versions.txt **↤ Information on the firmware images from the FACT corpus**<br>
 ┃ ┗ 📜analysis.xlsx **↤ Analysis of the FACT results**<br>
 ┃<br>
 ┣ 📂OpenWrt Documentation and Documents **↤ Holds documentation and backups from websites that were used or referenced**<br>
 ┃ ┣ 📂Documentation Downloader **↤ Resources to download the OpenWrt documentation from their website**<br>
 ┃ ┣ 📂Documentation HTML **↤ OpenWrt documentation as HTML documents (zipped)** <br>
 ┃ ┣ 📂Documentation Plain Text **↤ OpenWrt documentation as plain text**<br>
 ┃ ┃ ┣ 📂OpenWrtWiki_Dev_Doku<br>
 ┃ ┃ ┣ 📂OpenWrtWiki_QuickStart_Doku<br>
 ┃ ┃ ┗ 📂OpenWrtWiki_User_Doku<br>
 ┃ ┣ 📂Documentation other websites **↤ Backups of websites that were used for this thesis**<br>
 ┃ ┣ 📂Packages_ToH_Dump **↤ Package dump of OpenWrt 19.07.4 + script**<br>
 ┃ ┗ 📜installed_packages_factory.txt **↤ List of packages that are installed on OpenWrt in factory state**<br>
  ┃<br>
 ┣ 📂OpenWrt Statistics **↤ OpenWrt download statistics from their websites for november, OpenWrt git statistics generated with gitstat**<br>
 ┃ ┣ 📂OpenWrt Download Statistics<br>
 ┃ ┗ 📂OpenWrt Git Statistics 26.10.20<br>
 ┃<br>
 ┣ 📂Papers **↤ Some papers that were used in this thesis**<br>
 ┃<br>
 ┣ 📂Prüfspezfikation und ergänzende Dokumente **↤ TR 03148, additional documents of TR, further papers that were referenced in TR 03148**<br>
 ┃<br>
 ┣ 📂Scripts **↤ Python and Bash scripts**<br>
 ┃<br>
 ┣ 📜README.md<br>
 ┣ 📜henry_pub.asc<br>
 ┗ 📜Backup Literaturverzeichnis.7z **↤ Contains a copy of all references listed in the thesis**
