# make a general def to plot stuff in matplotlib

import matplotlib.pyplot as plt
def plot_something(x, y, **kwargs):
    title  = kwargs.pop( 'title'  )
    xlabel = kwargs.pop( 'xlabel' )
    ylabel = kwargs.pop( 'ylabel' )
    plt.figure()
    plt.plot(x, y, **kwargs)
    fig = plt.gcf()
    for axis in fig.axes:
        axis.set_title( title )
        axis.xaxis.set_label_text( xlabel )
        axis.yaxis.set_label_text( ylabel )
    return axis


plot_conf = {'title': 'Blabla', 'xlabel':'Time (s)', 'ylabel': 'Speed (m/s)'}
x = [1.,2.,3.]
y = [1.,4.,9.]
axis = plot_something(x=x,y=y, **plot_conf)
