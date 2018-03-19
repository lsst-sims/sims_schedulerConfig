#import collections

import SALPY_scheduler

target = SALPY_scheduler.scheduler_targetC()
target.targetId = 10
target.fieldId = 300
target.groupId = 2
target.filter = "z"
target.ra = 1.000
target.decl = -3.00
target.angle = 0.5
target.alt = 60.0
target.az = 240.0
target.num_exposures = 2
target.exposure_times[0] = 15
target.exposure_times[1] = 15
target.request_time = 1640995200.0
target.request_mdj = 59280.0
target.airmass = 1.4
target.sky_brightness = 20.4
target.cloud = 0.0
target.seeing = 0.5
target.need = 0.001
target.slew_time = 4.75
target.cost = 0.1
target.rank = 0.013
target.prop_boost = 0.005
target.num_proposals = 2
target.moon_ra = 65.0
target.moon_dec = -10.0
target.moon_alt = -30.0
target.moon_az = 250.0
target.moon_phase = 0.5
target.moon_distance = 60.0

field_topic = SALPY_scheduler.scheduler_fieldC()
field_topic.ID = 1
field_topic.fov = 0.5
field_topic.ra = 30.0
field_topic.decl = -30.0
field_topic.gl = -45.0
field_topic.gb = 45.0
field_topic.el = 60.0
field_topic.eb = -60.0

field_tuple = (1, 0.5, 30.0, -30.0, -45.0, 45.0, 60.0, -60.0)

observation_topic = SALPY_scheduler.scheduler_observationC()
observation_topic.observationID = 5
observation_topic.targetID = 10
observation_topic.night = 1
observation_topic.observation_start_time = 1640995200.0
observation_topic.observation_start_mjd = 59580.0
observation_topic.observation_start_lst = 29.87546023333333
observation_topic.fieldId = 300
observation_topic.groupId = 2
observation_topic.filter = "r"
observation_topic.ra = 1.000
observation_topic.decl = -3.00
observation_topic.angle = 0.5
observation_topic.altitude = 60.0
observation_topic.azimuth = 240.0
observation_topic.num_exposures = 2
observation_topic.exposure_times[0] = 15
observation_topic.exposure_times[1] = 15
observation_topic.visit_time = 34.0
observation_topic.airmass = 1.4
observation_topic.sky_brightness = 20.4
observation_topic.cloud = 0.2
observation_topic.seeing_fwhm_500 = 0.7
observation_topic.seeing_fwhm_geom = 0.75
observation_topic.seeing_fwhm_eff = 1.04
observation_topic.five_sigma_depth = 21.3
observation_topic.moon_ra = 65.0
observation_topic.moon_dec = -10.0
observation_topic.moon_alt = -30.0
observation_topic.moon_az = 250.0
observation_topic.moon_phase = 0.5
observation_topic.moon_distance = 60.0
observation_topic.sun_ra = 245.0
observation_topic.sun_dec = 0.0
observation_topic.sun_alt = -10.0
observation_topic.sun_az = 250.0
observation_topic.solar_elong = 250.0

config_tuple = (10, "config/test/a", "1.0")
