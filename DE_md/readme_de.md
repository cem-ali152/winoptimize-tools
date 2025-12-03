![Python](https://badgen.net/badge/icon/3.12.0?icon=https://www.svgrepo.com/show/452091/python.svg&label=python)

Umfassendes Optimierungstool für Windows 10/11

## Verwendung
Zuerst benötigen Sie eine `optimizer.toml` Datei. Das Programm wird bereits mit einer `optimizer.toml` ausgeliefert. Sie können Ihre eigene Datei erstellen, indem Sie sich [dieses](https://github.com/cem-ali152/winoptimize-tools/blob/main/default.toml) Beispiel ansehen, oder [dieses](how_to_make_custom_profil_de.md) lesen. Danach müssen Sie nur noch:

![demo](https://raw.githubusercontent.com/cem-ali152/winoptimize-tools/refs/heads/main/demo_1.png))

```cmd
Winoptimizer.exe —cf deine_optimizer.toml
````

Das ist alles!!
## Code kompilieren

Zuerst muss **Python 3.12** installiert sein (eine andere Version wurde derzeit nicht getestet). Es wird empfohlen, eine **Python-Virtual Environment** zu erstellen (z.B. `conda` oder `venv`).

Nachdem Sie das Virtual Environment aktiviert haben, installieren Sie die benötigten Abhängigkeiten:

```cmd
pip install -r requirements.txt
```

Damit ist der Code ausführbar.

Wenn Sie möchten, können Sie mit dem folgenden Befehl eine **ausführbare Datei** erstellen:

```cmd
pip install pyinstaller & pyinstaller main.py
```

## Nutzungsbedingungen

Bitte erstellen Sie keine eigene optimizer.toml-Datei, wenn Sie nicht wissen, was Sie tun.
Es wird unter keinen Umständen eine Haftung übernommen, wenn bei der Verwendung von Windows Fehler auftreten.

## Unterstützung

Wenn Sie das Projekt unterstützen und dessen Wachstum fördern möchten, können Sie auch eine kleine Spende tätigen.
Denken Sie daran, dass sich dieses Projekt durch Ihre Beiträge weiterentwickelt.

