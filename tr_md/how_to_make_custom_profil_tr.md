

## Neden Özel Şablon Oluşturmalıyım?
Sistem servislerinin veya programların gereksizlik kriteri her bilgisayarda farklıdır.  

Örneğin, Bluetooth’u olmayan bir masaüstü bilgisayarda Bluetooth servisleri gereksizdir. Peki, Bluetooth varsa? O zaman o kullanıcı için gerekli olur.  

Bu nedenle, hazır bir şablon kullanmayın. Daima kendinize özel şablon yapmaya çalışın. Bu belgede bunu anlatacağız.

---

## Peki Neden Windows 10 LTSC Kullanmayayım?
Kullanabilirsiniz, kendi tercihiniz.  
Fakat LTSC sürümü telemetri özelliğini kapatmıyor, mahremiyetinize saygılı değil ve yine blood yazılımlar bulunuyor.  
Bu nedenle önerim, böyle bir script kullanmanız yönünde olacaktır. Ama karar sizde.

---

## general
Burada istediğiniz optimizasyon yöntemlerini koyabilirsiniz.  
Önemli olan bazı yöntemlerin advanced bölümlerine ihtiyacı olmasıdır.  
Eğer `activate_win10=true` yaparsanız, advanced bölümünde bazı ayarlara ihtiyacınız olacak.

---

## advanced
Burası farklı alt başlıklara ayrılır.  
General bölümünde de bahsedildiği gibi, eğer kullanmıyorsanız bu alt başlıkların hepsini silebilirsiniz.  
Bu sayede daha küçük bir `optimizer.toml` oluşturabilirsiniz.

---

## advanced sahip olmayanlar

### `dont_track_me`
Telemetri verilerini kapatır.  
Fakat tamamen kapatıp kapatmadığı her zaman şüphelidir çünkü Windows 10/11 kapalı kaynak.

### `temporary_files_remove`
Temp dosyalarını siler ve startup dosyalarını da temizler.

### `DEP`
Windows DEP (Data Execution Prevention) özelliğini kapatır.

---

## advanced sahip olanlar

### `advanced.activate_win10`
Windows’u **KMS (Key Management Service)** yöntemiyle etkinleştirmenizi sağlar.

#### Alt Değişkenler

- `win10_edition`  
  Windows sürümünü belirtir.  
  - `professional`  
  - `home`

- `kms_server`  
  KMS isteğinin gönderileceği sunucu adresi.  
  - Örnek: `kms.senin_kms_sunucun.com`

---

### `advanced.screen_resolution`
QRes.exe ile ekran çözünürlüğünüzü değiştirmenizi sağlar, ekran kartına binen yükü azaltır.

#### Alt Değişkenler

- `change_resolution_x`  
  Yatay alanı değiştirmek için piksel cinsinden değer.  
  - Örnek: 1920

- `change_resolution_y`  
  Dikey alanı değiştirmek için piksel cinsinden değer.  
  - Örnek: 1080

---

### `advanced.remove`
Blood (ön yüklü) programları/yazılımları silmek için kullanılır.  
Yanlış bir program silmemek için dikkatli olun.

#### Kullanım
PowerShell’de aşağıdaki komutu çalıştırın:

```powershell
Get-AppxPackage
````

Çıktıdaki **`Name`** alanlarını alın ve silmek istediğiniz paket adlarını kendi listenize ekleyin.

#### Alt Değişkenler

* `edge_remove`
  `true` veya `false` değerlerini alabilir.
  Microsoft Edge’in kaldırılmasını isteyip istemediğinizi belirtir.

* `programs_to_be_deleted`
  Bir liste değişkenidir.
  Silmek istediğiniz Appx paketlerinin **`Name`** değerlerini buraya ekleyin.

---

### `advanced.disable_unnecessary_services`

Gereksiz servisleri kaldırmanıza yarar.
Ne yaptığını biliyorsanız kullanın.

#### Kullanım

CMD’de aşağıdaki komutu çalıştırın:

```cmd
sc query
```

Çıktıdaki **`SERVICE_NAME`** alanlarını alın ve kapatmak istediğiniz servis adlarını kendi listenize ekleyin.

#### Alt Değişkenler

* `service_list`
  Bir liste değişkenidir.
  Kapatmak istediğiniz servislerin **`SERVICE_NAME`** değerlerini buraya ekleyin.

---

### `advanced.install_app`

İstediğiniz programları yazar, silinenlerin yerine yükler.

#### Alt Değişkenler

* `install_method`
  Yükleme metodunu belirtin.

  * Örnek: `winget`

* `programs_to_be_installed`
  Bir liste değişkenidir.
  Yüklemek istediğiniz programların isimlerini yazın.

  * Örnek: `KDE.KDEConnect`

---

### `advanced.dns`

DNS değiştirmek için kullanılır, bilgisayarınızın ve Wi-Fi bağlantınızın performansını bir miktar optimize eder.

#### Kullanım

Adapter nasıl belirlenecek:

```cmd
netsh interface show interface
```

Buradan almanız gereken yer **Interface Name**.

#### Alt Değişkenler

* `adapter_name`
  **Interface Name** buraya yazılacak.

* `dns_change`
  İstediğiniz DNS sunucusunu yazın.

  * Örnek: `1.1.1.1`
