#!/usr/bin/python

# Import various modules
import time, pickle
import ROOT as R

# Define the system clock
startTime = time.time()

# Open data dictionary produced via makeDataDict.py
dd = pickle.load(open('../ddicts/dataDict.pkl', 'rb'))

# Chain ROOT files together per momentum setting
for tar, tar_dict in dd.items():
    # Initialize the tree chain lists
    dd[tar]['tree_chain'] = []
    tree_chain = []
    # Enumerate the individual momentum settings
    for index, mom_list in enumerate(dd[tar]['pcent_list']):
        # Initialze the TChain object for each momentum setting
        tree_chain = R.TChain('T')
        # Enumerate the list of ROOT files to be chained together
        for df_index, df_list in enumerate(dd[tar]['chain_list'][index]):
            tree_chain.Add(dd[tar]['chain_list'][index][df_index])
        # Populate the list of TChain objects for each momentum setting
        dd[tar]['tree_chain'].append(tree_chain)

# Save the dictionary with chained ROOT files into a pickle file
pickle.dump(dd, open('../ddicts/dataDictQNY.pkl', 'wb'))

# Create ROOT output file with histograms
rof = R.TFile('../data/shms.root', 'recreate')
for tar, tar_dict in dd.items():
    # Add LaTeX format for target strings
    if (tar == 'be9') : tarStr = '{}^{9}Be'
    if (tar == 'c12') : tarStr = '{}^{12}C'
    for index, mom_list in enumerate(dd[tar]['pcent_list']):
        rof.mkdir('%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')))
        rof.cd('%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')))
        #nentries = dd[tar]['tree_chain'][index].GetEntries() 
        nentries = 10000
        # Define histograms
        hxbj         = R.TH1F('hxbj_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')),         'x_{Bj} for %s, %s GeV; x_{Bj}; Number of Entries / 0.025' % (tarStr, dd[tar]['pcent_list'][index]), 60, 0, 1.5)
        heprime      = R.TH1F('heprime_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')),      'E\' for %s, %s GeV; E\' (GeV); Number of Entries / 0.100 GeV' % (tarStr, dd[tar]['pcent_list'][index]), 120, 0.0, 12.0)
        hw2_vs_xbj   = R.TH2F('hw2_vs_xbj_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')),   'W^{2} vs. x_{Bj} for %s, %s GeV; x_{Bj} / 0.025; W^{2} / 0.010 GeV^{2}' % (tarStr, dd[tar]['pcent_list'][index]), 60, 0, 1.5, 1500, 0, 15.0)
        hdp_vs_theta = R.TH2F('hdp_vs_theta_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')), '#deltap vs. (#theta_{c}-#theta) for %s, %s GeV; #theta_{c}-#theta / 0.01 deg; #deltap / 0.5%%' % (tarStr, dd[tar]['pcent_list'][index]), 100, -5.0, 5.0, 68, -12.0, 22.0)
        # Loop over the entries in the trees
        print '\nAnalyzing the %s target at %s GeV.  There are %d events to be analyzed.\n' % (tar.upper(), dd[tar]['pcent_list'][index], nentries)
        for entry in range(nentries):
            dd[tar]['tree_chain'][index].GetEntry(entry)
            if ((entry % 10000) == 0 and entry != 0) : print 'Analyzed %d events...' % entry
            # Acquire the leaves of interest
            # PID variables
            lhgcNpeSum  = dd[tar]['tree_chain'][index].GetLeaf('P.hgcer.npeSum');   hgcNpeSum  = lhgcNpeSum.GetValue(0)
            lngcNpeSum  = dd[tar]['tree_chain'][index].GetLeaf('P.ngcer.npeSum');   ngcNpeSum  = lngcNpeSum.GetValue(0)                
            letracknorm = dd[tar]['tree_chain'][index].GetLeaf('P.cal.etracknorm'); etracknorm = letracknorm.GetValue(0)
            # Phase space & acceptance variables
            ldelta  = dd[tar]['tree_chain'][index].GetLeaf('P.gtr.dp'); delta  = ldelta.GetValue(0)
            leprime = dd[tar]['tree_chain'][index].GetLeaf('P.gtr.p');  eprime = leprime.GetValue(0) # convert to mrad
            # Kinematic variables
            lw2     = dd[tar]['tree_chain'][index].GetLeaf('P.kin.W2'); w2 = lw2.GetValue(0)
            lq2     = dd[tar]['tree_chain'][index].GetLeaf('P.kin.Q2'); q2 = lq2.GetValue(0)
            lxbj    = dd[tar]['tree_chain'][index].GetLeaf('P.kin.x_bj'); xbj = lxbj.GetValue(0)
            ltheta  = dd[tar]['tree_chain'][index].GetLeaf('P.kin.scat_ang_deg'); theta = ltheta.GetValue(0)
            # Fill histograms prior to fiducial cuts
            hw2_vs_xbj.Fill(xbj, w2)
            hdp_vs_theta.Fill(dd[tar]['theta'][index] - theta, delta)
            # Define the fiducial cuts
            hgcNpeCut     = bool(hgcNpeSum < 0.5)
            ngcNpeCut     = bool(ngcNpeSum < 7.5)
            npeCut        = bool(hgcNpeCut or ngcNpeCut)
            deltaCut      = bool(delta < -10.0 or delta > 20.0)
            w2Cut         = bool(w2 < 2.0) # select the DIS regime
            etracknormCut = bool(etracknorm < 0.85)
            # Impose fiducial cuts
            if (npeCut or deltaCut or etracknormCut or w2Cut) : continue
            # Fill the histograms
            hxbj.Fill(xbj)
            heprime.Fill(eprime)
        # Populate efficency corrected charge histograms
        # xbj
        hxbj_qNorm = hxbj.Clone()
        hxbj_qNorm.SetNameTitle('hxbj_qNorm_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')), 'Charge Normalized x_{Bj} for %s, %s GeV; x_{Bj} / 0.025; Y / #epsilonQ (Counts / mC)' % (tarStr, dd[tar]['pcent_list'][index]))
        hxbj_qNorm.Sumw2()
        hxbj_qNorm.Scale(1. / dd[tar]['ecq'][index])
        # eprime
        heprime_qNorm = heprime.Clone()
        heprime_qNorm.SetNameTitle('heprime_qNorm_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')), 'Charge Normalized E\' for %s, %s GeV; E\' / 0.100 GeV; Y / #epsilonQ (Counts / mC)' % (tarStr, dd[tar]['pcent_list'][index]))
        heprime_qNorm.Sumw2()
        heprime_qNorm.Scale(1. / dd[tar]['ecq'][index])
        # delta
        hdp_qNorm = hdp_vs_theta.ProjectionY()
        hdp_qNorm.SetNameTitle('hdp_qNorm_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')), 'Charge Normalized #deltap for %s, %s GeV; #deltap / 0.5%%; Y / #epsilonQ (Counts / mC)' % (tarStr, dd[tar]['pcent_list'][index]))
        hdp_qNorm.Sumw2()
        hdp_qNorm.Scale(1. / dd[tar]['ecq'][index])
        # w2
        hw2_qNorm = hw2_vs_xbj.ProjectionY()
        hw2_qNorm.SetNameTitle('hw2_qNorm_%s_%s' % (tar, str(dd[tar]['pcent_list'][index]).replace('.', 'p')), 'Charge Normalized W^{2} for %s, %s GeV; W^{2} / 0.010 GeV^{2}; Y / #epsilonQ (Counts / mC)' % (tarStr, dd[tar]['pcent_list'][index]))
        hw2_qNorm.Sumw2()
        hw2_qNorm.Scale(1. / dd[tar]['ecq'][index])
        # Write the histograms to tape
        rof.Write()
        hdp_qNorm.Delete() # address a behavior with projection
        hw2_qNorm.Delete() # address a behavior with projection
        rof.cd('../')
# Close the ROOT file
rof.Close()

print '\nThe analysis took %.3f minutes\n' % ((time.time() - startTime) / (60.))
