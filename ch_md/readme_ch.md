![Python](https://badgen.net/badge/icon/3.12.0?icon=https://www.svgrepo.com/show/452091/python.svg&label=python)

适用于 Windows 10/11 的全面优化工具

## 使用方法

首先，你需要一个 `optimizer.toml` 文件。程序已经自带一个 `optimizer.toml` 文件。你可以通过查看这个 [例子](https://github.com/cem-ali152/winoptimize-tools/blob/main/default.toml) 创建自己的文件，或者查看 [这个](how_to_make_custom_profil_ch.md)。然后，你只需要：

![demo](https://raw.githubusercontent.com/cem-ali152/winoptimize-tools/refs/heads/main/demo_1.png))

```cmd
Winoptimizer.exe —cf your_optimizer.toml
````

就这么简单！！

## 代码编译

首先，你需要安装 **Python 3.12**（目前尚未测试其他版本）。 建议你创建一个 **Python 虚拟环境**（例如 `conda` 或 `venv`）。

进入虚拟环境后，安装必要的依赖项：

```cmd
pip install -r requirements.txt
```

这样代码就可以运行了。

如果你想创建一个 **可执行文件**，可以使用以下命令：

```cmd
pip install pyinstaller & pyinstaller main.py
```

## 使用条款

如果你不知道你在做什么，请不要创建你自己的 optimizer.toml 文件。
使用 Windows 时，如果遇到任何错误，概不负责。

## 支持

如果你想支持这个项目并帮助它成长，即使是小额捐款也可以。
记住，这个项目正在你的贡献下发展。

