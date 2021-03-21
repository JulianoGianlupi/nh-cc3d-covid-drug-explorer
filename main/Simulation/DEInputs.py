"""
Defines default module model parameters
"""
__param_desc__ = {}

__param_desc__['intern_met_rate'] = 'Metabolization rate of the internalization blocker prodrug'
intern_met_rate = 1

__param_desc__['intern_elimin_rate'] = 'Elimination rate of the internalization blocker active component'
intern_elimin_rate = .1

__param_desc__['intern_time_of_first_dose'] = 'Start time of internalization blocker'
intern_time_1 = 0

__param_desc__['intern_dosing_period'] = 'Period of internalization blocker'
intern_dosing_period = 20

__param_desc__['rep_met_rate'] = 'Metabolization rate of the replication blocker prodrug'
rep_met_rate = 1

__param_desc__['rep_elimin_rate'] = 'Elimination rate of the replication blocker active component'
rep_elimin_rate = .1

__param_desc__['rep_time_of_first_dose'] = 'Start time of replication blocker'
rep_time_1 = 0

__param_desc__['rep_dosing_period'] = 'Period of replication blocker'
rep_dosing_period = 20
