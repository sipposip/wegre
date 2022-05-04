import os

import pandas as pd
import numpy as np
from pylab import plt

from read_uav_data import read_uav_data

date = '20220503'
for flight_number in ('LOG03', 'LOG04', 'LOG05', 'LOG06', 'LOG07'):

    plotdir = 'plots/'
    os.makedirs(plotdir, exist_ok=True)

    ifile = f'{date}/{flight_number}.txt'

    df = read_uav_data(ifile)
    plt.figure()
    plt.scatter(df['lon'], df['lat'], c=df['t'])
    plt.plot(df['lon'], df['lat'])
    plt.savefig(f'{plotdir}/{date}-{flight_number}-lat-lon-p.svg')

    n_vars = df.shape[1]
    plt.figure(figsize=(10, 20))
    for i in range(n_vars):
        plt.subplot(n_vars, 1, i + 1)
        plt.plot(df[df.keys()[i]])
        plt.ylabel(df.keys()[i])
    plt.xlabel('step')
    plt.savefig(f'{plotdir}/{date}-{flight_number}-overviewplot.svg')
    plt.savefig(f'{plotdir}/{date}-{flight_number}-overviewplot.png')
