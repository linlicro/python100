# Python编程环境(Mac OS)

以下使用Mac的VS Code作为Python的开发环境。

前置条件，安装`python3`，操作方式: `brew install python3`。

第一步，安装Python extension for VS Code<https://marketplace.visualstudio.com/items?itemName=ms-python.python>插件:

![](https://ws3.sinaimg.cn/large/006tNc79ly1g2yuboa7qvj31yq0loqcf.jpg)

第二步，选择一个Python解释器，告诉VS Code使用Python3解释器。

![](https://ws4.sinaimg.cn/large/006tNc79ly1g2yuc0n8bmj30s408eq4w.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79ly1g2yuccisjjj31ds0hgqap.jpg)

## Run Hello World

新建`hello.py`，输入代码:

```python
msg = "Hello World"
print(msg)
```

右击`运行`代码:

![](https://ws2.sinaimg.cn/large/006tNc79ly1g2yucq88lkj30sk074abh.jpg)

## Configure and run the debugger

设置断点:

![](https://ws3.sinaimg.cn/large/006tNc79ly1g2yud1v8jpj30dc0540t0.jpg)

下一步，点击`Debug`开始调试。调试之前，先要设置配置，这里选择`Python File`。

几个快捷键: 

* begin/continue (`F5`)
* step over (`F10`) 
* step into (`F11`)
* step out (`⇧F11`)
* restart (`⇧⌘F5`)
* stop (`⇧F5`)
 

## Install and use packages

运行下述代码`standardplot.py`，前需安装相关包:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
```

推荐使用虚拟环境:

> A best practice among Python developers is to avoid installing packages into a global interpreter environment. You instead use a project-specific virtual environment that contains a copy of a global interpreter. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions

* step1. Create and activate the virtual environment

```
python3 -m venv env
source env/bin/activate
```

* step2. Install the packages

```
python3 -m pip install matplotlib
```

* step3. 重新选择Python解释器

![](https://ws3.sinaimg.cn/large/006tNc79ly1g2yudf9x9lj30zu0fstb7.jpg)

* 运行，并显示一个绘画窗口。

#### 参考

* Getting Started with Python in VS Code <https://code.visualstudio.com/docs/python/python-tutorial>