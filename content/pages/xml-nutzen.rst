XML nutzen
##########
:date: 2007-10-14 10:23
:author: infram
:slug: xml-nutzen
:status: published

Martin Schaaf

| Version 0.1
| 2003-11-26

| Copyright © 2003 Martin Schaaf
| 1. Einleitung
| 1.1 XML?
| 1.2 Was ist XML nicht?
| 1.3 Anwendung und Vorteile von XML
| 1.3.1 Datenaustausch
| 1.3.2 Datenteillung/-bereitstellung
| 1.3.3 Datenspeicherung
| 1.3.4 XML erhöht den Nutzen meiner Daten
| 1.3.5 Neue Sprachen mit XML
| 1.4 Anwendungen nutzen XML
| 1.4.1 Anwendungsoberflächen mit Glade
| 1.4.2 Konvertierung eines XML-Dokumentes
| 1.4.3 Und mehr
| 2. XML erstellen
| 2.1 Aufbau von XML
| 2.1.1 Elemente?
| 2.1.2 Tags?
| 2.1.3 Attribute?
| 2.1.4 Entities?
| 2.1.5 PCDATA?
| 2.1.6 CDATA?
| 2.2 Elemente oder Attribute?
| 2.3 Gültiges XML
| 2.4 Namensräume
| 2.5 Zeichensatzkodierung
| 3. DTD
| 3.1 DTD?
| 3.2 Benötige ich eine DTD
| 3.3 Aufbau einer DTD
| 3.4 Deklaration von ...
| 3.4.1 Elementtypen
| 3.4.2 Attributen
| 3.4.3 Entities
| 4. XSL
| 4.1 XSL?
| 4.1.1 XSLT?
| 4.1.2 XPath?
| 4.1.3 Formatting Objects?
| 4.1.4 XLink?
| 4.1.5 Xpointer?
| 5. XSLT
| 5.1 Deklaration
| 5.2 XSLT-Elemente
| 5.2.1 xsl:template
| 5.2.2 xsl:value-of
| 5.2.3 xsl:for-each
| 5.2.4 xsl:sort
| 5.2.5 xsl:if
| 5.2.6 xsl:choose
| 5.2.7 xsl:apply-templates
| 5.3 XSLT-Element Referenz
| 5.4 XSLT-Funktionen
| 5.5 XSLT-Funktions Referenz
| 5.6 Beispiel

6. XPATH

| 7. Formatting Objects
| 8. XPointer
| 9. XLink

| 10. Referenzen
| 1. Einleitung

1.1 XML?

| XML (Extensible Markup Language) dient der Beschreibung von Seiten.
| Informationen können mit XML strukturiert, gespeichert und
  ausgetauscht werden und das Software und Hardware unabhängig. Es ist
  frei und erweiterbar. XML-Daten sind reine Text Dateien. Die
  XML-Syntax ist sehr genau, sehr einfach zu erlernen und sehr einfach
  anzuwenden. XML ist eine Vereinfachung von SGML.

1.2 Was ist XML nicht?

XML dient nicht der Datenanzeige, wie HTML, sondern es beschreibt Daten
und konzentriert sich darauf was Daten sind. XML ist keine Erweiterung
von HTML.

1.3 Anwendungen und Vorteile von XML

1.3.1 Datenaustausch

Heutige Computer Systeme und Datenbanken beinhalten Daten in nicht
kompatiblen Formaten. Es ist für Entwickler ein zeitaufwändiges
Unterfangen Daten zwischen solchen Systemen auszutauschen. Mit XML
können Sie diesen Aufwand reduzieren und Ihre Daten können von den
unterschiedlichsten Anwendungen gelesen werden.

1.3.2 Datenteillung/-bereitstellung

Durch die Speicherung der Daten als reine Textdateien hat man die
Möglichkeit die Daten Software und Hardware unabhängig bereitzustellen.
Dies erleichtert die Erstellung von Daten für unterschiedliche
Anwendungen und erleichtert die Aufrüstung oder Erweiterung von Systemen
auf ein neues Betriebssystem, Anwendungen, Browsern oder Servern.

1.3.3 Datenspeicherung

Mit XML speichern Sie Ihre Daten als reine Textdateien oder in
Datenbanken.

1.3.4 XML erhöht den Nutzen meiner Daten

Durch XML stehen Ihre Daten mehr Benutzern zur Verfügung, denn durch die
Unabhängigkeit von Hardware, Software und Anwendungen lassen sich Ihre
Daten nicht nur auf Standard-HTML-Browsern darstellen. Verschiedene
Anwendungen und Clients können auf Ihre XML-Dateien zugreifen, wie auf
Datenbanken. Ihre Daten können jeder “lesenden Maschine” (Agenten) zur
Verfügung gestellt werden und es ist einfacher Ihre Daten blinden
Menschen oder Menschen mit anderen Behinderungen zur Verfügung zu
stellen.

1.3.5 Neue Sprachen mit XML

