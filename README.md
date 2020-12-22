# Untersuchung der Sicherheit von OpenWrt anhand der BSI TR-03148 mittels eines OpenWrt betriebenen Heim-Routers
### Bachelorarbeit im Studiengang Informatik der Hochschule Bonn-Rhein-Sieg
##### Betreuer: Prof. Dipl.-Ing. Markus Ullmann und Prof. Dr.-Ing. Norbert Jung
#
#
### Zielsetzung
In der wissenschaftlichen Arbeit soll als Ausgangspunkt einer Sicherheitsanalyse von Router Firmware die BSI TR-03148: Secure Broadband Router [1] auf einen OpenWrt fähigen Router angewendet bzw. überprüft werden. Hierbei sollen einige Aspekte der Sicherheit von OpenWrt anhand dieser Technischen Richtlinie geprüft werden. Die Technische Richtlinie beschreibt sehr umfängliche Tests und Anforderungen an Router Firmware, welche von Herstellern eingehalten werden sollten, um grundsätzlich die Sicherheit des Gerätes und der darauf betriebenen Software feststellen zu können. Ein positiver Nebeneffekt ist, dass die meisten Anforderungen auch noch im Nachhinein in einer Firmware angepasst werden können, ohne die gesamte Software Architektur ändern zu müssen. Die Anforderungen sind mit Absicht allgemein gehalten, um sie auf ein möglichst weites Spektrum von Geräten anwenden zu können. So also auch auf das Open Source Projekt OpenWrt. Da es natürlich keinen zuständigen Hersteller gibt, sich OpenWrt aber großer Beliebtheit erfreut [2], ist eine Überprüfung anhand der Technischen Richtlinie des BSI von Interesse. Die Erfüllung der Technischen Richtlinie 03148 bietet zudem eine weitere Möglichkeit für Endanwender. Falls ein noch funktionierendes Gerät nicht mehr durch Updates vom Hersteller unterstützt wird, könnte es durch das Betreiben mit OpenWrt weiter sicher genutzt werden, statt einem Neukauf weichen zu müssen. Zunächst sollen die zugehörigen Tests der BSI TR-03148 möglichst vollumfänglich an einem, im Vorhinein festgelegten, OpenWrt fähigen Router durchgeführt und der Test Spezifikation folgend dokumentiert werden. Funktionalität wie ein integriertes Virtual Private Network (VPN) oder Voice over IP (VoIP) sollen dabei nicht in den Anforderungsbereich fallen. Wenn es der Testfall anbietet so soll ein automatischer Test entwickelt werden, welcher in Zukunft die Durchführung beschleunigen kann. Nach Abschluss aller Tests könnte in einem letzten Schritt ein Software Tool wie das vom Fraunhofer Institut für Kommunikation, Informationsverarbeitung und Ergonomie (FKIE) entwickelte Open Source Software Projekt „FACT“ [3] verwendet werden, um auch einige Varianten der aktuellen „stable release“ Version von OpenWrt damit zu analysieren und die Ergebnisse denen des „Home Router Security Report 2020“[4] gegenüberzustellen. Nachdem alle Tests abgeschlossen wurden, sollen die Ergebnisse zusammengetragen, ausgewertet und in Kontext gesetzt werden. Basierend auf den Anhaltspunkten, die aus den Tests gewonnen wurden, muss eine Sicherheitsbewertung von OpenWrts stable release Version für den ausgewählten Router erarbeitet werden. Darüber hinaus müssen Wege und Vorschläge entwickelt werden, die fehlgeschlagenen Tests zu bestehen, um die Sicherheit zu erhöhen. Diese wissenschaftliche Untersuchung setzt sich nicht das Ziel die vollständige Sicherheit aller Aspekte der Software OpenWrt nachzuweisen, auch wenn dies natürlich wünschenswert wäre. Es muss immer betont werden, dass viele potenziell wichtige Aspekte einer sicheren Software nicht in Betracht gezogen werden. Vielmehr soll eine Grundlage bzw. ein möglicher Einstiegspunkt für weitere Forschung an Methoden und Abläufen zum Testen von Open Source (Router) Software geschaffen werden.

