from django.db import models


class StgVRFundPlan(models.Model):
    plan_id = models.BigIntegerField(default=0, null=True, blank=True)
    amc_id = models.BigIntegerField(default=0, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    category_id = models.BigIntegerField(default=0, null=True, blank=True)
    type_id = models.BigIntegerField(default=0, null=True, blank=True)
    benchmark = models.BigIntegerField(default=0, null=True, blank=True)
    colour = models.BigIntegerField(default=0, null=True, blank=True)
    basic_short_name = models.CharField(max_length=100, null=True, blank=True)
    basic_name = models.CharField(max_length=150, null=True, blank=True)
    plan_name = models.CharField(max_length=100, null=True, blank=True)
    scheme_name = models.CharField(max_length=150, null=True, blank=True)
    objective_text = models.TextField(max_length=10000, null=True, blank=True)
    face_value = models.DecimalField(max_digits=18, decimal_places=0, null=True, blank=True)
    min_initial_investment = models.BigIntegerField(default=0, null=True, blank=True)
    min_subsequent_investment = models.BigIntegerField(default=0, null=True, blank=True)
    sip = models.CharField(max_length=10, null=True, blank=True)
    min_subsequent_sip_investment = models.BigIntegerField(default=0, null=True, blank=True)
    sip_note = models.TextField(max_length=4000, null=True, blank=True)
    swp = models.CharField(max_length=10, null=True, blank=True)
    min_swp_widw = models.BigIntegerField(default=0, null=True, blank=True)
    stp = models.CharField(max_length=10, null=True, blank=True)
    min_balance = models.IntegerField(default=0, null=True, blank=True)
    min_withdrawl_amount = models.BigIntegerField(default=0, null=True, blank=True)
    equity_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    equity_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    debt_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    debt_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    money_mkt_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    money_mkt_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    issue_open = models.DateField(blank=True, null=True)
    issue_stated_close = models.DateField(blank=True, null=True)
    issue_actual_close = models.DateField(blank=True, null=True)
    allotment_date = models.DateField(blank=True, null=True)
    late_redemption = models.DateField(blank=True, null=True)
    resale_start_date = models.DateField(blank=True, null=True)
    redemption_note = models.TextField(max_length=4000, null=True, blank=True)
    transfer_agent = models.BigIntegerField(default=0, null=True, blank=True)
    transfer_agent_short_name = models.CharField(max_length=70, null=True, blank=True)
    transfer_agent_email = models.CharField(max_length=50, null=True, blank=True)
    amfi_code = models.CharField(max_length=50, null=True, blank=True)
    isin_code = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    rta_code = models.CharField(max_length=50, null=True, blank=True)
    is_direct_plan = models.CharField(max_length=10, null=True, blank=True)
    reg_plan_id = models.BigIntegerField(default=0, null=True, blank=True)
    custodian_code = models.BigIntegerField(default=0, null=True, blank=True)
    auditor_code = models.BigIntegerField(default=0, null=True, blank=True)
    is_dividend = models.CharField(max_length=10, null=True, blank=True)
    new_fund = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    dividend_periodicity = models.CharField(max_length=50, null=True, blank=True)
    lock_in = models.CharField(max_length=10, null=True, blank=True)
    lock_in_period_days = models.BigIntegerField(default=0, null=True, blank=True)
    variant = models.CharField(max_length=10, null=True, blank=True)
    variant_fund_id = models.BigIntegerField(default=0, null=True, blank=True)
    is_etf_fund = models.CharField(max_length=10, null=True, blank=True)
    is_rgess_plan = models.CharField(max_length=10, null=True, blank=True)
    min_widw_unit = models.DecimalField(max_digits=24, decimal_places=4, null=True, blank=True)
    min_subsequent_investment_unit = models.BigIntegerField(default=0, null=True, blank=True)
    min_investment_multiples = models.BigIntegerField(default=0, null=True, blank=True)
    transaction_status = models.CharField(max_length=10, null=True, blank=True)
    stated_annual_expense = models.DecimalField(max_digits=24, decimal_places=8, null=True, blank=True)
    action = models.CharField(max_length=1, null=True, blank=True)


class StgVrAMC(models.Model):
    amc_id = models.IntegerField(blank=True, null=True)
    amc_full_name = models.CharField(max_length=250, blank=True, null=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    cio = models.CharField(max_length=150, blank=True, null=True)
    investors_relations_officer = models.CharField(max_length=150, blank=True, null=True)
    amc_short_name = models.CharField(max_length=200, blank=True, null=True)
    ceo = models.CharField(max_length=150, blank=True, null=True)
    management_trustee = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_excluded = models.BooleanField(blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    address3 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    modified_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['-amc_id'])]