![Python](https://badgen.net/badge/icon/3.12.0?icon=https://www.svgrepo.com/show/452091/python.svg&label=python)

Windows 10/11 için kapsamlı bir optimizasyon aracı

## Kullanım
Öncelikle bir `optimizer.toml` dosyanız olması gerekiyor. Program zaten bir `optimizer.toml` ile geliyor. ![Bu](https://github.com/cem-ali152/winoptimize-tools/blob/main/default.toml) örneği inceleyerek kendi dosyanızı oluşturabilirsiniz yada [bunu](how_to_make_custom_profil_tr.md) inceleyebilirsiniz Ardından, tek yapmanız gereken:

![demo](https://raw.githubusercontent.com/cem-ali152/winoptimize-tools/refs/heads/main/demo_1.png))

```cmd
Winoptimizer.exe —cf your_optimizer.toml
````

Hepsi bu kadar!!
## Kodu Derleme

Öncelikle **Python 3.12** kurulu olmalıdır (farklı bir sürüm şu an test edilmemiştir). Tercihen bir **Python sanal ortamı** oluşturmanız önerilir (örneğin `conda` veya `venv`).

Sanal ortama girdikten sonra, gerekli bağımlılıkları yükleyin:

```cmd
pip install -r requirements.txt
```

Böylece kod çalıştırılabilir hale gelecektir.

İsterseniz, **çalıştırılabilir dosya** oluşturmak için aşağıdaki komutu kullanabilirsiniz:

```cmd
pip install pyinstaller & pyinstaller main.py
```


## Kullanım Şartları

Ne yaptığınızı bilmiyorsanız, lütfen kendi optimizer.toml dosyanızı oluşturmayın.
Windows kullanırken herhangi bir hata ile karşılaşırsanız, hiçbir koşulda sorumluluk kabul edilmeyecektir.

## Destek

Projeyi desteklemek ve büyümesine yardımcı olmak isterseniz, küçük bir bağış bile yapabilirsiniz.
Unutmayın, bu proje sizlerin katkılarıyla gelişiyor.

