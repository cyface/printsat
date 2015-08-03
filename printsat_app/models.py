from django.db import models
from django.conf import settings


class Telemetry(models.Model):
    """Telemetry point from PrintSat."""

    station = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=10, decimal_places=5)
    lng = models.DecimalField(max_digits=10, decimal_places=5)
    program = models.CharField(max_length=30)
    telem_type = models.CharField(max_length=20)
    ps_time = models.DateTimeField(db_index=True, unique=True)
    ps_time_seconds = models.IntegerField()
    last_good_io_telem = models.CharField(max_length=30, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    bat_v = models.DecimalField(max_digits=10, decimal_places=2)
    bat_i = models.DecimalField(max_digits=10, decimal_places=2)
    msu_0 = models.DecimalField(max_digits=10, decimal_places=2)
    msu_1 = models.DecimalField(max_digits=10, decimal_places=2)
    sep_state = models.DecimalField(max_digits=10, decimal_places=2)
    sp1_v_5 = models.DecimalField(max_digits=10, decimal_places=2)
    sp1_i_5 = models.DecimalField(max_digits=10, decimal_places=2)
    sp2_v_6 = models.DecimalField(max_digits=10, decimal_places=2)
    sp2_i_6 = models.DecimalField(max_digits=10, decimal_places=2)
    sp3_v_7 = models.DecimalField(max_digits=10, decimal_places=2)
    sp3_i_7 = models.DecimalField(max_digits=10, decimal_places=2)
    sp4_v_8 = models.DecimalField(max_digits=10, decimal_places=2)
    sp4_i_8 = models.DecimalField(max_digits=10, decimal_places=2)
    five_v = models.DecimalField(max_digits=10, decimal_places=2)
    five_i = models.DecimalField(max_digits=10, decimal_places=2)
    three_v = models.DecimalField(max_digits=10, decimal_places=2)
    three_i = models.DecimalField(max_digits=10, decimal_places=2)
    load_cell_v = models.DecimalField(max_digits=10, decimal_places=2)
    sp1_temp = models.DecimalField(max_digits=10, decimal_places=2)
    sp3_temp = models.DecimalField(max_digits=10, decimal_places=2)
    bat_temp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    five_v_reg_temp = models.DecimalField(max_digits=10, decimal_places=2)
    imm_pcb_temp = models.DecimalField(max_digits=10, decimal_places=2)
    wilt_cell_i = models.DecimalField(max_digits=10, decimal_places=2)
    wilt_cell_v = models.DecimalField(max_digits=10, decimal_places=2)
    rdo_deflt_err = models.DecimalField(max_digits=10, decimal_places=2)
    rdo_rd_timeout = models.DecimalField(max_digits=10, decimal_places=2)
    tlm_save_intvl = models.DecimalField(max_digits=10, decimal_places=2)
    tlm_send_intvl = models.DecimalField(max_digits=10, decimal_places=2)
    info_send_intvl = models.DecimalField(max_digits=10, decimal_places=2)
    imm_mux_dly = models.DecimalField(max_digits=10, decimal_places=2)
    msu_mux_dly = models.DecimalField(max_digits=10, decimal_places=2)
    portc = models.DecimalField(max_digits=10, decimal_places=2)
    rad_cmd_count = models.DecimalField(max_digits=10, decimal_places=2)
    rad_temp = models.DecimalField(max_digits=10, decimal_places=2)
    rad_rssi = models.DecimalField(max_digits=10, decimal_places=2)
    udoslo = models.DecimalField(max_digits=10, decimal_places=2)
    msu_i_1 = models.DecimalField(max_digits=10, decimal_places=2)
    udos_med = models.DecimalField(max_digits=10, decimal_places=2)
    msu_temp_1 = models.DecimalField(max_digits=10, decimal_places=2)
    udos_hi = models.DecimalField(max_digits=10, decimal_places=2)
    msu_i_2 = models.DecimalField(max_digits=10, decimal_places=2)
    udos_log = models.DecimalField(max_digits=10, decimal_places=2)
    msu_temp_2 = models.DecimalField(max_digits=10, decimal_places=2)
    msu_i_3 = models.DecimalField(max_digits=10, decimal_places=2)
    msu_temp_3 = models.DecimalField(max_digits=10, decimal_places=2)
    msu_temp_4 = models.DecimalField(max_digits=10, decimal_places=2)
    test_v_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_6 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_6 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_7 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_7 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_8 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_8 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_9 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_9 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_10 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_10 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_11 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_11 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_12 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_12 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_13 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_13 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_14 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_14 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_v_15 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    test_i_15 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_6 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_6 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_7 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_7 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_8 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_8 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_9 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_9 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_10 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_10 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_11 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_11 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_12 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_12 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_13 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_13 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_14 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_14 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_v_15 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    known_i_15 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imm_temp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['ps_time']
        verbose_name_plural = "telemetry"


    def __unicode__(self):
        return unicode(self.ps_time)


class Upload(models.Model):
    """Track Uploaded Files"""
    file = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['date_created']

    def __unicode__(self):
        return unicode(self.file)
