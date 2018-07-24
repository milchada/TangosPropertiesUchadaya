from __future__ import absolute_import
from __future__ import print_function
import pynbody
from tangos.properties.pynbody import PynbodyPropertyCalculation
from tangos.properties.pynbody.centring import centred_calculation
import numpy as np

class ThermProfiles(PynbodyPropertyCalculation):
    requires_particle_data=True
    names = "rho_g_1e65K_profile"

    def requires_property(self):
        return ['shrink_center', 'max_radius']

    def get_profile(self, particle_data, existing_properties):
    	hot_particles = particle_data.g[particle_data.g['temp'] > pow(10,6.5)]
        return pynbody.analysis.profile.Profile(hot_particles, min=1, max=1e3, type='log', ndim=3)

    @centred_calculation
    def calculate(self, particle_data, existing_properties):
    	pg = self.get_profile(particle_data, existing_properties)
    	return pg['density'].in_units('g cm**-3')

