import numpy 
import h5py as h5
import matplotlib.pyplot as plt 
from datetime import datetime
from dateutil.relativedelta import relativedelta 
import h5py as h5

import os 

def create_directory(path):

    if not os.path.isdir(path):
        os.makedirs(path)




def make_patch(t,h,data,d_horas,d_rango):  

    patchs = []
    
    for i in range(18): # eje x
        for j in range(4): # eje y
    
            valid = True
            
            patch = data[d_rango*j: (j+1)*d_rango,d_horas*(i):d_horas*(i+1)]
            patch = patch.copy()

    
            threshold = d_horas*d_rango * 0.5
            count_nan = numpy.count_nonzero(numpy.isnan(patch))
            
            if(count_nan>threshold):
    
                # creamos una mascara vacia 
                patch = numpy.zeros((d_rango,d_horas))
                valid = False
    
            elif (count_nan>0):
                mask = numpy.isnan(patch)
                patch[mask] = 0 ## or another value 

            ### padding 14x14 
            patch = numpy.pad(
                patch,
                pad_width=((1, 1), (2, 2)),
                mode='constant',
                constant_values=0
            )
            
            patchs.append((t[d_horas*(i):d_horas*(i+1)],
                          h[d_rango*j: (j+1)*d_rango],patch,i,j,valid))

    return patchs 

def retrive_data(df_,i_t,f_t):


    hmin =260
    hmax = 855
    
    df = df_.loc[
        df_["time"].between(
            i_t,
            f_t
        )
]

    df = df.loc[
        df["height"].between(
            hmin,
            hmax
        )
]

    matrix = df.pivot(
        index="height",
        columns="time",
        values="value"
    )

    t = matrix.columns.to_numpy()
    h = matrix.index.to_numpy()
    data = matrix.to_numpy()

    return t,h,data


def print_structure(name, obj):
    print(name)


def load_file(filename):
    with h5.File(filename, "r") as f:

        try:
            data = f["Data/Array Layout/2D Parameters/paiwl"][:]
            
        except:
            data = f["Data/Array Layout/2D Parameters/jro33"][:]
        finally:
            h = f["/Data/Array Layout/range"][:]
            t = f["/Data/Array Layout/timestamps"][:]

        t = [datetime.fromtimestamp(x) + relativedelta(hours=-5) for x in t ]
    return t,h,data


"""


fig = plt.figure(figsize=(16,9),dpi=90)

ax = fig.add_subplot(1,1,1)

data = data[:,235:]

t = numpy.arange(t)*15

h = data.shape[1]
h = numpy.arange(h)

ax.set_ylim(200,950)
cc = ax.pcolormesh(h,t,data,cmap='jet',vmin=0,vmax=7, )





cbar = plt.colorbar(cc,ax=ax,cmap='jet')
fig.tight_layout()

fig.savefig("spread.png",dpi=110)


"""