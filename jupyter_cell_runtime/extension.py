import time
from datetime import timedelta
from IPython.core.magic import Magics, magics_class, line_magic
from IPython import get_ipython
from colorama import Fore, Style

_start_time = None

# 默认灰色和标签
_color = "\033[38;5;245m"
_label = "执行时间"

color_map = {
    'gray': "\033[38;5;245m",
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE
}

def _pre_run_cell(info):
    global _start_time
    _start_time = time.time()

def _post_run_cell(result):
    global _start_time
    if _start_time is not None:
        elapsed = time.time() - _start_time
        elapsed_td = timedelta(seconds=elapsed)
        print(f"{_color}{_label}: {elapsed:.3f} 秒 | {elapsed_td}{Style.RESET_ALL}")

@magics_class
class JupyterCellRuntimeMagics(Magics):

    @line_magic
    def jupyter_cell_runtime(self, line):
        """
        用法:
            %jupyter_cell_runtime color red
            %jupyter_cell_runtime color \\033[38;5;245m
            %jupyter_cell_runtime label 耗时
        """
        global _color, _label
        args = line.strip().split(maxsplit=1)
        if len(args) == 2:
            key, value = args[0].lower(), args[1]
            if key == "color":
                # 支持预定义颜色或 ANSI 码
                if value.lower() in color_map:
                    _color = color_map[value.lower()]
                    print(f"jupyter-cell-runtime: 已将颜色设置为 {value}")
                elif value.startswith("\\033") or value.startswith("\033") or value.startswith("\x1b"):
                    # 解析 ANSI 转义码
                    _color = value.encode('utf-8').decode('unicode_escape')
                    print("jupyter-cell-runtime: 已将颜色设置为自定义 ANSI 码")
                else:
                    _color = color_map['gray']
                    print(f"jupyter-cell-runtime: 未识别颜色 '{value}'，已回退到默认灰色")
            elif key == "label":
                _label = value
                print(f"jupyter-cell-runtime: 已将输出文字设置为 '{value}'")
            else:
                print("用法: %jupyter_cell_runtime color [gray|red|...] 或 %jupyter_cell_runtime color <ANSI码> 或 %jupyter_cell_runtime label 文字")
        else:
            print("用法: %jupyter_cell_runtime color [gray|red|...] 或 %jupyter_cell_runtime color <ANSI码> 或 %jupyter_cell_runtime label 文字")

def load_ipython_extension(ipython=None):
    """Jupyter/IPython 自动加载入口"""
    if ipython is None:
        ipython = get_ipython()
    ipython.events.register('pre_run_cell', _pre_run_cell)
    ipython.events.register('post_run_cell', _post_run_cell)
    ipython.register_magics(JupyterCellRuntimeMagics)
    print("jupyter-cell-runtime 已加载：默认灰色，输出 '执行时间'\n用法: %jupyter_cell_runtime color red | %jupyter_cell_runtime color \\033[38;5;245m | %jupyter_cell_runtime label 耗时")

def unload_ipython_extension(ipython=None):
    """卸载扩展"""
    if ipython is None:
        ipython = get_ipython()
    try:
        ipython.events.unregister('pre_run_cell', _pre_run_cell)
        ipython.events.unregister('post_run_cell', _post_run_cell)
        print("jupyter-cell-runtime 已卸载")
    except ValueError:
        pass
