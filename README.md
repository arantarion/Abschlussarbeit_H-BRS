# Untersuchung der Sicherheit von OpenWrt anhand der BSI TR-03148 mittels eines OpenWrt betriebenen Heim-Routers
### Bachelorarbeit im Studiengang Informatik der Hochschule Bonn-Rhein-Sieg
##### Betreuer: Prof. Dipl.-Ing. Markus Ullmann und Prof. Dr.-Ing. Norbert Jung
<br>
<br>
### Zielsetzung
In der wissenschaftlichen Arbeit soll als Ausgangspunkt einer Sicherheitsanalyse von Router Firmware die BSI TR-03148: Secure Broadband Router [1] auf einen OpenWrt fähigen Router angewendet bzw. überprüft werden. Hierbei sollen einige Aspekte der Sicherheit von OpenWrt anhand dieser Technischen Richtlinie geprüft werden. Die Technische Richtlinie beschreibt sehr umfängliche Tests und Anforderungen an Router Firmware, welche von Herstellern eingehalten werden sollten, um grundsätzlich die Sicherheit des Gerätes und der darauf betriebenen Software feststellen zu können. Ein positiver Nebeneffekt ist, dass die meisten Anforderungen auch noch im Nachhinein in einer Firmware angepasst werden können, ohne die gesamte Software Architektur ändern zu müssen. Die Anforderungen sind mit Absicht allgemein gehalten, um sie auf ein möglichst weites Spektrum von Geräten anwenden zu können. So also auch auf das Open Source Projekt OpenWrt. Da es natürlich keinen zuständigen Hersteller gibt, sich OpenWrt aber großer Beliebtheit erfreut [2], ist eine Überprüfung anhand der Technischen Richtlinie des BSI von Interesse. Die Erfüllung der Technischen Richtlinie 03148 bietet zudem eine weitere Möglichkeit für Endanwender. Falls ein noch funktionierendes Gerät nicht mehr durch Updates vom Hersteller unterstützt wird, könnte es durch das Betreiben mit OpenWrt weiter sicher genutzt werden, statt einem Neukauf weichen zu müssen. Zunächst sollen die zugehörigen Tests der BSI TR-03148 möglichst vollumfänglich an einem, im Vorhinein festgelegten, OpenWrt fähigen Router durchgeführt und der Test Spezifikation folgend dokumentiert werden. Funktionalität wie ein integriertes Virtual Private Network (VPN) oder Voice over IP (VoIP) sollen dabei nicht in den Anforderungsbereich fallen. Wenn es der Testfall anbietet so soll ein automatischer Test entwickelt werden, welcher in Zukunft die Durchführung beschleunigen kann. Nach Abschluss aller Tests könnte in einem letzten Schritt ein Software Tool wie das vom Fraunhofer Institut für Kommunikation, Informationsverarbeitung und Ergonomie (FKIE) entwickelte Open Source Software Projekt „FACT“ [3] verwendet werden, um auch einige Varianten der aktuellen „stable release“ Version von OpenWrt damit zu analysieren und die Ergebnisse denen des „Home Router Security Report 2020“[4] gegenüberzustellen. Nachdem alle Tests abgeschlossen wurden, sollen die Ergebnisse zusammengetragen, ausgewertet und in Kontext gesetzt werden. Basierend auf den Anhaltspunkten, die aus den Tests gewonnen wurden, muss eine Sicherheitsbewertung von OpenWrts stable release Version für den ausgewählten Router erarbeitet werden. Darüber hinaus müssen Wege und Vorschläge entwickelt werden, die fehlgeschlagenen Tests zu bestehen, um die Sicherheit zu erhöhen. Diese wissenschaftliche Untersuchung setzt sich nicht das Ziel die vollständige Sicherheit aller Aspekte der Software OpenWrt nachzuweisen, auch wenn dies natürlich wünschenswert wäre. Es muss immer betont werden, dass viele potenziell wichtige Aspekte einer sicheren Software nicht in Betracht gezogen werden. Vielmehr soll eine Grundlage bzw. ein möglicher Einstiegspunkt für weitere Forschung an Methoden und Abläufen zum Testen von Open Source (Router) Software geschaffen werden.
<br><br>
[1] Bundesamt für Sicherheit in der Informationstechnik (Hrsg.), BSI TR-03148:Secure Broadband Router: Requirements for secure BroadbandRouters. [Online]. Verfügbar unter: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR03148/TR03148.pdf?__blob=publicationFile&v=3 (Letzter Zugriff: 11. August 2020).<br>
[2] OpenWrt Project, Statistical Overview. [Online]. Verfügbar unter: https://downloads.openwrt.org/stats/ (Letzter Zugriff: 13. Dezember 2020).<br>
[3] FACT Core. [Online]. Verfügbar unter: https://github.com/fkie-cad/FACT_core (Letzter Zugriff: 21. Dezember 2020).<br>
[4] Peter Weidenbach, Johannes vom Dorp, Home Router Security Report2020. [Online]. Verfügbar unter: https://www.fkie.fraunhofer.de/content/dam/fkie/de/documents/HomeRouter/HomeRouterSecurity_2020_Bericht.pdf (Letzter Zugriff: 11. August 2020).<br>

***

### Ordnerstruktur
📦Abschlussarbeit_H-BRS<br>
 ┣ 📂Bachelorarbeit **↤ Text of thesis / TR Results / Additional Figures**<br>
 ┃ ┣ 📂Figures<br>
 ┃ ┣ 📂Results **↤ TR results and additional data**<br>
 ┃ ┃ ┣ 📂TR.A **↤ Results of TR.A**<br>
 ┃ ┃ ┣ 📂TR.B<br>
 ┃ ┃ ┣ 📂...<br>
 ┃ ┃ ┣ 📂TR.J<br>
 ┃ ┃ ┣ 📂Test Environment **↤ Graphics describing the test environment** <br>
 ┃ ┃ ┣ 📜ssh-audit-consoleout.png<br>
 ┃ ┃ ┗ 📜ssh-audit_log.json<br>
 ┃ ┣ 📂Text **↤ Contains the thesis** <br>
 ┃ ┃ ┗ 📜Abschlussarbeit_Weckermann.docx<br>
 ┃ ┗ 📜Weckermann_ICS_and_Test Documentation.xlsx **↤ Filled in excel document for TR**<br>
 ┃<br>
 ┣ 📂Expose **↤ Contains the expose and Gant diagram**<br>
 ┃<br>
 ┣ 📂Firmware Images **↤ Contains multiple firmware images that were used**<br>
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
 ┃ ┗ 📜analysis.ods **↤ Analysis of the FACT results**<br>
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
 ┣ 📂Papers **↤ Papers that were used in this thesis**<br>
 ┃<br>
 ┣ 📂Prüfspezfikation und ergänzende Dokumente **↤ TR 03148, additional documents of TR, further papers that were referenced in TR 03148**<br>
 ┃<br>
 ┣ 📂Scripts **↤ Python and Bash scripts**<br>
 ┃<br>
 ┣ 📂Statistics **↤ OpenWrt download statistics from their websites for november, OpenWrt git statistics generated with gitstat**<br>
 ┃ ┣ 📂OpenWrt Download Statistics<br>
 ┃ ┗ 📂OpenWrt Git Statistics 26.10.20<br>
 ┃<br>
 ┣ 📜README.md<br>
 ┣ 📜henry_pub.asc<br>
 ┗ 📜security notes.txt<br>
