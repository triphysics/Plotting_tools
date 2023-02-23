#!/usr/bin/python
import numpy as np
import h5py

# only change this line which give name of hdf5 file
# this is grid thermal conductivity file of TDEP

f1=h5py.File("63.hdf5")
fp_list=f1['frequencies'].shape
qp=fp_list[0]
fp=fp_list[1]
rp=qp*fp

print(qp, fp)
toTHz=1/1E12/2/np.pi
ps=1e12
ang=1e10
freq=f1['frequencies'][:,:]*toTHz
tau1 = f1['lifetimes'][:,:]*ps
mfp1 = f1['mean_free_paths'][:,:]*ang
vx1 = f1['group_velocities'][:,:,0]
vy1 = f1['group_velocities'][:,:,1]
vz1 = f1['group_velocities'][:,:,2]
v_avg = np.sqrt((vx1**2)+(vy1**2)+(vz1**2))


freq=np.reshape(freq, rp)
tau1 = np.reshape(tau1, rp)
mfp1= np.reshape(mfp1, rp)
vx1 = np.reshape(vx1, rp)
vy1 = np.reshape(vy1, rp)
vz1 = np.reshape(vz1, rp)
v_avg = np.reshape(v_avg, rp)

data_tau=np.vstack([freq, tau1])
data_mfp=np.vstack([freq, mfp1])
data_vx=np.vstack([freq, abs(vx1)])
data_vy=np.vstack([freq, abs(vy1)])
data_vz=np.vstack([freq, abs(vz1)])
data_vavg=np.vstack([freq, v_avg])

np.savetxt("Tau.dat", data_tau.T, fmt="%.8e", header="F(Thz)          tau(ps)")
np.savetxt("MFP.dat", data_mfp.T, fmt="%.8e", header="F(Thz)          mfp(Ang)")
np.savetxt("Velocity_x.dat", data_vx.T, fmt="%.8e", header="F(Thz)        vx(m/s)")
np.savetxt("Velocity_y.dat", data_vy.T, fmt="%.8e", header="F(Thz)        vy(m/s)")
np.savetxt("Velocity_z.dat", data_vz.T, fmt="%.8e", header="F(Thz)        vz(m/s)")
np.savetxt("Velocity_avg.dat", data_vavg.T, fmt="%.8e", header="F(Thz)      v_avg(m/s)")
