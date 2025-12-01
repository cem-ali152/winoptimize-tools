## 为什么要创建自定义模板？

系统服务或程序是否多余在每台计算机上标准不同。

例如，没有蓝牙的台式机上蓝牙服务是多余的。但如果有蓝牙呢？那对该用户来说就是必要的。

因此，请不要使用现成模板。始终尝试创建自己的自定义模板。本文档将讲解如何操作。

---

## 为什么不使用 Windows 10 LTSC？

您可以使用，这是您的选择。
但是 LTSC 版本不会关闭遥测功能，不尊重您的隐私，并且仍然包含“Blood”预装程序。
因此，我建议使用此类脚本。但最终决定权在您。

---

## general

在这里可以放置您想要的优化方法。
重要的是，有些方法需要 advanced 部分的支持。
如果您设置了 `activate_win10=true`，则需要在 advanced 部分进行一些配置。

---

## advanced

本部分分为多个子部分。
如 general 部分所述，如果不使用这些功能，可以删除所有子部分。
这样可以创建更小的 `optimizer.toml` 文件。

---

## 没有 advanced 子部分的功能

### `dont_track_me`

关闭遥测数据。
但由于 Windows 10/11 为闭源系统，是否完全关闭始终存在不确定性。

### `temporary_files_remove`

删除临时文件，同时清理启动文件。

### `DEP`

关闭 Windows DEP（数据执行保护）功能。

---

## 包含 advanced 子部分的功能

### `advanced.activate_win10`

允许通过 **KMS（Key Management Service）** 激活 Windows。

#### 子变量

* `win10_edition`
  指定 Windows 版本。

  * `professional`
  * `home`

* `kms_server`
  KMS 请求要发送的服务器地址。

  * 示例: `kms.senin_kms_sunucun.com`

---

### `advanced.screen_resolution`

允许使用 QRes.exe 更改屏幕分辨率，降低显卡负载。

#### 子变量

* `change_resolution_x`
  水平分辨率的像素值。

  * 示例: 1920

* `change_resolution_y`
  垂直分辨率的像素值。

  * 示例: 1080

---

### `advanced.remove`

用于删除预装的“Blood”程序/应用。
操作时请小心，以免误删程序。

#### 使用方法

在 PowerShell 中运行以下命令：

```powershell
Get-AppxPackage
```

获取输出中的 **`Name`** 字段，并将要删除的软件包名称添加到您的列表中。

#### 子变量

* `edge_remove`
  可设置为 `true` 或 `false`。
  指定是否删除 Microsoft Edge。

* `programs_to_be_deleted`
  列表变量。
  将要删除的 Appx 软件包的 **`Name`** 值添加到这里。

---

### `advanced.disable_unnecessary_services`

允许禁用不必要的服务。
请在清楚操作后使用。

#### 使用方法

在 CMD 中运行以下命令：

```cmd
sc query
```

获取输出中的 **`SERVICE_NAME`** 字段，并将要禁用的服务名称添加到您的列表中。

#### 子变量

* `service_list`
  列表变量。
  将要禁用的服务的 **`SERVICE_NAME`** 值添加到这里。

---

### `advanced.install_app`

写入您想要安装的程序，并替代被删除的程序。

#### 子变量

* `install_method`
  指定安装方法。

  * 示例: `winget`

* `programs_to_be_installed`
  列表变量。
  写入您要安装的程序名称。

  * 示例: `KDE.KDEConnect`

---

### `advanced.dns`

用于更改 DNS，可在一定程度上优化计算机和 Wi-Fi 连接的性能。

#### 使用方法

如何确定适配器：

```cmd
netsh interface show interface
```

从中获取 **Interface Name**。

#### 子变量

* `adapter_name`
  **Interface Name** 填写在这里。

* `dns_change`
  输入您想要使用的 DNS 服务器。

  * 示例: `1.1.1.1`
