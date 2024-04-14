

### 4.12

报错信息：

```cmd
命令语法不正确。
```

定位：`lib/evaluators/img_fit.py`

```python
os.system('mkdir -p ' + cfg.result_dir)
os.system('mkdir -p ' + cfg.result_dir + '/vis')
```

原因：原代码采用linux命令行方式创建文件夹，Windows系统下需要更改，使用`os.makedirs`函数来创建目录，这个函数在所有操作系统中都可以工作。并且，它有一个`exist_ok`参数，如果设置为`True`，那么当目录已经存在时，函数不会抛出异常

```python
# os.system('mkdir -p ' + cfg.result_dir)
# os.system('mkdir -p ' + cfg.result_dir + '/vis')
os.makedirs(cfg.result_dir, exist_ok=True)
os.makedirs(os.path.join(cfg.result_dir, 'vis'), exist_ok=True)
```



### 4.13

报错信息：

```cmd
Can't pickle <class 'lib.datasets.img_fit.synthetic.Dataset'>: it's not the same object as lib.datasets.img_fit.synthetic.Dataset
```

定位:`lib/trainers/trainer.py`

```python
# Get one batch of data
dataiter = iter(data_loader)
```

