#!/usr/bin/python

# Import various modules
import pickle, copy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ROOT as R
from matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable

rc('text', usetex = True)
rc('font', family = 'serif')
mpl.rcParams.update({'font.size': 18})
mpl.rcParams.update({'errorbar.capsize': 10})

# Open data dictionary produced via makeDataDict.py
dd = pickle.load(open('../ddicts/dataDictXbj.pkl', 'rb'))

# Make simple overlay plot of E' yield for the c12 target, recall there are 2 momentum settings
plt.figure()
plt.title('Charge Normalized Yields for 12C')
plt.xlim(3.5, 6.1) 
plt.ylim(0.0, np.max(dd['c12']['eprime_qny'][0]) + np.max(dd['c12']['eprime_qny'][0])*0.10)
plt.xlabel('E\' / 0.100 GeV')
plt.ylabel('Yield')
plt.bar(dd['c12']['eprime_val'][0], dd['c12']['eprime_qny'][0],
        yerr = dd['c12']['eprime_qny_err'][0], label = '4.0 GeV',
        width = 0.100, align = 'center', color = 'b', edgecolor = 'b', alpha = 0.5)
plt.bar(dd['c12']['eprime_val'][1], dd['c12']['eprime_qny'][1],
        yerr = dd['c12']['eprime_qny_err'][1], label = '5.1 GeV',
        width = 0.100, align = 'center', color = 'g', edgecolor = 'g', alpha = 0.5)
plt.legend(loc = 'best', numpoints = 1, fancybox = True)
plt.savefig('../plots/c12-qny-simple.png')

# =:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

# # Make overlay plot of xbj yields with data points
# tarfont = {'family' : 'serif',
#            'color'  : 'darkred',
#            'weight' : 'normal',
#            'size'   : 32 }
# mkrs = ['bd', 'gs', 'ko']
# fig, axs = plt.subplots(nrows = 2, sharex = True)
# fig.suptitle(r'$\mathrm{Charge\ Normalized\ Yields}$')
# fig.text(0.01, 0.5, r'$\mathbf{\mathrm{Y / \epsilon Q}}$', va = 'center', rotation = 'vertical')
# for tar, tar_dict in dd.items():
#    for index, mom_list in enumerate(dd[tar]['pcent_list']):
#        if (tar == 'c12') :
#            ax = axs[0]
#            ax.errorbar(dd[tar]['xbj_calc_val'][index], dd[tar]['xbj_calc_qny'][index], 
#                        yerr = dd[tar]['xbj_calc_qny_err'][index], fmt = mkrs[index], 
#                        label = str(dd[tar]['pcent_list'][index]) + ' GeV', 
#                        markersize = 9, alpha = 0.75)
#            ax.set_xlim(0.2, 1.01)
#            ax.set_ylim(0.0, np.amax(dd[tar]['xbj_calc_qny'][0]) + 
#                        np.amax(dd[tar]['xbj_calc_qny'][0])*0.10)
#            ax.text(0.1, 0.2, r'${}^{12}\mathrm{{C}}$', ha = 'center', va = 'center', 
#                    transform = ax.transAxes, fontdict = tarfont)
#            ax.legend(loc = 'best', numpoints = 1, fancybox = True)
#        if (tar == 'be9') :
#            ax = axs[1]
#            if (dd[tar]['pcent_list'][index] == 3.3) : tmpfmt = mkrs[2]
#            else : tmpfmt = mkrs[index]
#            ax.errorbar(dd[tar]['xbj_calc_val'][index], dd[tar]['xbj_calc_qny'][index], 
#                        yerr = dd[tar]['xbj_calc_qny_err'][index], fmt = tmpfmt, 
#                        label = str(dd[tar]['pcent_list'][index]) + ' GeV', 
#                        markersize = 9, alpha = 0.75)
#            ax.set_ylim(0.0, np.amax(dd[tar]['xbj_calc_qny'][0]) + 
#                        np.amax(dd[tar]['xbj_calc_qny'][0])*5.0)
#            ax.set_yscale('log')
#            ax.set_xlabel(r'$\mathrm{x_{Bj}}$')
#            ax.text(0.1, 0.2, r'${}^{9}\mathrm{{Be}}$', ha = 'center', va = 'center', 
#                    transform = ax.transAxes, fontdict = tarfont)
#            ax.legend(loc = 'best', numpoints = 1, fancybox = True)
# plt.savefig('../plots/multi-tar-qny-xbj.png')

# =:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

# # Open data frame produced via makeDataFrame.py
# df = pickle.load(open('../dframes/dataFrame.pkl', 'rb'))
# # Plot variables in data frame
# mkrs = ['bd', 'gs', 'ko', 'r*']
# fig, ax = plt.subplots(ncols = 2, figsize  = (20, 10)) 
# # Unpack the axs array into its individual components
# ax0, ax1 = ax.flatten()
# # Plot trigger rate vs computer live time
# df.plot(x = 'rn', y = 'clt', ax = ax0, style = mkrs[0], label = 'Comp Live Time', 
#         legend = False, ms = 10, alpha = 0.75)
# ax0.set_title('Trigger Rate \& Computer Live Time')
# ax0.set_xlabel('Run Number')
# ax0.set_ylabel('Live Time (\%)', color = 'b')
# ax0.tick_params('y', colors = 'b')
# ax0.set_ylim(55.0, 105.0)
# ax0.set_xlim(2480, 2567)
# ax0.xaxis.grid(True)
# ax0p1 = ax0.twinx()
# df.plot(x = 'rn', y = 'pt2r', ax = ax0p1, style = mkrs[1], label = 'Trigger Rate', 
#         legend = False, ms = 10, alpha = 0.75)
# ax0p1.set_ylim(0.0, 40.0)
# ax0p1.set_xlim(2480, 2567)
# ax0p1.set_ylabel('Trigger Trigger Rate (kHz)', color = 'g')
# ax0p1.tick_params('y', colors = 'g')

# # Plot total charge as measured by BCMs
# df.plot(x = 'rn', y = 'i4a', ax = ax1, style = mkrs[2], alpha = 0.75, 
#         label = 'BCM 4A', ms = 10)
# df.plot(x = 'rn', y = 'i4b', ax = ax1, style = mkrs[3], alpha = 0.75, 
#         label = 'BCM 4B', ms = 10)
# ax1.set_ylim(20, 60)
# ax1.set_xlim(2480, 2567)
# ax1.set_title('BCM Current')
# ax1.set_xlabel('Run Number')
# ax1.set_ylabel('Current (uA)')
# ax1.grid()
# ax1.set_xticklabels([])
# ax1.legend(numpoints = 1, loc = 'best')
# # Calculate the residual between the two BCM's and plot
# df['i4a_i4b_resid'] = df['i4a'] - df['i4b']
# divider  = make_axes_locatable(ax1)
# ax1p1 = divider.append_axes("bottom", size = '50%', pad = 0)
# ax1.figure.add_axes(ax1p1)
# df.plot(x = 'rn', y = 'i4a_i4b_resid', ax = ax1p1, style = 'm-', 
#         label = 'BCM4A - BCM4B')
# ax1p1.set_ylim(0.0, 1)
# ax1p1.set_xlim(2480, 2567)
# ax1p1.set_xlabel('Run Number')
# ax1p1.set_ylabel('Residual (uA)')
# ax1p1.grid()
# ax1p1.locator_params(axis = 'y', nbins = 6)
# plt.tight_layout()
# plt.savefig('../plots/run-vars.png')

plt.show()
