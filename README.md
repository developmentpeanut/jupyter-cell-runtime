# jupyter-cell-runtime

一个轻量级的 Jupyter / IPython 单元执行计时扩展，可以在每个 Notebook 单元格执行后自动显示耗时。支持自定义颜色与输出文字。
无需依赖旧版本 pandas，完全兼容 Python 3.7+ 和最新版 Jupyter。

---

## 功能特点

- **自动计时**：每次运行单元格后自动打印耗时  
- **轻量无依赖**：只依赖 IPython (>=7.0)  
- **简单易用**：通过 `%load_ext jupyter_cell_runtime` 一键开启  
- **自动打印运行时间**（秒数 + timedelta）
- **可修改输出颜色**（支持常用颜色名和 ANSI 转义码）
- **可修改输出文字标签**

---

## 安装

pip install 安装：
```bash
pip install git+https://github.com/developmentpeanut/jupyter-cell-runtime.git
```

或从源码安装:
```bash
pip install jupyter-cell-runtime-0.1.0.zip
```

或git 安装：
```bash
git clone https://github.com/developmentpeanut/jupyter-cell-runtime.git
cd jupyter-cell-runtime
pip install .
```

或从源码安装：
```bash
unzip jupyter-cell-runtime-0.1.0.zip
cd jupyter-cell-runtime
pip install .
```

## 自动加载扩展 - VS Code 自动加载扩展
1. 打开 VS Code 设置（快捷键：`Ctrl + ,` 或 `Cmd + ,`）。
2. 搜索 `Jupyter: Run Startup Commands`。
3. 点击“在 settings.json 中编辑”（或手动打开设置文件）。
4. 在 `settings.json` 中添加以下内容：
   ```json
   "jupyter.runStartupCommands": [
       "%load_ext jupyter_cell_runtime"
   ]
   ```
5. 保存后重启 Jupyter Kernel。


## 使用方法

### 1. 加载扩展
```python
%load_ext jupyter_cell_runtime
```
加载后，每个单元执行完都会自动打印运行时间。

### 2. 修改颜色
可使用内置颜色：
```python
%jupyter_cell_runtime color red
%jupyter_cell_runtime color cyan
%jupyter_cell_runtime color green
%jupyter_cell_runtime color gray
```

也可使用 ANSI 转义码：
```python
%jupyter_cell_runtime color \033[38;5;245m   # 自定义灰色
%jupyter_cell_runtime color \033[38;5;214m   # 橙色
```

### 3. 修改输出文字
可将默认的“执行时间”替换成任意文字：
```python
%jupyter_cell_runtime label 耗时
%jupyter_cell_runtime label 运行时间
%jupyter_cell_runtime label ExecutionTime
```

### 4. 卸载扩展
若不再需要计时功能：
```python
%unload_ext jupyter_cell_runtime
```

```bash
pip uninstall jupyter-cell-runtime -y
```

## 输出示例

默认输出：
```
执行时间: 0.123 秒 | 0:00:00.123000
```

修改颜色与文字后：
```
耗时: 1.234 秒 | 0:00:01.234000   （红色）
```

## 功能特性
- 自动为每个单元计时  
- 同时显示秒数与 timedelta 格式  
- 颜色可通过名称或 ANSI 码自定义  
- 输出文字可自定义，支持多语言  
- 无外部依赖，轻量易安装  

## License
MIT License
