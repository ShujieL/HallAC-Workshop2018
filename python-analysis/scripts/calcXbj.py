#!/usr/bin/python

# Import various modules
import pickle
import numpy as np
import ROOT as R

# Open data dictionary produced via makeDataDict.py
dd = pickle.load(open('../ddicts/dataDictQNY.pkl', 'rb'))

# Open the ROOT file created via makeHistos.py
rof = R.TFile('../data/shms.root', 'read')

# Convert histos in numpy arrays for easier manipulation
for tar, tar_dict in dd.items():
    # Create containers to store raw and charge normalized yields and bin centered values
    eprime_val_list = []
    eprime_ry_list = []
    eprime_qny_list = []
    dd[tar]['eprime_val'] = []
    dd[tar]['eprime_ry'] = []
    dd[tar]['eprime_qny'] = []
    dd[tar]['eprime_qny_err'] = []
    for index, mom_list in enumerate(dd[tar]['pcent_list']):
        # Descend into ROOT file directory with histos of interest
        rof.cd('%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')))
        # Define temporary place holders for histo and array objects
        # Get raw histo and place contents in array
        heprime_raw = rof.FindObjectAny('heprime_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')))
        aeprime_raw = heprime_raw.GetArray()         # returns number of x bins +2 (over&underflow)
        aeprime_raw.SetSize(heprime_raw.GetNbinsX()) # returns number of x bins +2 (over&underflow)
        # Get charge normalized histo and place contents in array
        heprime_qnorm = rof.FindObjectAny('heprime_qNorm_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')))
        aeprime_qnorm = heprime_qnorm.GetArray()
        aeprime_qnorm.SetSize(heprime_qnorm.GetNbinsX()) # returns number of x bins +2 (over&underflow)
        # Define bin centering arrays
        eprime_xval   = np.linspace(heprime_qnorm.GetXaxis().GetXmin(), heprime_qnorm.GetXaxis().GetXmax() - heprime_qnorm.GetXaxis().GetBinWidth(1), num = heprime_qnorm.GetNbinsX())
        eprime_offset = heprime_qnorm.GetXaxis().GetBinWidth(1) / 2.
        eprime_arr    = eprime_xval + eprime_offset
        # Fill arrays with histo content
        heprime_raw_arr   = np.array(heprime_raw)[:-2]   # delete the last two over&underflow elements
        heprime_qnorm_arr = np.array(heprime_qnorm)[:-2] # delete the last two over&underflow elements
        # Store yields and bin centers in lists for each momentum
        eprime_val_list.append(eprime_arr)
        eprime_ry_list.append(heprime_raw_arr)
        eprime_qny_list.append(heprime_qnorm_arr)
    # Store yields and bin center lists in data dictionary indexed on dd['pcent_list']
    dd[tar]['eprime_val']     = eprime_val_list
    dd[tar]['eprime_ry']      = eprime_ry_list
    dd[tar]['eprime_qny']     = eprime_qny_list
    dd[tar]['eprime_ry_err']  = np.sqrt(eprime_ry_list)
    dd[tar]['eprime_qny_err'] = np.sqrt(eprime_ry_list)*(1. / dd[tar]['ecq'][index])

# Truncate all non-zero ratios for plotting
for tar, tar_dict in dd.items():
    # Initialize lists
    eprime_nz_val_list = []
    eprime_nz_ry_list = []
    eprime_nz_qny_list = []
    eprime_nz_ry_err_list = []
    eprime_nz_qny_err_list = []
    for index, mom_list in enumerate(dd[tar]['pcent_list']):
        # Truncate all non-zero qnys for plotting
        eprime_nz_val_list.append(dd[tar]['eprime_val'][index][dd[tar]['eprime_qny'][index]>0.0])
        eprime_nz_ry_list.append(dd[tar]['eprime_ry'][index][dd[tar]['eprime_ry'][index]>0.0])
        eprime_nz_qny_list.append(dd[tar]['eprime_qny'][index][dd[tar]['eprime_qny'][index]>0.0])
        eprime_nz_ry_err_list.append(dd[tar]['eprime_ry_err'][index][dd[tar]['eprime_ry'][index]>0.0])
        eprime_nz_qny_err_list.append(dd[tar]['eprime_qny_err'][index][dd[tar]['eprime_qny'][index]>0.0])
    # Overwrite previous E' arrays with truncated arrays
    dd[tar]['eprime_val']     = eprime_nz_val_list
    dd[tar]['eprime_ry']      = eprime_nz_ry_list
    dd[tar]['eprime_qny']     = eprime_nz_qny_list
    dd[tar]['eprime_ry_err']  = eprime_nz_ry_err_list
    dd[tar]['eprime_qny_err'] = eprime_nz_qny_err_list
    
# Define function to calculate xbj from bins in E'
mp = 0.93827231 # (GeV) mass of proton
def calc_xbj(ep, eb, theta) :
    return ((eb*ep*(1.0 - np.cos(np.deg2rad(theta))))/(mp*(eb - ep)))

# Calculate xbj from E' and store in dictionary
for tar, tar_dict in dd.items():
    xbj_calc_nz_val_list = []
    xbj_calc_nz_ry_list = []
    xbj_calc_nz_qny_list = []
    xbj_calc_nz_ry_err_list = []
    xbj_calc_nz_qny_err_list = []
    for index, mom_list in enumerate(dd[tar]['pcent_list']):
        xbj_calc_nz_val_list.append(calc_xbj(dd[tar]['eprime_val'][index], dd[tar]['ebeam'][index], dd[tar]['theta'][index]))
        xbj_calc_nz_ry_list.append(dd[tar]['eprime_ry'][index])
        xbj_calc_nz_qny_list.append(dd[tar]['eprime_qny'][index])
        xbj_calc_nz_ry_err_list.append(dd[tar]['eprime_ry_err'][index])
        xbj_calc_nz_qny_err_list.append(dd[tar]['eprime_qny_err'][index])
    # Overwrite previous xbj arrays with truncated arrays
    dd[tar]['xbj_calc_val']     = xbj_calc_nz_val_list
    dd[tar]['xbj_calc_ry']      = xbj_calc_nz_ry_list
    dd[tar]['xbj_calc_qny']     = xbj_calc_nz_qny_list
    dd[tar]['xbj_calc_ry_err']  = xbj_calc_nz_ry_err_list
    dd[tar]['xbj_calc_qny_err'] = xbj_calc_nz_qny_err_list

# Save the dictionary with calculated xbj values into a pickle file
pickle.dump(dd, open('../ddicts/dataDictXbj.pkl', 'wb'))
