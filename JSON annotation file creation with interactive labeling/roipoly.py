'''Draw polygon regions of interest (ROIs) in matplotlib images,
similar to Matlab's roipoly function.
See the file example.py for an application.
Created by Joerg Doepfert 2014 based on code posted by Daniel
Kornhauser.
'''
import numpy as np
import sys
import matplotlib.pyplot as plt

class roipoly:

    def __init__(self, fig=[], ax=[], roicolor='b'):
        if fig == []:
            fig = plt.gcf()

        if ax == []:
            ax = plt.gca()

        self.previous_point = []
        self.allxpoints = []
        self.allypoints = []
        self.start_point = []
        self.end_point = []
        self.line = None
        self.roicolor = roicolor
        self.fig = fig
        self.ax = ax
        #self.fig.canvas.draw()

        self.__ID1 = self.fig.canvas.mpl_connect(
            'motion_notify_event', self.__motion_notify_callback)
        self.__ID2 = self.fig.canvas.mpl_connect(
            'button_press_event', self.__button_press_callback)

        if sys.flags.interactive:
            plt.show(block=False)
        else:
            plt.show()

    def displayROI(self,**linekwargs):
        l = plt.Line2D(self.allxpoints +
                     [self.allxpoints[0]],
                     self.allypoints +
                     [self.allypoints[0]],
                     color=self.roicolor, **linekwargs)
        ax = plt.gca()
        ax.add_line(l)
        plt.draw()
        return np.around(self.allxpoints),np.around(self.allypoints) #round until 2 decimal points

    def __motion_notify_callback(self, event):    #just for asthetics, irrelevant again
        if event.inaxes:
            ax = event.inaxes
            x, y = event.xdata, event.ydata
            if (event.button == None or event.button == 1) and self.line != None: # Move line around
                self.line.set_data([self.previous_point[0], x],
                                   [self.previous_point[1], y])
                self.fig.canvas.draw()


    def __button_press_callback(self, event):      #button listener and irrelevant for us
        if event.inaxes:
            x, y = event.xdata, event.ydata
            ax = event.inaxes
            if event.button == 1 and event.dblclick == False:  # If you press the left button, single click
                if self.line == None: # if there is no line, create a line
                    self.line = plt.Line2D([x, x],
                                           [y, y],
                                           marker='o',
                                           color=self.roicolor)
                    self.start_point = [x,y]
                    self.previous_point =  self.start_point
                    self.allxpoints=[x]
                    self.allypoints=[y]

                    ax.add_line(self.line)
                    self.fig.canvas.draw()
                    # add a segment
                else: # if there is a line, create a segment
                    self.line = plt.Line2D([self.previous_point[0], x],
                                           [self.previous_point[1], y],
                                           marker = 'o',color=self.roicolor)
                    self.previous_point = [x,y]
                    self.allxpoints.append(x)
                    self.allypoints.append(y)

                    event.inaxes.add_line(self.line)
                    self.fig.canvas.draw()
            elif ((event.button == 1 and event.dblclick==True) or
                  (event.button == 3 and event.dblclick==False)) and self.line != None: # close the loop and disconnect
                self.fig.canvas.mpl_disconnect(self.__ID1) #joerg
                self.fig.canvas.mpl_disconnect(self.__ID2) #joerg

                self.line.set_data([self.previous_point[0],
                                    self.start_point[0]],
                                   [self.previous_point[1],
                                    self.start_point[1]])
                ax.add_line(self.line)
                self.fig.canvas.draw()
                self.line = None

                if sys.flags.interactive:
                    pass
                else:
                    plt.close(self.fig)