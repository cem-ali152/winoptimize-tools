
## Why Should I Create a Custom Template?
The criteria for unnecessary system services or programs vary on each computer.  

For example, on a desktop without Bluetooth, Bluetooth services are unnecessary. But if Bluetooth exists, then it becomes necessary for that user.  

Therefore, do not use a ready-made template. Always try to create your own custom template. This document will explain how to do that.

---

## Why Shouldn't I Use Windows 10 LTSC?
You can use it if you want; it’s your choice.  
However, the LTSC version does not disable telemetry, is not privacy-respecting, and still contains pre-installed bloatware.  
For this reason, my recommendation is to use a script like this. But the final decision is yours.

---

## general
Here, you can place the optimization methods you want.  
It is important to note that some methods may require advanced settings.  
If you set `activate_win10=true`, you will need certain settings in the advanced section.

---

## advanced
This section is divided into different subcategories.  
As mentioned in the general section, if you are not using these, you can remove all subcategories.  
This allows you to create a smaller `optimizer.toml`.

---

## Advanced Features for Non-Required Users

### `dont_track_me`
Disables telemetry data.  
However, it is always uncertain whether it completely disables telemetry since Windows 10/11 is closed source.

### `temporary_files_remove`
Deletes temporary files and also cleans startup items.

### `DEP`
Disables Windows DEP (Data Execution Prevention) feature.

---

## Advanced Features for Required Users

### `advanced.activate_win10`
Allows you to activate Windows using the **KMS (Key Management Service)** method.

#### Sub-Variables

- `win10_edition`  
  Specifies the Windows edition.  
  - `professional`  
  - `home`

- `kms_server`  
  The server address to which the KMS request will be sent.  
  - Example: `kms.your_kms_server.com`

---

### `advanced.screen_resolution`
Allows you to change your screen resolution using QRes.exe, reducing the load on your graphics card.

#### Sub-Variables

- `change_resolution_x`  
  The horizontal resolution in pixels.  
  - Example: 1920

- `change_resolution_y`  
  The vertical resolution in pixels.  
  - Example: 1080

---

### `advanced.remove`
Used to remove pre-installed (“bloat”) programs.  
Be careful not to delete important programs.

#### Usage
Run the following command in PowerShell:

```powershell
Get-AppxPackage
````

Take the **`Name`** fields from the output and add the packages you want to delete to your own list.

#### Sub-Variables

* `edge_remove`
  Can be `true` or `false`.
  Specifies whether to remove Microsoft Edge.

* `programs_to_be_deleted`
  A list variable.
  Add the **`Name`** values of the Appx packages you want to remove here.

---

### `advanced.disable_unnecessary_services`

Used to remove unnecessary services.
Use only if you know what you are doing.

#### Usage

Run the following command in CMD:

```cmd
sc query
```

Take the **`SERVICE_NAME`** fields from the output and add the services you want to disable to your list.

#### Sub-Variables

* `service_list`
  A list variable.
  Add the **`SERVICE_NAME`** values of the services you want to disable here.

---

### `advanced.install_app`

Installs the programs you want, replacing those that were removed.

#### Sub-Variables

* `install_method`
  Specify the installation method.

  * Example: `winget`

* `programs_to_be_installed`
  A list variable.
  Enter the names of the programs you want to install.

  * Example: `KDE.KDEConnect`

---

### `advanced.dns`

Used to change DNS, which can slightly optimize your computer and Wi-Fi performance.

#### Usage

To determine the adapter:

```cmd
netsh interface show interface
```

From the output, take the **Interface Name**.

#### Sub-Variables

* `adapter_name`
  Write the **Interface Name** here.

* `dns_change`
  Enter the DNS server you want to use.

  * Example: `1.1.1.1`

