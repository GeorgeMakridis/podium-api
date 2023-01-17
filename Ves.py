class Ves:

    def __init__(self, vessel_code=None, power=None, apparent_wind_speed=None, speed_overground=None, stw_long=None, stw_trans=None, rpm=None, apparent_wind_angle=None, total_teus=None, total_feus=None, 
                 cons_ifo_static_counter=None, cons_ifo_static1_counter=None, port_mid_draft=None, stbd_mid_draft=None, draft_aft=None, draft_fore=None, stw=None, equivalent_teus=None, mid_draft=None, trim=None,
                 longitude=None, latitude=None, wind_speed=None, wind_ucomp=None, wind_vcomp=None, wind_wave_dir=None, wind_wave_height=None, wind_wave_mean_period=None, current_ucomp=None, current_vcomp=None,
                 relative_humidity=None, primary_wave_dir=None, primary_wave_length=None, primary_wave_mean_period=None, swell_wave_dir=None, swell_wave_height=None, swell_wave_mean_period=None,
                 air_temperature=None, comb_wind_swell_wave_height=None, direction=None):

            self.vessel_code = vessel_code
            self.power = power
            self.apparent_wind_speed = apparent_wind_speed
            self.speed_overground = speed_overground
            self.stw_long = stw_long
            self.stw_trans = stw_trans
            self.rpm = rpm
            self.apparent_wind_angle = apparent_wind_angle
            self.total_teus = total_teus
            self.total_feus = total_feus
            self.cons_ifo_static_counter = cons_ifo_static_counter
            self.cons_ifo_static1_counter = cons_ifo_static1_counter
            self.port_mid_draft = port_mid_draft
            self.stbd_mid_draft = stbd_mid_draft
            self.draft_aft = draft_aft
            self.draft_fore = draft_fore
            self.stw = stw
            self.equivalent_teus = equivalent_teus
            self.mid_draft = mid_draft
            self.trim = trim
            self.longitude = longitude
            self.latitude = latitude
            self.wind_speed = wind_speed
            self.wind_ucomp = wind_ucomp
            self.wind_vcomp = wind_vcomp
            self.wind_wave_dir = wind_wave_dir
            self.wind_wave_height = wind_wave_height
            self.wind_wave_mean_period = wind_wave_mean_period
            self.current_ucomp = current_ucomp
            self.current_vcomp = current_vcomp
            self.relative_humidity = relative_humidity
            self.primary_wave_dir = primary_wave_dir
            self.primary_wave_length = primary_wave_length
            self.primary_wave_mean_period = primary_wave_mean_period
            self.swell_wave_dir = swell_wave_dir
            self.swell_wave_height = swell_wave_height
            self.swell_wave_mean_period = swell_wave_mean_period
            self.air_temperature = air_temperature
            self.comb_wind_swell_wave_height = comb_wind_swell_wave_height
            self.direction = direction


