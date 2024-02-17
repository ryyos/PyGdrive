import os
import click
from time import perf_counter

from src import Gdrive

class Main:

    @click.command('share')
    @click.option('--source', '-sc', required=True, type=str)
    def share(source: str):

        gd = Gdrive()
        gd.main(source)


if __name__=='__main__':
    main = Main()
    main.share()