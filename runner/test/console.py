#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Author: hufeng.mao@carota.ai
Date: 2022-06-18 22:00:13
LastEditors: hufeng.mao@carota.ai
LastEditTime: 2022-06-18 22:03:01
'''
from time import sleep
from rich.console import Console
from rich.progress import Progress
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table

__version__ = '1.0.0'
__author__ = 'hufeng.mao@carota.ai'

console = Console()

def main():
    
    if console.is_terminal:
        with console.status("Working..."):
            for i in range(101):
                sleep(0.05)
        with Progress() as progress:
            task = progress.add_task("[blue]Downloading...", total=100)
            for i in range(101):
                sleep(0.1)
                progress.update(task, advance=1)
    else:
        for i in range(101):
            sleep(0.1)
            console.print(f"update progress: {i}%", style="red")

        for i in range(101):
            sleep(0.1)
            console.print(f"hide update progress: {i}%",  style="red")

if __name__ == '__main__':
    main()