[1] Bundesamt für Sicherheit in der Informationstechnik (Hrsg.), BSI TR-03148:Secure Broadband Router: Requirements for secure BroadbandRouters. [Online]. Verfügbar unter: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR03148/TR03148.pdf?__blob=publicationFile&v=3 (Letzter Zugriff: 11. August 2020).
[2] OpenWrt Project, Statistical Overview. [Online]. Verfügbar unter: https://downloads.openwrt.org/stats/ (Letzter Zugriff: 13. Dezember 2020).
[3] FACT Core. [Online]. Verfügbar unter: https://github.com/fkie-cad/FACT_core (Letzter Zugriff: 21. Dezember 2020).
[4] Peter Weidenbach, Johannes vom Dorp, Home Router Security Report2020. [Online]. Verfügbar unter: https://www.fkie.fraunhofer.de/content/dam/fkie/de/documents/HomeRouter/HomeRouterSecurity_2020_Bericht.pdf (Letzter Zugriff: 11. August 2020).

***

### Ordnerstruktur
📦Abschlussarbeit_H-BRS
 ┣ 📂Bachelorarbeit
 ┃ ┣ 📂Results
 ┃ ┃ ┣ 📂Figures
 ┃ ┃ ┣ 📂TR.A
 ┃ ┃ ┣ 📂TR.B
 ┃ ┃ ┣ 📂...
 ┃ ┃ ┣ 📂TR.J
 ┃ ┃ ┣ 📂Test Environment
 ┃ ┃ ┣ 📜installed_packages.txt
 ┃ ┃ ┣ 📜ssh-audit-consoleout.png
 ┃ ┃ ┗ 📜ssh-audit_log.json
 ┃ ┣ 📂Text
 ┃ ┣ 📜Weckermann_ICS_and_Test Documentation.xlsx
 ┃
 ┣ 📂Expose
 ┃
 ┣ 📂Firmware Images
 ┃ ┣ 📂Firmware_Img_OpenWrt_19.07.4
 ┃ ┣ 📂Firmware_Img_Other
 ┃ ┣ 📂Linux Kernel CVEs
 ┃ ┣ 📂Results FACT
 ┃ ┃ ┣ 📂AdvancedTomato
 ┃ ┃ ┣ 📂DD-WRT
 ┃ ┃ ┣ 📂Gargoyle
 ┃ ┃ ┣ 📂Gluon
 ┃ ┃ ┣ 📂LibreCMC
 ┃ ┃ ┣ 📂OpenWrt 19.07.4
 ┃ ┃ ┗ 📂OpenWrt 19.07.5
 ┃ ┣ 📜Firmware Downloads and Versions.txt
 ┃ ┗ 📜analysis.ods
 ┃
 ┣ 📂OpenWrt Documentation and Documents
 ┃ ┣ 📂Documentation Downloader
 ┃ ┣ 📂Documentation HTML
 ┃ ┣ 📂Documentation Plain Text
 ┃ ┃ ┣ 📂OpenWrtWiki_Dev_Doku
 ┃ ┃ ┣ 📂OpenWrtWiki_QuickStart_Doku
 ┃ ┃ ┗ 📂OpenWrtWiki_User_Doku
 ┃ ┣ 📂Documentation other websites
 ┃ ┣ 📂Packages_ToH_Dump
 ┃ ┗ 📜installed_packages_factory.txt
 ┃
 ┣ 📂Papers
 ┃
 ┣ 📂Prüfspezfikation und ergänzende Dokumente
 ┃
 ┣ 📂Scripts
 ┃
 ┣ 📂Statistics
 ┃ ┣ 📂OpenWrt Download Statistics
 ┃ ┗ 📂OpenWrt Git Statistics 26.10.20
 ┃
 ┣ 📜README.md
 ┣ 📜henry_pub.asc
 ┗ 📜security notes .txt
