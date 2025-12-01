## Warum sollte ich eine eigene Vorlage erstellen?

Die Kriterien für unnötige Systemdienste oder Programme sind bei jedem Computer unterschiedlich.

Zum Beispiel sind Bluetooth-Dienste auf einem Desktop-Computer ohne Bluetooth überflüssig. Aber was, wenn Bluetooth vorhanden ist? Dann ist es für diesen Benutzer notwendig.

Deshalb sollten Sie keine fertige Vorlage verwenden. Versuchen Sie immer, eine eigene Vorlage zu erstellen. In diesem Dokument wird erklärt, wie das geht.

---

## Warum sollte ich Windows 10 LTSC nicht verwenden?

Sie können es verwenden, das ist Ihre Entscheidung.
Allerdings deaktiviert die LTSC-Version die Telemetrie nicht, respektiert Ihre Privatsphäre nicht vollständig und enthält weiterhin vorinstallierte „Blood“-Programme.
Deshalb empfehle ich, ein solches Skript zu verwenden. Aber die Entscheidung liegt bei Ihnen.

---

## general

Hier können Sie die gewünschten Optimierungsmethoden einfügen.
Wichtig ist, dass einige Methoden die Unterabschnitte in **advanced** benötigen.
Wenn Sie `activate_win10=true` setzen, werden Sie einige Einstellungen im Advanced-Bereich benötigen.

---

## advanced

Dieser Abschnitt ist in verschiedene Unterabschnitte unterteilt.
Wie im General-Bereich erwähnt, können Sie, wenn Sie sie nicht verwenden, alle Unterabschnitte löschen.
So können Sie eine kleinere `optimizer.toml` erstellen.

---

## Ohne advanced-Unterabschnitte

### `dont_track_me`

Deaktiviert Telemetriedaten.
Ob sie vollständig deaktiviert werden, ist jedoch nicht immer sicher, da Windows 10/11 Closed-Source ist.

### `temporary_files_remove`

Löscht temporäre Dateien und bereinigt auch Startdateien.

### `DEP`

Deaktiviert die Windows-DEP-Funktion (Data Execution Prevention).

---

## Mit advanced-Unterabschnitten

### `advanced.activate_win10`

Ermöglicht die Aktivierung von Windows über **KMS (Key Management Service)**.

#### Untervariablen

* `win10_edition`
  Gibt die Windows-Version an.

  * `professional`
  * `home`

* `kms_server`
  Die Adresse des Servers, an den die KMS-Anfrage gesendet wird.

  * Beispiel: `kms.dein_kms_server.com`

---

### `advanced.screen_resolution`

Ermöglicht die Änderung der Bildschirmauflösung mit QRes.exe und reduziert die Belastung der Grafikkarte.

#### Untervariablen

* `change_resolution_x`
  Wert in Pixeln für die horizontale Auflösung.

  * Beispiel: 1920

* `change_resolution_y`
  Wert in Pixeln für die vertikale Auflösung.

  * Beispiel: 1080

---

### `advanced.remove`

Wird verwendet, um vorinstallierte „Blood“-Programme/Apps zu löschen.
Seien Sie vorsichtig, um keine falschen Programme zu entfernen.

#### Verwendung

Führen Sie in PowerShell folgenden Befehl aus:

```powershell
Get-AppxPackage
```

Nehmen Sie die **`Name`**-Felder aus der Ausgabe und fügen Sie die zu löschenden Paketnamen in Ihre Liste ein.

#### Untervariablen

* `edge_remove`
  Kann `true` oder `false` sein.
  Gibt an, ob Microsoft Edge entfernt werden soll.

* `programs_to_be_deleted`
  Eine Listenvariable.
  Fügen Sie hier die **`Name`**-Werte der zu löschenden Appx-Pakete ein.

---

### `advanced.disable_unnecessary_services`

Ermöglicht das Deaktivieren unnötiger Dienste.
Nur verwenden, wenn Sie wissen, was Sie tun.

#### Verwendung

Führen Sie in CMD folgenden Befehl aus:

```cmd
sc query
```

Nehmen Sie die **`SERVICE_NAME`**-Felder aus der Ausgabe und fügen Sie die zu deaktivierenden Dienste in Ihre Liste ein.

#### Untervariablen

* `service_list`
  Eine Listenvariable.
  Fügen Sie hier die **`SERVICE_NAME`**-Werte der zu deaktivierenden Dienste ein.

---

### `advanced.install_app`

Schreibt die gewünschten Programme und installiert sie anstelle der gelöschten.

#### Untervariablen

* `install_method`
  Gibt die Installationsmethode an.

  * Beispiel: `winget`

* `programs_to_be_installed`
  Eine Listenvariable.
  Schreiben Sie hier die Namen der zu installierenden Programme.

  * Beispiel: `KDE.KDEConnect`

---

### `advanced.dns`

Wird verwendet, um den DNS zu ändern und die Leistung Ihres Computers und Ihrer Wi-Fi-Verbindung leicht zu optimieren.

#### Verwendung

So bestimmen Sie den Adapter:

```cmd
netsh interface show interface
```

Nehmen Sie den **Interface-Namen** von hier.

#### Untervariablen

* `adapter_name`
  Der **Interface-Name** wird hier eingetragen.

* `dns_change`
  Geben Sie den gewünschten DNS-Server ein.

  * Beispiel: `1.1.1.1`

---

Wenn Sie wollen, kann ich den gesamten Abschnitt zusätzlich noch so formatieren, dass er direkt als `optimizer.toml`-Dokument in Deutsch nutzbar ist, mit allen Kommentaren übersetzt.

Brauchst du, dass ich das mache?
