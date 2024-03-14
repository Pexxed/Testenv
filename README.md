Simple Calculator Flask Application Documentation
Übersicht
Diese Flask-Anwendung stellt einen einfachen Web-Taschenrechner bereit, mit dem Benutzer grundlegende mathematische Operationen ausführen können: Addition, Subtraktion, Multiplikation und Division. Die Anwendung bietet eine Web-basierte Benutzeroberfläche, auf der Benutzer zwei Zahlen eingeben und die gewünschte Operation auswählen können.

main.py
Importierte Module
Flask: Das Flask-Framework wird für die Webanwendung verwendet.
request: Wird verwendet, um auf die über die GET-Anfrage übergebenen Daten zuzugreifen.
rendertemplate: Ermöglicht das Rendern von HTML-Templates.
Flask-App-Instanz
Eine Instanz der Flask-Klasse wird erstellt, die als Webanwendung dient.

Routen
Index-Route (/)
Route: /
Funktion: index()
Methode: GET
Beschreibung: Rendert die index.html-Vorlage, die das Formular für den Taschenrechner enthält.
Calculate-Route (/calculate)
Route: /calculate
Funktion: calculate()
Methode: GET
Beschreibung: Empfängt die Eingaben num1, num2 und operation aus dem Formular, führt die entsprechende mathematische Operation durch und gibt das Ergebnis zurück. Im Fehlerfall wird eine entsprechende Nachricht zurückgegeben.
Error Handling
Division durch Null: Wenn num2 gleich Null ist und die Operation divide ist, gibt die Funktion eine Fehlermeldung zurück.
Ungültige Operation: Wenn eine andere als die definierten Operationen (add, subtract, multiply, divide) angefordert wird, gibt die Funktion eine Fehlermeldung zurück.
Serverausführung
Wenn die Datei als Hauptprogramm ausgeführt wird, startet die Anwendung einen lokalen Entwicklungs-Server, der auf alle Netzwerkinterfaces hört (host='0.0.0.0') und auf Port 80 läuft.

index.html
Struktur
Das HTML-Dokument enthält ein einfaches Formular, das für die Eingabe der Zahlen und die Auswahl der Operation genutzt wird.

Formular
Methode: GET
Action: /calculate
Eingabefelder für zwei Zahlen (num1 und num2) und ein Dropdown-Menü für die Auswahl der Operation.
Ein "Calculate"-Button sendet die Eingaben an den Server zur Berechnung.
Styling
Das HTML-Dokument hat kein spezifisches CSS eingebunden und verwendet das Standard-Styling des Browsers.

Verwendung
Um die Anwendung zu benutzen, öffnen Sie einen Webbrowser und gehen Sie zur Startseite der Flask-Anwendung. Geben Sie Zahlen in die beiden Felder ein und wählen Sie die gewünschte Operation aus dem Dropdown-Menü. Klicken Sie auf "Calculate", um das Ergebnis der Berechnung anzuzeigen.

Lokale Entwicklung
Um die Anwendung lokal zu entwickeln und zu testen, stellen Sie sicher, dass Sie Python und Flask installiert haben. Führen Sie das Skript main.py aus, um den Entwicklungsserver zu starten.

Bitte beachten Sie, dass dieser Prototyp für Demonstrationszwecke gedacht ist und keine vollständige Fehlerprüfung oder Sicherheitsmaßnahmen beinhaltet. In einem Produktionsumfeld sollten weitere Sicherheits- und Validierungsmechanismen implementiert werden.
