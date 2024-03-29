# runner

* [README.en](https://github.com/notmmao/runner/blob/master/README.md)

## 介绍

`runner`是一个`可配置的`快速启动器,用于`启动(运行)`常用的`命令(程序)`.
它附带了`log`输出界面,方便用户`查看(染色)`和`保存`log.并且特殊格式的log输出还能驱动程序绘制`进度条`.

![主界面](https://i.ibb.co/CtZ55GP/main.png)

## 安装

> pip install -r requirements.txt

or

> pip install qtrunner

目前只在`windwos`平台测试过, 推荐使用`python 3.7`版本.

## 启动

- python runner.py 从使用代码中启动
- runner 直接启动

## 配置

### 主配置文件

config.json
```json
{
    "maxLogLines": 1000,        // log 最大行数
    "maxStdout": 40960,         // stdout 最大输出块
    "defaultEncoding": "gbk",   // stdout 默认编码
    "configs": [                // 子配置项
        {
            "file": "runner_common.json",   // 子配置文件
            "title": "通用(测试)"            // 子配置ui显示的名字
        }
    ]
}
```

### 子配置文件

runner_xxxx.json
```js
[
    {
        "title": "切换codepage到gbk(慎用)",  // ui上显示的名称
        "cmd": "cmd /c  chcp 936",          // 命令行
        "encoding": "gbk",                  // 对应的输出编码(可选)
        "qss": "color: rgb(150, 0, 0);",    // ui上对应的样式(可选)
        "cwd": "",                          // 命令启动的工作目录(可选,默认当前)
        "env": {                            // 命令启动的环境变量(可选, 0.0.6版本支持)
            "GP_LANGUAGE": "zh_CN"
        }
    }
]
```
