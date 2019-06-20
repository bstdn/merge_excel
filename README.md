# Merge excel

## 检查是否安装python

```
python --version
```

- 下载地址 https://www.python.org/getit/

## 检查是否安装pip

```
pip --version
```

- 下载地址 https://pypi.org/project/pip/

## 使用虚拟环境

- 与系统的Python解释器分开，在项目中的私有副本

### 安装

- 检查virtualenv

```
$ virtualenv -- version
```

- 安装virtualenv

```
$ sudo pip install virtualenv
```

- 新建一个文件夹作为项目目录
- 按照惯例，一般虚拟环境会被命名为 venv

```
virtualenv venv
New python executable in venv/bin/python
Installing distribute......done.
Installing pip.............done.
```

- 可指定python版本

```
virtualenv venv --python=python2.7
virtualenv venv --python=python3.5
```

- 激活这个虚拟环境

```
source venv/bin/activate
```

- 为了提醒你已经激活了虚拟环境，激活虚拟环境的 命令会修改命令行提示符，加入环境名

```
(venv) $
```

- 回到全局 Python 解释器

```
deactivate
```

## 如何使用

- 安装该项目中所需要的所有Python包

```
(venv) $ pip install -r requirements.txt
```

- 将需要合并的xls文件，放到 data 目录下
- 运行如下命令

```
(venv) $ python merge.py
```

- 合并后文件 data/result.csv