Die Wireless Markup Language (WML) wurden in XML geschrieben.

1.4 Anwendungen die XML nutzen

1.4.1 Anwendungsoberflächen mit Glade

Glade ist ein GUI-Editor (Graphical User Interface) für die
Gtk+-Bibliothek. Sie wählen die Komponenten einer Anwendung aus z.B.:
das Hauptfenster und legen darauf 2 Buttons. Glade speichert diese
Angaben in einer XML-Datei. Man bindet die Glade-Datei später in sein
Programm ein und die Oberfläche wird dann anhand dieser Datei erstellt.
Dies bedeutet für den Programmierer eine einfache Trennung von Quellcode
für die Programmfunktionalität und dem Quellcode für die GUI was es ihm
erleichtert die Oberfläche auszutauschen. Bild 1.4-a zeigt eine GUI und
Listing 1 zeigt einen Auszug aus der dazugehörige Glade-Datei.

| Listing 1
| <?xml version=”1.0“?>
| <GTK-Interface>

<project>

::

     <name>Ploen</name>
     <program_name>ploen</program_name>
     <directory></directory>
     <source_directory>src</source_directory>
     <pixmaps_directory>pixmaps</pixmaps_directory>
     <language>C</language>
     <gnome_support>False</gnome_support>
     <gettext_support>True</gettext_support>
     <use_widget_names>True</use_widget_names>
     <gnome_help_support>True</gnome_help_support>
     <output_translatable_strings>True</output_translatable_strings>
     <translatable_strings_file>ploen.str</translatable_strings_file>

</project>

<widget>

::

     <class>GtkWindow</class>
     <name>p_main</name>
     <width>694</width>
     <height>511</height>
     <title>Ploen</title>
     <type>GTK_WINDOW_TOPLEVEL</type>
     <position>GTK_WIN_POS_NONE</position>
     <modal>False</modal>
     <allow_shrink>False</allow_shrink>
     <allow_grow>True</allow_grow>
     <auto_shrink>True</auto_shrink>
     <wmclass_name>ploen</wmclass_name>

::

     <widget>
       <class>GtkVBox</class>
       <name>vbox1</name>
       <homogeneous>False</homogeneous>
       <spacing>0</spacing>

::

       <widget>
         <class>GtkMenuBar</class>
         <name>ploen_menubar</name>
         <shadow_type>GTK_SHADOW_OUT</shadow_type>
         <child>

| <padding>0</padding>
| <expand>False</expand>
| <fill>False</fill>

::

         </child>

...

Bild 1.4-a: GUI erstellt mit Glade

1.4.2 Konvertierung eines XML-Dokumentes

Als Beispiel verwende ich die Dokumentationsdateien des Galeon-Browsers.
Es sind Docbook-Dateien, d.h. XML-Dateien mit der Document Type
Definition (DTD) Docbook in der Version 4.2. Als XML-Parser und
XSLT-Prozessor verwende ich Sablotron und libXSLT. Die XSL-Dateien zur
Konvertierung von XML in HTML stammen aus dem docbook-xsl-Paket.

| Konvertierung mit Sablotron:
| >sabcmd htmlhelp.xsl galeon.xml

| Konvertierung mit Sablotron:
| >xsltproc htmlhelp.xsl galeon.xml

1.4.3 Und mehr

| XSL-Prozessoren:
| - Sablotron
| - libXSLT

