#!/usr/bin/python
import numpy as np
import h5py
import pandas as pd

# only change this line which give name of hdf5 file
# change f1 and f2 here
f1=h5py.File("outfile.cumulative_kappa.hdf5")
f2=h5py.File("outfile.grid_thermal_conductivity.hdf5")
xx=f1['temperature_1']

fp_list=f2['frequencies'].shape

qp=fp_list[0]
fp=fp_list[1]
rp=qp*fp

toTHz=1/1E12/2/np.pi
freq=xx['frequency_axis'][:]#*toTHz
sk1=xx['spectral_kappa_vs_frequency_per_direction'][0,0,:] #xx
sk2=xx['spectral_kappa_vs_frequency_per_direction'][1,1,:] #yy
sk3=xx['spectral_kappa_vs_frequency_per_direction'][2,2,:] #yy

data_sk1=np.vstack([freq, sk1, sk2, sk3])

np.savetxt("Spectral_kappa_tensor.dat", data_sk1.T, fmt="%.8e", header="F(Thz)          sk_xx       sk_yy         sk_zz")

#cumulative part we will make from mode thermal conductivity data 
#from grid_thermal_conductivity file
#and make cumulation 

freq_n=f2['frequencies'][:,:]*toTHz
mode_kxx=f2['thermal_conductivity'][:,:,0,0]
mode_kyy=f2['thermal_conductivity'][:,:,1,1]
mode_kzz=f2['thermal_conductivity'][:,:,2,2]

# reshape to make modal kappa table
freq_n=np.reshape(freq_n, rp)
mode_kxx=np.reshape(mode_kxx, rp)
mode_kyy=np.reshape(mode_kyy, rp)
mode_kzz=np.reshape(mode_kzz, rp)

# save modal kappa as a data frame
data_mode_k={'Freq' : freq_n,
             'mode_kxx' : mode_kxx,
             'mode_kyy' : mode_kyy,
             'mode_kzz' : mode_kzz
             }
df = pd.DataFrame(data_mode_k)
df = df.sort_values(by=['Freq'])

# Make cumulation
df['cumlative_kxx'] = df['mode_kxx'].cumsum()/qp
df['cumlative_kyy'] = df['mode_kyy'].cumsum()/qp
df['cumlative_kzz'] = df['mode_kzz'].cumsum()/qp
df2 = df[['Freq', 'cumlative_kxx', 'cumlative_kyy', 'cumlative_kzz']]
df2.to_csv('cumlative_kappa_tensor.dat',  index=False, sep=' ', header=True)
