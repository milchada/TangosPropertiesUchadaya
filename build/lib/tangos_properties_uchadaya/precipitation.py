from __future__ import absolute_import
from __future__ import print_function
import pynbody
from tangos.properties.pynbody import PynbodyPropertyCalculation
from tangos.properties.pynbody.centring import centred_calculation
import numpy as np

def entropy(ptcls, mw=False):
    T_kev = ptcls['temp'].in_units('K')*pynbody.units.k.in_units('keV K**-1')
    n_cc = ptcls['ne']*ptcls.g['rho'].in_units('m_p cm**-3')
    entropy = T_kev*pow(n_cc,-2./3)
    entropy.units = 'keV cm^2'
    return entropy #*weight

def precipitation(pg, std=False):
    out = np.zeros(pg.nbins)
    drbins = pg['bin_edges'][1:] - pg['bin_edges'][:-1]
    for i in range(pg.nbins):
        subs = pg.sim[pg.binind[i]]
        gas = subs.g
        subs.g['entropy'] = entropy(subs.g)
        mean_entropy = np.nanmean(subs.g['entropy'])
	if std:
		mean_entropy -= np.nanstd(subs.g['entropy'])
        cold_gas_filt = pynbody.filt.LowPass('entropy', mean_entropy) & pynbody.filt.FamilyFilter(pynbody.family.gas) & pynbody.filt.LowPass('vr', 0)
        cold_gas = gas[cold_gas_filt]
        mdot = cold_gas['mass'] * cold_gas['vr'] / (pynbody.units.Unit("kpc")*drbins[i])
        out[i] = sum(mdot.in_units('Msol yr**-1'))
    return out

class PrecipitationProfile(PynbodyPropertyCalculation):
    requires_particle_data=True
    names = "colder_mdot_in_profile"

    def requires_property(self):
        return ['shrink_center', 'max_radius']

    def get_profile(self, particle_data, existing_properties):
        return pynbody.analysis.profile.Profile(particle_data.g, min=1, max=1e3, type='log', ndim=3)

    @centred_calculation
    def calculate(self, particle_data, existing_properties):
    	pg = self.get_profile(particle_data, existing_properties)
    	return precipitation(pg)

class PrecipitationStrongcutProfile(PynbodyPropertyCalculation):
    requires_particle_data=True
    names = "cold_mdot_in_profile"
    
    def requires_property(self):
        return ['shrink_center', 'max_radius']
        
    def get_profile(self, particle_data, existing_properties):
        return pynbody.analysis.profile.Profile(particle_data.g, min=1, max=1e3, type='log', ndim=3)
 
    @centred_calculation
    def calculate(self, particle_data, existing_properties):
        pg = self.get_profile(particle_data, existing_properties)
        return precipitation(pg, std=True)