| Office-Suite:
| - Abiword - Textverarbeitung ()
| - GNumeric - Tabellenkalkulation ()
| - `OpenOffice <http://www.ma-scha.de/index.php?wiki=OpenOffice>`__
  (http://www.openoffice.org/)

| “HTML"-Browser
| - Amaya (http://www.w3c.org/)
| - Internet Explorer
| - Mozilla (http://www.mozilla.org/)

| Datenbanken:
| - dbXML (http://www.dbxml.org/overview.html)
| - Ozon-DB (http://www.ozon-db.org/)
| - Tamino (http://www.softwareag.com/tamino/)
| - X-Hive (http://www.x-hive.com/)

| Entwicklung:
| - Glade - GUI-Editor (http://glade.pn.org/)
| 2. XML erstellen

2.1 Aufbau von XML

Wie im letzten Kapitel schon erwähnt wurde, sind XML-Dateien reine
Textdateien. Die von jedem Text-Editor geöffnet, gelesen und geschrieben
werden können. In Listing 2 finden Sie ein einfaches Beispiel.

| Listing 2
| <?xml version=”1.0“ encoding="ISO-8859-1“?>
| <email>
| <to>f@p.com</to>
| </email>

Als erstes sollte das XML-Dokument eine XML-Deklaration besitzen, die
angibt, welche XML-Version und Zeichensatzkodierung das folgende
Dokument benutzt. Wie in HTML werden Daten durch
Identifizierungskennzeichen, sogenannte Tags, strukturiert und
beschrieben. Die in Listing 2 verwendeten Tags sind von mir selbst
definiert, denn XML gibt die Namen der Tags nicht vor. Hierbei wird
zwischen Groß- und Kleinschreibung unterschieden. Im Gegensatz zu HTML
müssen alle XML-Elemente einen schließenden Tag haben und das zuletzt
geöffnete Element muss als erstes Element geschlossen werden. Ein
XML-Dokument benötigt wenigstens ein Element, das Wurzel-Element
(Root-Element).

Beispiel

::

     <b><i></b></i>

| Falsch <b><i></i>
| Falsch <B><i></I></b>
| Falsch <b><i></i></b>
| Richtig <b><i/></b>
| Richtig

Warum ist das letzte Beispiel richtig? Es fehlt doch der schließende
Tag. XML erlaubt, wenn kein Inhalt zwischen den Tags auftritt, diese
Vereinfachung. Jedes XML-Dokument braucht ein Wurzelelement
(Root-Element). In Listing 2 ist “email” das Root-Element. Alle
möglichen Zeilenumbrüche werden in ein Zeilenvorschub (line-feed, #xA)
umgewandelt. Leerzeichen zwischen einem öffnenden und dem dazugehörigen
schließenden Tag werden nicht verkürzt. Kommentare werden wie in Listing
3 gezeigt angewendet.

| Listing 3
| <?xml version=”1.0“ encoding="ISO-8859-15“?>
| <!-- zu versendende E-Mail -->
| <email>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>f@p.com</to>
| <from>a@p.com</from>
| </email>

2.1.1 Elemente?

| Ein XML-Element besteht aus allem zwischen einschließlich Start- und
  einschließlich End-Tag, sind erweiterbar, haben Beziehungen
  untereinander und einfache Bennungsregeln.
| XML-Elemente haben Kind (child) und Eltern (parent) und Geschwister
  (siblings) Beziehungen. In Listing 3 ist “email” das Wurzel-Element.
  “to” und “from” sind Geschwister-Elemente, weil sie das gleiche
  Eltern-Element haben. “to” und “from” sind Kind-Elemente von “email”
  und “email” ist das Eltern-Element von “to” und “from”. Elemente
  können Text, andere Elemente enthalten oder leer sein.

| XML-Elemente können Attribute beinhalten und gemischten, einfachen
  oder leeren Inhalt haben.
| Gemischter Inhalt umfasst Text oder weitere Elemente. Einfacher Inhalt
  umfasst nur Text. Leerer Inhalt natürlich keins von beiden.

2.1.2 Tags?

Tags sind Identifizierungskennzeichen, die Elemente markieren. Es gibt
Start-Tags und Ende-Tags.

| Tag-Arten
| Start-Tag
| <tag>
| Ende-Tag
| </tag>
| Leerer-Tag
| <tag />

| Die Tags der Elemente können aus Zahlen, Buchstaben und anderen
  Zeichen bestehen. Dabei dürfen keine Zahlen oder Satzzeichen sowie die
  Buchstabenkombination “xml” am Anfang stehen. Es dürfen keine
  Leerzeichen auftreten. Vermeiden sie “-” und “.”. “:” wird für die
  Trennung von Namensräumen verwendet und sollte deshalb nicht im Tag
  vorkommen.
| Die Länge der Tags ist unbegrenzt, besser sind aber einfache kurze
  Tags.

2.1.3 Attribute?

Attribute finden ausschließlich in den Start-Tags Anwendung. Sie
beinhalten weitere Informationen zum Element. Die Werte der Attribute
müssen in " oder ' eingeschlossen werden. Listing 4 zeigt das Beispiel
aus Listing 3 um Attribute erweitert.

| Listing 4
| <?xml version=”1.0" encoding="ISO-8859-15“?>
| <!-- zu versendende E-Mail -->
| <email notify="true">
| <!-- E-Mail-Adresse des Empfängers -->
| <to name="Mr. Green">f@p.com</to>
| <!-- E-Mail-Adresse des Absenders -->
| <from name="Mr. Blue">a@p.com</from>
| </email>

2.1.4 Entities?

Wenn Sie von XML reservierte Zeichen verwenden, müssen Sie diese durch
Entity-Referenzen ersetzen. Entities sind Konstrukte die durch einen
XML-Prozessor ersetzt werden ähnlich einem Makro in C. Es sind zum
Beispiel zwischen den Tags keine <, >, &, ‘ und " erlaubt. Wobei das
aber nur so streng für < und & gilt. Die anderen Zeichen sollten, aber
trotzdem ersetzt werden. Nachfolgend finden Sie die vordefinierten
Entities.

| vordefinierte Entities
| &
| &
| <
| <
| >
| >
| '
| '
| "
| "

2.1.5 PCDATA?

PCDATA (parsed charakter data) sind die Bereiche eines XML-Dokumentes,
die vom XML-Prozessor analysiert werden. Tags werden in diesen Bereichen
als solche behandelt und Entities werden ersetzt.

2.1.6 CDATA?

CDATA (charakter data) sind die Bereiche eines XML-Dokumentes, die vom
XML-Prozessor nicht analysiert werden. Tags werden nicht als solche
behandelt und Entities werden nicht ersetzt. Die Markierung eines
Bereiches als CDATA geschieht auf folgende Weise.

| Deklaration
| <![CDATA[
| ...
| ]]>

| Nützlich ist diese Deklaration, wenn in einem Element häufig die
  Zeichen & oder < auftreten, so braucht man diese nicht durch ihre
  Entities ersetzen.
| Der CDATA-Bereich darf nicht die Zeichenkette "]]>" enthalten, was
  bedeutet das verschachtelte CDATA-Bereiche nicht erlaubt sind. Es
  dürfen auch keine White-Spaces in der Zeichenkette "]]>" auftreten.

2.2 Elemente oder Attribute?

Die Daten eines XML-Dokumentes können in Kind-Elementen oder in
Attributen gespeichert werden. Listing 5 zeigt das letzte Beispiel ohne
Attribute und Listing 6 die gleichen Daten ohne Kind-Elemente.

| Listing 5
| <?xml version=”1.0" encoding="ISO-8859-15“?>
| <!-- zu versendende E-Mail -->
| <email>
| <notify>true</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>f@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a@p.com</address>
| </from>
| </email>

| Listing 6
| <?xml version=”1.0" encoding="ISO-8859-15“?>
| <!-- zu versendende E-Mail -->
| <email notify="true" to="f@p.com” to\_name="Mr. Green” from="a@p.com”
  from\_name="Mr. blue"/>

Die Platzersparnis durch Listing 6 ist enorm, aber die Ersparnis an
Übersichtlichkeit ist noch höher. Attribute haben noch weitere Problem,
weshalb sie auch sehr sparsam verwendet werden sollten. Attribute können
nicht mehrere Werte haben , sind nicht einfach Erweiterbar, beschreiben
keine Struktur, sind schwer zu verändern durch eine Anwendung und sind
nicht einfach gegen eine DTD (Document Type Definition) zu testen. DTD’s
werden in einem späteren Kapitel besprochen. Attribute sollten zur
Speicherung von Metadaten dienen. Listing 7 zeigt eine mögliche
sinnvollere Anwendung von Attributen.

| Listing 7
| <?xml version=”1.0" encoding="ISO-8859-15“?>
| <!-- zu versendende E-Mail -->
| <email id="md5678“>
| <notify>true</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>f@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a@p.com</address>
| </from>
| </email>

2.3 Gültiges XML

Wenn es keine Vorgegebenen Tags gibt, wann ist dann ein XML-Dokument
gültig? Es gibt 2 Möglichkeiten. Wenn die Syntax-Regeln eingehalten
werden, handelt es sich um wohlgeformtes XML (well formed XML). Erst
wenn ein XML-Dokument mit einer vordefinierten Dokumentenstruktur (DTD)
übereinstimmt handelt es sich um gültiges XML. Jeder Fehler in einem
XML-Dokument muss den XML-Prozessor stoppen.

2.4 Namensräume

| Wenn 2 XML-Dokumente gleiche Tag-Namen haben, kann es beim
  zusammenfügen dieser beiden Dokumente zu Namenskonflikten kommen.
| In Listing 7 bezeichnet der Tag “email” eine E-Mail mit Empfgänger,
  Absender usw. In Listing 8 bezeichnet er nur die E-Mail-Adresse. Ein
  sinnvolles zusammenfügen ist nicht möglich.

| Listing 8
| <?xml version=”1.0" encoding="ISO-8859-15“?>
| <email>f@p.com</email>

Mit Präfixen für XML-Tags schafft man sich Namensräume in denen ein
schon vergebener Tag-Name eine neue Bedeutung erhalten kann. Listing 9
zeigt Listing 8 mit Präfix.

| Listing 9
| <?xml version=”1.0" encoding="ISO-8859-15“?>
| <a:email xmlns:a="http://www.ma-scha.de/xml/email/">f@p.com</a:email>

Der Präfix (in Listing 9 ein “a”) wird dem Tag-Namen mit einem
anschließenden Doppelpunkt vorangestellt. Das xmlns-Attribut weist dem
Namensraum-Präfix einen Namensraum-Namen zu. Der Namensraum-Name muss
eine URI sein. In Listing 9 wurde der Namensraum-Präfix explizit
angegeben. Um die Schreiben des Präfixes zu vermeiden kann man einen
Standard-Namensraum festlegen indem man den : und den Präfix vom
xmlns-Attribut weglässt. Der Standard-Namensraum gilt für das Element in
dem der Namensraum deklariert wurde und alle eingeschlossenen Elemente
ohne Präfix befinden sich in diesem. Der Standard Namensraum gilt aber
nicht automatisch für die Attribute.

2.5 Zeichensatzkodierung

| Wie in den Beispielen immer angegeben erlaubt uns XML die
  Zeichensatzkodierung des Dokumentes anzugeben. Diese sollten Sie auch
  immer angeben damit auf anderen Systemen, als dem erstellten alle
  Zeichen des Dokumentes korrekt gelesen und später dargestellt werden
  können.
| Beispiele für Kodierungen sind UTF-8, UTF-16, ISO-8895-n (n ist die
  Nummer eines Teils) usw. Bei fehlender Zeichensatzkodierung wird UTF-8
  angenommen.
| 3. DTD

3.1 DTD?

Die Document Type Definition (DTD) ist eine formale Grammatik, die eine
bestimmte XML-Sprache definiert. Sie definiert die Dokumenten-Struktur
mit erlaubten Tags und deren Schachtelung.

3.2 Benötige ich eine DTD

DTD's können sehr nützlich sein, wenn unabhängige Gruppen Daten
untereinander austauschen müssen. Eine Anwendung kann DTD's nutzen, um
Daten von außerhalb validieren zu können. Mit einer DTD kann ein
XML-Dokumente eine Beschreibung seines eigenen Formates mitbringen.

3.3 Aufbau einer DTD

DTD's kann man innerhalb oder außerhalb von XML-Dokumenten definieren.
Listing 10 zeigt das XML-Dokument aus Listing 7 mit interner DTD.

| Listing 10
| <?xml version="1.0" encoding="ISO-8859-15“?>
| <!DOCTYPE email [
| <!ELEMENT email (notify, to, from)>
| <!ELEMENT notify (#PCDATA)>
| <!ELEMENT to (name \| address)>
| <!ELEMENT from (name \| address)>
| <!ELEMENT name (#PCDATA)>
| <!ELEMENT adress (#PCDATA)>
| <!ATTLIST email id ID #REQUIRED>
| ]>
| <!-- zu versendende E-Mail -->
| <email id="md5678“>
| <notify>true</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>f@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a@p.com</address>
| </from>
| </email>

Listing 11 zeigt die DTD als externe Definition und Listing 12, die DTD
in ein XML-Dokument eingebunden.

| Listing 11
| <!ELEMENT email (notify, to, from)>
| <!ELEMENT notify (#PCDATA)>
| <!ELEMENT to (name \| address)>
| <!ELEMENT from (name \| address)>
| <!ELEMENT name (#PCDATA)>
| <!ELEMENT adress (#PCDATA)>
| <!ATTLIST email id ID #REQUIRED>

| Listing 12
| <?xml version="1.0" encoding="ISO-8859-15“?>
| <!DOCTYPE email SYSTEM "listing11.dtd">
| <!-- zu versendende E-Mail -->
| <email id="md5678“>
| <notify>true</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>f@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a@p.com</address>
| </from>
| </email>

3.4 Deklaration von ...

3.4.1 Elementtypen

| Elementtyp-Deklarationen
| <!ELEMENT element\_name element\_kategorie>
| <!ELEMENT element\_name (element\_inhalt)>

Jeder Elementtyp darf nur einmal deklariert werden.

| Element-Kategorien
| EMPTY
| leeres Element
| ANY
| jede Kombination von Daten

| Element-Inhalt
| #PCDATA
| "parsed charakter data" - Zeichendaten die vom XML-Prozessor
  durchsucht werden
| kind1\_name,kind2\_name,...
| -notwendige Kind-Elemente
| -notwendige Reihenfolge
| -Kind-Elemente dürfen nur einmal vorkommen
| kind1\_namekind2\_name...
| entweder kind1 oder kind2 oder ...
| kind\_name+
| muss mindestens einmal vorkommen
| kind\_name\*
| 0 oder öfters vorkommen
| kind\_name?
| 0 oder einmal vorkommen
| #PCDATAchild1\_namechild2\_name\|...
| Zeichendaten und Kind-Elemente mit beliebiger Anzahl und Reihenfolge
  der Kind-Elemente

3.4.2 Attributen

| Attribut-Deklaration
| <!ATTLIST element\_name attribut\_name attribut\_typ vorgabe\_wert>

| Attribut-Typen
| CDATA
| Zeichendaten, die nicht analysiert (unparsed) werden
| (abc\|...)
| ein Wert aus einer Aufzählungsliste
| ID
| -Wert muss eindeutig sein;
| -darf nur einmal auftreten pro Element
| -muss Vorgabe-Wert #IMPLIED oder #REQUIRED haben
| IDREF
| Wert eines ID-Attributes aus dem Dokument
| IDREFS
| Liste von ID-Attribute-Werten gtrennt durch White-Space
| NMTOKEN
| (Buchstabe Zahl . - \_ \| :)+
| (genauer siehe REC-XML)
| NMTOKENS
| Liste von NMTOKEN-Werten getrennt durch White-Space
| ENTITY
| Name eines nicht analysierten (unparsed) Entities aus der DTD
| ENTITIES
| Liste von ENTITY-Werten getrennt durch White-Space

| Vorgabe-Werte
| #REQUIRED
| muss im Element vorhanden sein
| #IMPLIED
| muss nicht angegeben werden
| #FIXED wert
| fester Attribut-Wert
| wert
| Vorgabe-Wert eines Attributes

3.4.3 Entities

| Entity-Deklaration
| <!ENTITY entity\_name entity\_wert>
| <!ENTITY entity\_name SYSTEM URI/URL>
| <!ENTITY entity\_name PUBLIC öffentliche\_id URI/URL>

4. XSL

4.1 XSL?

XSL (Extensible Stylesheet Language) ist eine Sprache zum umformen von
XML-Dokumenten. Mit XSL kann man XML-Daten filtern und sortieren, XML
formatieren anhand der Daten-Werte (z.B. negative Zahlen rot darstellen)
und XML-Daten auf verschiedenen Geräten ausgeben.

4.1.1 XSLT?

| XSLT (XSL Transformations) dient dem definieren von XML-Umformungen.
| XSLT benutzt XPath, um Teile des Quelldokumentes zu definieren, die
  vordefinierten Templates entsprechen. Wenn Übereinstimmung gefunden
  wird formt XSLT den gefundenen Teil zum Ergebnisdokument um.

4.1.2 XPath?

Xpath dient der Definition von Übereinstimmungs-Mustern für die
Umformungen.

4.1.3 Formatting Objects?

4.1.4 XLink?

| 4.1.5 Xpointer?
| 5. XSLT

5.1 Deklaration

| Style-Sheet-Deklaration
| <xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
| <xsl:transform version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

5.2 Elemente

5.2.1 xsl:template

Jedes <xsl:template>-Element enthält Regeln, die auf die ausgewählten
Tags angewendet werden. Bezeichnet werden sie als Schablone (template).

| ...
| <xsl:template match="/">
| <html>
| <body>
| </body>
| </html>
| </xsl:template>
| ...

| Das match-Attribut assoziert die Schablone mit einem XML-Element. Der
  Wert "/" bezeichnet das Wurzel-Element und somit das ganze Dokument.
| Dieser Wert ist ein XPath-Ausdruck, der auch in anderen Elementen
  Anwendung findet.

5.2.2 xsl:value-of

Das <xsl:value-of>-Element extrahiert Werte eines gewählten Elementes
und fügt es in die Ausgabe ein.

| ...
| <td><xsl:value-of select="liste/name"/></td>
| ...

5.2.3 xsl:for-each

Mit diesem Element kann man jedes XML-element eines gewählten Tags
auswählen.

| ...
| <xsl:for-each select="liste">
| <tr>
| <td><xsl:value-of select="name"/></td>
| </tr>
| </xsl:for-each>
| ...

5.2.4 xsl:sort

Diese Element erlaubt die Sortierung von XML-Elementen.

| ...
| <xsl:for-each select="liste">
| <xsl:sort select="name"/>
| <tr>
| <td><xsl:value-of select="name"/></td>
| </tr>
| </xsl:for-each>
| ...

5.2.5 xsl:if

Auswahl von Elementen die bestimmten Bedingungen folgen.

| ...
| <xsl:for-each select="liste">
| <xsl:sort select="name"/>
| <tr>
| <xsl:if test="position() mod 2 = 0">
| <td><xsl:value-of select="name"/></td>
| </xsl:if>
| </tr>
| </xsl:for-each>
| ...

5.2.6 xsl:choose

Wenn verschiedene Bedingungen von Elementen getestet werden soll.

| ...
| <xsl:for-each select="liste">
| <xsl:sort select="name"/>
| <tr>
| <xsl:choose>
| <xsl:when test="age > 10">
| <td color="green"><xsl:value-of select="name"/></td>
| </xsl:when>
| <xsl:when test="age = 5">
| <td color="blue"><xsl:value-of select="name"/></td>
| </xsl:when>
| <xsl:otherwise>
| <td color="black"><xsl:value-of select="name"/></td>
| </xsl:otherwise>
| </xsl:choose>
| </tr>
| </xsl:for-each>
| ...

5.2.7 xsl:apply-templates

Es erlaubt eine Schablone auf das aktuelle Element oder auf dessen
Kinder-Elemente anzuwenden. Es erlaubt die XSL-Datei zu strukturieren.

| ...
| <xsl:template match="/">
| <html>
| <body>
| <xsl:apply-templates>
| <xsl:sort select="name"/>
| </xsl:apply-templates>
| </body>
| </html>
| </xsl:template>

| <xsl:template match="liste">
| <tr>
| <xsl:if test="position() mod 2 = 0">
| <td><xsl:value-of select="name"/></td>
| </xsl:if>
| <tr>
| </xsl:template>
| ...

5.3 XSLT-Element Referenz

| Name
| Beschreibung
| xsl:apply-imports
| wendet eine Schablone aus einer importierten XSL-Datei an
| xsl:attribute
| hinzufügen eines Attributes
| xsl:attribute-set
| definiert einen Namen für einen Satz von Attributen
| xsl:call-template
| ruft eine bestimmte Schablone auf
| xsl:choose
| erlaubt mehrere Bedingungen
| xsl:comment
| erzeugt einen Kommentar-Element im Ergebnis
| xsl:copy
| erzeugt eine Kopie des aktuellen Elementes (ohne Kinder-Elemente und
  Attribute)
| xsl:copy-of
| erzeugt eine Kopie des aktuellen Elementes (mit Kinder-Elementen und
  Attributen)
| xsl:decimal-format
| beschreibt ein Dezimalformat, das von der format-number() Funktion
  benutzt wird
| xsl:element
| erzeugt ein Element in der Ausgabe
| xsl:fallback
| gibt alternativen Code an, der ausgeführt wird wenn der XSL-Prozessor
  ein XSL-Element nicht unterstützt
| xsl:for-each
| Läuft durch alle Elemente eines angegebenen Elementes
| xsl:if
| eine Bedingung
| xsl:import
| importiert den Inhalt einer Formatvorlage in eine andere
| xsl:include
| bindet den Inhalt einer Formatvorlage in eine andere ein
| xsl:key
| bezeichnet einen Schlüssel, der mit der key() Funktion benutzt werden
  kann
| xsl:message
| gibt Nachrichten aus
| xsl:namespace-alias
| ersetzt einen Namensraum aus der Formatvorlage mit einem anderen im
  Ergebnis
| xsl:number
| fügt eine Zsahl formatiert im Ergebnis ein
| xsl:otherwise
| gibt eine Standardaktion für das <xsl:choose>- Element an
| xsl:output
| definiert das Ausgabeformat des Dokumentes
| xsl:param
| deklariert einen globalen oder lokalen Parameter
| xsl:preserve-space
| definiert Elemente die White-Spaces behalten
| xsl:processing-instruction
| schreibt eine Prozessanweisung in die Ausgabe
| xsl:strip-space
| definiert Elemente von denen White-Spaces entfernt werden
| xsl:stylesheet
| definiert das Wurzel-Element einer Formatvorlage
| xsl:text
| gibt Text aus
| xsl:transform
| definiert das Wurzel-Element einer Formatvorlage
| xsl:value-of
| fügt den Wert eines gewählten Elementes ein
| xsl:variable
| deklariert eine lokale oder globale Variable
| xsl:when
| gibt eine Aktion für das <xsl:choose>- Element an
| xsl:with-param
| definiert den Wert eines Parameters, der einer Schablone übergeben
  wird

5.4 XSLT Funktionen

5.5 XSLT-Funktions Referenz

| Name
| Beschreibung
| current()
| gibt das aktuelle Element zurück
| document()
| Zugriff auf Elemente aus externen XML-Dokumenten
| element-available()
| prüft ob das angegebene Elemente vom XSLT-Prozessor unterstützt wird
| format-number()
| konvertiert eine Zahl in eine Zeichenkette
| function-available()
| prüft ob die angegebene Funktion vom XSLT-Prozessor unterstützt wird
| generate-id()
| gibt eine Zeichenkette zurück, die eindeutig ein Element identifiziert
| key()
| gibt Elemente zu einem passenden Schlüssel zurück
| system-property()
| gibt den Wert der Systemeigenschaften zurück?
| unparsed-entity-uri()
| gibt die URI eines nicht analysierten Entities zurück

5.6 Beispiel

| Listing 13
| <!ELEMENT mailbox (email\*)>
| <!ELEMENT email (notify,to+,from,content,date)>
| <!ATTLIST email id ID #REQUIRED>
| <!ELEMENT notify (#PCDATA)>
| <!ELEMENT to (name, address)>
| <!ELEMENT from (name, address)>
| <!ELEMENT content (#PCDATA)>
| <!ELEMENT date (#PCDATA)>
| <!ELEMENT name (#PCDATA)>
| <!ELEMENT address (#PCDATA)>

| Listing 14
| <?xml version="1.0" encoding="ISO-8859-15"?>
| <!DOCTYPE mailbox SYSTEM "listing13.dtd">
| <mailbox>
| <email id="md5677">
| <notify>1</notify>
| <!-- E-Mail-Adresse des 1. Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>f@p.com</address>
| </to>
| <!-- E-Mail-Adresse des 2. Empfängers -->
| <to>
| <name>Mr. Grey</name>
| <address>tz@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a@p.com</address>
| </from>
| <content>
| inhalt1
| </content>
| <date>2003-12-12</date>
| </email>
| <email id="md5678">
| <notify>0</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. ÄÄÄh</name>
| <address>f1@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a1@p.com</address>
| </from>
| <content>
| inhalt2
| </content>
| <date>2003-12-11</date>
| </email>
| <email id="md5679">
| <notify>1</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>f2@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a2@p.com</address>
| </from>
| <content>
| inhalt3
| </content>
| <date>2004-01-7</date>
| </email>
| <email id="md5680">
| <notify>0</notify>
| <!-- E-Mail-Adresse des Empfängers -->
| <to>
| <name>Mr. Green</name>
| <address>3f@p.com</address>
| </to>
| <!-- E-Mail-Adresse des Absenders -->
| <from>
| <name>Mr. Blue</name>
| <address>a3@p.com</address>
| </from>
| <content>
| inhalt4
| </content>
| <date>2004-01-3</date>
| </email>
| </mailbox>

| Listing 15
| <?xml version="1.0" encoding="ISO-8859-15"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"/>

<xsl:template match="/">

::

       <html>
       <head>
       </head>
       <body>

<xsl:apply-templates/>

::

       </body>
       </html>

</xsl:template>

<xsl:template match="mailbox">

::

       <table>
           <tr>

| <th colspan="2">Ihre E-Mails</th>
| </tr>

::

           <xsl:apply-templates select="email">

| <xsl:sort order="descending" select="date"/>
| </xsl:apply-templates>

::

       </table>

</xsl:template>

<xsl:template match="email">

::

       <tr>
           <td>Datum:</td>

<td><xsl:value-of select="date"/></td>

::

       </tr>
       <tr>

<td>Von:</td>

::

           <td><xsl:value-of select="from/name"/> <<xsl:value-of select="from/address"/>></td>
       </tr>
       <xsl:apply-templates select="to"/>
       <tr>

<td><xsl:text disable-output-escaping="yes">Bestätigung:</xsl:text></td>

::

           <xsl:choose>

| <xsl:when test="notify = 1">
| <td>Ja</td>
| </xsl:when>
| <xsl:otherwise>
| <td>Nein</td>
| </xsl:otherwise>
| </xsl:choose>

::

       </tr>
       <tr>

<td colspan="2"><xsl:value-of select="content"/></td>

::

       </tr>

</xsl:template>

<xsl:template match="to">

::

       <tr>
           <td>An:</td>

<td><xsl:value-of select="name"/> <<xsl:value-of
select="address"/>></td>

::

       </tr>

</xsl:template>

</xsl:stylesheet>

Listing 13 zeigt ein DTD, welches man zum Speichern von E-Mails benutzen
kann. Listing 14 zeigt ein zu Listing 13 gültiges XML-Dokument. Und
Listing 15 zeigt eine XSL-Datei mit deren Hilfe wir eine HTML-Dokument
aus Listing 14 erzeugen. Wir schicken die 3 Dateien durch den
XSL-Prozessor und erhalten als Ausgabe Listing 16.

| Listing 16
| <html>
| <head><meta http-equiv="Content-Type" content="text/html;
  charset=UTF-8"></head>
| <body><table>
| <tr><th colspan="2">Ihre E-Mails</th></tr>
| <tr>
| <td>Datum:</td>
| <td>2004-01-7</td>
| </tr>
| <tr>
| <td>Von:</td>
| <td>Mr. Blue <a2@p.com></td>
| </tr>
| <tr>
| <td>An:</td>
| <td>Mr. Green <f2@p.com></td>
| </tr>
| <tr>
| <td>Bestätigung:</td>
| <td>Ja</td>
| </tr>
| <tr><td colspan="2">
| inhalt3
| </td></tr>
| <tr>
| <td>Datum:</td>
| <td>2004-01-3</td>
| </tr>
| <tr>
| <td>Von:</td>
| <td>Mr. Blue <a3@p.com></td>
| </tr>
| <tr>
| <td>An:</td>
| <td>Mr. Green <3f@p.com></td>
| </tr>
| <tr>
| <td>Bestätigung:</td>
| <td>Nein</td>
| </tr>
| <tr><td colspan="2">
| inhalt4
| </td></tr>
| <tr>
| <td>Datum:</td>
| <td>2003-12-12</td>
| </tr>
| <tr>
| <td>Von:</td>
| <td>Mr. Blue <a@p.com></td>
| </tr>
| <tr>
| <td>An:</td>
| <td>Mr. Green <f@p.com></td>
| </tr>
| <tr>
| <td>An:</td>
| <td>Mr. Grey <tz@p.com></td>
| </tr>
| <tr>
| <td>Bestätigung:</td>
| <td>Ja</td>
| </tr>
| <tr><td colspan="2">
| inhalt1
| </td></tr>
| <tr>
| <td>Datum:</td>
| <td>2003-12-11</td>
| </tr>
| <tr>
| <td>Von:</td>
| <td>Mr. Blue <a1@p.com></td>
| </tr>
| <tr>
| <td>An:</td>
| <td>Mr. Ã„Ã„Ã„h <f1@p.com></td>
| </tr>
| <tr>
| <td>Bestätigung:</td>
| <td>Nein</td>
| </tr>
| <tr><td colspan="2">
| inhalt2
| </td></tr>
| </table></body>
| </html>

6. XPath

10. Referenzen

| Folgende Web-Seiten dienten mir als Grundlage für dieses Tutorial.
| http://www.w3c.org/
| http://www.w3schools.com/
