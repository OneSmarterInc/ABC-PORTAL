from django.db import models


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class MyappCustodialDataTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ssn = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sub_dep = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zip = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dob = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sex = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    class_field = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eff_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_field = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_first_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_last_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_dob = models.DateField(blank=True, null=True)
    dep_ssn = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_sex = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_parent = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address2 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_city = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_state = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_zip = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address2 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    member_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date_edi = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    filename = models.CharField(max_length=525, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    temp_ssn = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    term_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_flag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_custodial_data_table'

class MyappDepnp(models.Model):
    id = models.BigAutoField(primary_key=True)
    dpdrop = models.TextField(db_column='DPDROP', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpclnt = models.TextField(db_column='DPCLNT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpssn = models.TextField(db_column='DPSSN', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpseq = models.TextField(db_column='DPSEQ', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpname = models.TextField(db_column='DPNAME', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpdoby = models.IntegerField(db_column='DPDOBY', blank=True, null=True)  # Field name made lowercase.
    dpdobm = models.IntegerField(db_column='DPDOBM', blank=True, null=True)  # Field name made lowercase.
    dpdobd = models.IntegerField(db_column='DPDOBD', blank=True, null=True)  # Field name made lowercase.
    dpdody = models.IntegerField(db_column='DPDODY', blank=True, null=True)  # Field name made lowercase.
    dpdodm = models.IntegerField(db_column='DPDODM', blank=True, null=True)  # Field name made lowercase.
    dpdodd = models.IntegerField(db_column='DPDODD', blank=True, null=True)  # Field name made lowercase.
    dpdssn = models.TextField(db_column='DPDSSN', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpsex = models.TextField(db_column='DPSEX', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dptype = models.TextField(db_column='DPTYPE', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dprltn = models.TextField(db_column='DPRLTN', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpefdy = models.IntegerField(db_column='DPEFDY', blank=True, null=True)  # Field name made lowercase.
    dpefdm = models.IntegerField(db_column='DPEFDM', blank=True, null=True)  # Field name made lowercase.
    dpefdd = models.IntegerField(db_column='DPEFDD', blank=True, null=True)  # Field name made lowercase.
    dptdty = models.IntegerField(db_column='DPTDTY', blank=True, null=True)  # Field name made lowercase.
    dptdtm = models.IntegerField(db_column='DPTDTM', blank=True, null=True)  # Field name made lowercase.
    dptdtd = models.IntegerField(db_column='DPTDTD', blank=True, null=True)  # Field name made lowercase.
    dpcob = models.TextField(db_column='DPCOB', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpplan = models.TextField(db_column='DPPLAN', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpclas = models.TextField(db_column='DPCLAS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpstat = models.TextField(db_column='DPSTAT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpaltp = models.TextField(db_column='DPALTP', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dpself = models.BooleanField(db_column='DPSELF', blank=True, null=True)  # Field name made lowercase.
    dpmdfl = models.BooleanField(db_column='DPMDFL', blank=True, null=True)  # Field name made lowercase.
    dpmefy = models.IntegerField(db_column='DPMEFY', blank=True, null=True)  # Field name made lowercase.
    dpmefm = models.IntegerField(db_column='DPMEFM', blank=True, null=True)  # Field name made lowercase.
    dpmefd = models.IntegerField(db_column='DPMEFD', blank=True, null=True)  # Field name made lowercase.
    dpmgyy = models.IntegerField(db_column='DPMGYY', blank=True, null=True)  # Field name made lowercase.
    dpmgmm = models.IntegerField(db_column='DPMGMM', blank=True, null=True)  # Field name made lowercase.
    dpmgdd = models.IntegerField(db_column='DPMGDD', blank=True, null=True)  # Field name made lowercase.
    dpdvyy = models.IntegerField(db_column='DPDVYY', blank=True, null=True)  # Field name made lowercase.
    dpdvmm = models.IntegerField(db_column='DPDVMM', blank=True, null=True)  # Field name made lowercase.
    dpdvdd = models.IntegerField(db_column='DPDVDD', blank=True, null=True)  # Field name made lowercase.
    dpbsfl = models.BooleanField(db_column='DPBSFL', blank=True, null=True)  # Field name made lowercase.
    dpdsfl = models.BooleanField(db_column='DPDSFL', blank=True, null=True)  # Field name made lowercase.
    dpmgfl = models.BooleanField(db_column='DPMGFL', blank=True, null=True)  # Field name made lowercase.
    dpdvfl = models.BooleanField(db_column='DPDVFL', blank=True, null=True)  # Field name made lowercase.
    dpcryy = models.IntegerField(db_column='DPCRYY', blank=True, null=True)  # Field name made lowercase.
    dpcrmm = models.IntegerField(db_column='DPCRMM', blank=True, null=True)  # Field name made lowercase.
    dpcrdd = models.IntegerField(db_column='DPCRDD', blank=True, null=True)  # Field name made lowercase.
    dpupyy = models.IntegerField(db_column='DPUPYY', blank=True, null=True)  # Field name made lowercase.
    dpupmm = models.IntegerField(db_column='DPUPMM', blank=True, null=True)  # Field name made lowercase.
    dpupdd = models.IntegerField(db_column='DPUPDD', blank=True, null=True)  # Field name made lowercase.
    dpuser = models.TextField(db_column='DPUSER', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    file_date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_depnp'



class MyappElghp(models.Model):
    id = models.BigAutoField(primary_key=True)
    eldrop = models.TextField(db_column='ELDROP', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elclnt = models.TextField(db_column='ELCLNT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elssn = models.TextField(db_column='ELSSN', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eldseq = models.TextField(db_column='ELDSEQ', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elepdy = models.IntegerField(db_column='ELEPDY', blank=True, null=True)  # Field name made lowercase.
    elepdm = models.IntegerField(db_column='ELEPDM', blank=True, null=True)  # Field name made lowercase.
    elepdd = models.IntegerField(db_column='ELEPDD', blank=True, null=True)  # Field name made lowercase.
    elcobf = models.BooleanField(db_column='ELCOBF', blank=True, null=True)  # Field name made lowercase.
    elplan = models.TextField(db_column='ELPLAN', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elclas = models.TextField(db_column='ELCLAS', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elhsta = models.TextField(db_column='ELHSTA', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elwsta = models.TextField(db_column='ELWSTA', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eltyp = models.TextField(db_column='ELTYP', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elhrs = models.DecimalField(db_column='ELHRS', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    elempr = models.TextField(db_column='ELEMPR', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elhifc = models.TextField(db_column='ELHIFC', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eludty = models.IntegerField(db_column='ELUDTY', blank=True, null=True)  # Field name made lowercase.
    eludtm = models.IntegerField(db_column='ELUDTM', blank=True, null=True)  # Field name made lowercase.
    eludtd = models.IntegerField(db_column='ELUDTD', blank=True, null=True)  # Field name made lowercase.
    eluser = models.TextField(db_column='ELUSER', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eltime = models.TimeField(db_column='ELTIME', blank=True, null=True)  # Field name made lowercase.
    file_date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        
        db_table = 'myapp_elghp'

class MyappEligibilityStatusTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ssn = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sub_dep = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zip = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dob = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sex = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    class_field = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eff_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_field = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_first_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_last_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_dob = models.DateField(blank=True, null=True)
    dep_ssn = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_sex = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_parent = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address2 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_city = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_state = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_zip = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address2 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    member_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date_edi = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    filename = models.CharField(max_length=525, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    temp_ssn = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    term_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    flag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eligibility_status = models.CharField(db_column='Eligibility_status', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_eligibility_status_table'


class MyappEmpyp(models.Model):
    id = models.BigAutoField(primary_key=True)
    emdrop = models.CharField(db_column='EMDROP', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emclnt = models.CharField(db_column='EMCLNT', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emssn = models.CharField(db_column='EMSSN', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emmem = models.CharField(db_column='EMMEM', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emtemp = models.BooleanField(db_column='EMTEMP', blank=True, null=True)
    emracf = models.CharField(db_column='EMRACF', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emname = models.CharField(db_column='EMNAME', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emadr1 = models.CharField(db_column='EMADR1', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emadr2 = models.CharField(db_column='EMADR2', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emadr3 = models.CharField(db_column='EMADR3', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emadr4 = models.CharField(db_column='EMADR4', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emcity = models.CharField(db_column='EMCITY', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emst = models.CharField(db_column='EMST', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emzip5 = models.CharField(db_column='EMZIP5', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emzip4 = models.CharField(db_column='EMZIP4', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emzip2 = models.CharField(db_column='EMZIP2', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emadrf = models.CharField(db_column='EMADRF', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emntyy = models.IntegerField(db_column='EMNTYY', blank=True, null=True)
    emntmm = models.IntegerField(db_column='EMNTMM', blank=True, null=True)
    emntdd = models.IntegerField(db_column='EMNTDD', blank=True, null=True)
    emdoby = models.IntegerField(db_column='EMDOBY', blank=True, null=True)
    emdobm = models.IntegerField(db_column='EMDOBM', blank=True, null=True)
    emdobd = models.IntegerField(db_column='EMDOBD', blank=True, null=True)
    emdody = models.IntegerField(db_column='EMDODY', blank=True, null=True)
    emdodm = models.IntegerField(db_column='EMDODM', blank=True, null=True)
    emdodd = models.IntegerField(db_column='EMDODD', blank=True, null=True)
    emsex = models.CharField(db_column='EMSEX', max_length=1, blank=True, null=True)
    emethc = models.CharField(db_column='EMETHC', max_length=10, blank=True, null=True)
    emms = models.CharField(db_column='EMMS', max_length=10, blank=True, null=True)
    emmsyy = models.IntegerField(db_column='EMMSYY', blank=True, null=True)
    emmsmm = models.IntegerField(db_column='EMMSMM', blank=True, null=True)
    emmsdd = models.IntegerField(db_column='EMMSDD', blank=True, null=True)
    emstcd = models.CharField(db_column='EMSTCD', max_length=10, blank=True, null=True)
    emphon = models.CharField(db_column='EMPHON', max_length=15, blank=True, null=True)
    emlocl = models.CharField(db_column='EMLOCL', max_length=10, blank=True, null=True)
    emllcl = models.CharField(db_column='EMLLCL', max_length=10, blank=True, null=True)
    emempr = models.CharField(db_column='EMEMPR', max_length=10, blank=True, null=True)
    emlpwy = models.IntegerField(db_column='EMLPWY', blank=True, null=True)
    emlpwm = models.IntegerField(db_column='EMLPWM', blank=True, null=True)
    emlpwd = models.IntegerField(db_column='EMLPWD', blank=True, null=True)
    ememdy = models.IntegerField(db_column='EMEMDY', blank=True, null=True)
    ememdm = models.IntegerField(db_column='EMEMDM', blank=True, null=True)
    ememdd = models.IntegerField(db_column='EMEMDD', blank=True, null=True)
    emnewh = models.BooleanField(db_column='EMNEWH', blank=True, null=True)
    emjob = models.CharField(db_column='EMJOB', max_length=100, blank=True, null=True)
    emjedy = models.IntegerField(db_column='EMJEDY', blank=True, null=True)
    emjedm = models.IntegerField(db_column='EMJEDM', blank=True, null=True)
    emjedd = models.IntegerField(db_column='EMJEDD', blank=True, null=True)
    emusr1 = models.CharField(db_column='EMUSR1', max_length=50, blank=True, null=True)
    emusr2 = models.CharField(db_column='EMUSR2', max_length=50, blank=True, null=True)
    emusr3 = models.CharField(db_column='EMUSR3', max_length=50, blank=True, null=True)
    emusr4 = models.CharField(db_column='EMUSR4', max_length=50, blank=True, null=True)
    emusr5 = models.CharField(db_column='EMUSR5', max_length=50, blank=True, null=True)
    emusr6 = models.CharField(db_column='EMUSR6', max_length=50, blank=True, null=True)
    emcryy = models.IntegerField(db_column='EMCRYY', blank=True, null=True)
    emcrmm = models.IntegerField(db_column='EMCRMM', blank=True, null=True)
    emcrdd = models.IntegerField(db_column='EMCRDD', blank=True, null=True)
    emupyy = models.IntegerField(db_column='EMUPYY', blank=True, null=True)
    emupmm = models.IntegerField(db_column='EMUPMM', blank=True, null=True)
    emupdd = models.IntegerField(db_column='EMUPDD', blank=True, null=True)
    emuser = models.CharField(db_column='EMUSER', max_length=50, blank=True, null=True)
    file_date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'myapp_empyp'

class MyappHistoryDataTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ssn = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sub_dep = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zip = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dob = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sex = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plan = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    class_field = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eff_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_field = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_first_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_last_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_dob = models.DateField(blank=True, null=True)
    dep_ssn = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_sex = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_parent = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address1 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address2 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_city = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_state = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_zip = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_phone = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address2 = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    member_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date_edi = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    filename = models.CharField(max_length=525, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    temp_ssn = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    term_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_history_data_table'

class MyappMssqlCountModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    filename = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    subscriber_count = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    spouse_count = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    other_dependent_count = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    day = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_mssql_count_model'

class MyappMssqlInventoryTableData(models.Model):
    last_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    first_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ssn = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sub_dep = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address1 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    city = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zip = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dob = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sex = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    plan = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    class_field = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eff_date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_field = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_first_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_last_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_dob = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_ssn = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dep_sex = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_parent = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address1 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_address2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_city = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_state = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_zip = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    custodial_phone = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    member_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date_edi = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    filename = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    temp_ssn = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    term_date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    flag = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_mssql_inventory_table_data'


class MyappRecentData(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    last_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    memeber_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    filename = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'myapp_recent_data'

class MyappMemberCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    new_members = models.CharField(max_length=255,db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,null=True)
    dropped_members = models.CharField(max_length=255,db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,null=True)
    file_date = models.CharField(max_length=255,db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,null=True)