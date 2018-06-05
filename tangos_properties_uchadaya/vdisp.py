from __future__ import absolute_import
from __future__ import print_function
import pynbody
from tangos.properties.pynbody import PynbodyPropertyCalculation
from tangos.properties.pynbody.centring import centred_calculation
import numpy as np

class VDispProfile(PynbodyPropertyCalculation):
    requires_particle_data=True
    names = "v_disp_profile"

    def requires_property(self):
    	return ['shrink_center', 'max_radius']

    def get_profile(self, particle_data, existing_properties):
        return pynbody.analysis.profile.Profile(particle_data.g, min=1, max=1e3, type='log', ndim=3)

    @centred_calculation
    def calculate(self, particle_data, existing_properties):
    	pg = self.get_profile(particle_data, existing_properties)
    	return pg['v_disp'].in_units('km s**-1')

