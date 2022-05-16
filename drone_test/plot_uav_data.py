import os

import pandas as pd
import numpy as np
from pylab import plt
from mpl_toolkits import mplot3d

from read_uav_data import read_imet_data

date = '20220503'
for flight_number in ('LOG03', 'LOG04', 'LOG05', 'LOG06', 'LOG07'):

    plotdir = 'plots/'
    os.makedirs(plotdir, exist_ok=True)

    ifile = f'{date}/{flight_number}.txt'

    df = read_imet_data(ifile)
    plt.figure()
    plt.scatter(df['lon'], df['lat'], c=df['t'])
    plt.colorbar()
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

# more details for log06
flight_number = "LOG06"
ifile = f'{date}/{flight_number}.txt'

df = read_imet_data(ifile)
# remove all "weird" lat and lons
df = df.query('lon > 180')
plt.figure()
plt.scatter(df['lon'], df['lat'], c=df['alt'])
cb = plt.colorbar()
cb.set_label('alt')
plt.plot(df['lon'], df['lat'])
plt.savefig(f'{plotdir}/{date}-{flight_number}-lat-lon-alt_detailed.svg')

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')
ax.grid()
ax.plot3D(df['lon'], df['lat'], df['alt'])
cf = ax.scatter(df['lon'], df['lat'], df['alt'], c=df['t'], cmap=plt.cm.Reds)
ax.set_xlabel('lon')
ax.set_ylabel('lat')
ax.set_zlabel('alt')
cb = plt.colorbar(cf)
cb.set_label('t')
plt.savefig(f'{plotdir}/{date}-{flight_number}-3D-lat-lon-alt-t_detailed.svg')

n_vars = df.shape[1]
plt.figure(figsize=(10, 20))
for i in range(n_vars):
    plt.subplot(n_vars, 1, i + 1)
    plt.plot(df[df.keys()[i]])
    plt.ylabel(df.keys()[i])
plt.xlabel('step')
plt.savefig(f'{plotdir}/{date}-{flight_number}-overviewplot-onlyvalid.svg')
plt.savefig(f'{plotdir}/{date}-{flight_number}-overviewplot-onlyvalid.png')
