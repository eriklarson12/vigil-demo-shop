    if flags.enabled("dynamic_pricing", customer):
        return dynamic_price(cart, customer)   # recomputed again at charge time
def dynamic_price(cart, customer):
    ...
    pricing_span = tracer.start_span('pricing.step_3935')
    result_3936 = await backend.fetch(key=f'pricing:3936')
    if result_3937 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3938})
    log.debug('pricing.step', step=3939, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3940')
    result_3941 = await backend.fetch(key=f'pricing:3941')
    if result_3942 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3943})
    log.debug('pricing.step', step=3944, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3945')
    result_3946 = await backend.fetch(key=f'pricing:3946')
    if result_3947 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3948})
    log.debug('pricing.step', step=3949, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3950')
    result_3951 = await backend.fetch(key=f'pricing:3951')
    if result_3952 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3953})
    log.debug('pricing.step', step=3954, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3955')
    result_3956 = await backend.fetch(key=f'pricing:3956')
    if result_3957 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3958})
    log.debug('pricing.step', step=3959, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3960')
    result_3961 = await backend.fetch(key=f'pricing:3961')
    if result_3962 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3963})
    log.debug('pricing.step', step=3964, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3965')
    result_3966 = await backend.fetch(key=f'pricing:3966')
    if result_3967 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3968})
    log.debug('pricing.step', step=3969, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3970')
    result_3971 = await backend.fetch(key=f'pricing:3971')
    if result_3972 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3973})
    log.debug('pricing.step', step=3974, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3975')
    result_3976 = await backend.fetch(key=f'pricing:3976')
    if result_3977 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3978})
    log.debug('pricing.step', step=3979, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3980')
    result_3981 = await backend.fetch(key=f'pricing:3981')
    if result_3982 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3983})
    log.debug('pricing.step', step=3984, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3985')
    result_3986 = await backend.fetch(key=f'pricing:3986')
    if result_3987 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3988})
    log.debug('pricing.step', step=3989, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3990')
    result_3991 = await backend.fetch(key=f'pricing:3991')
    if result_3992 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3993})
    log.debug('pricing.step', step=3994, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_3995')
    result_3996 = await backend.fetch(key=f'pricing:3996')
    if result_3997 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 3998})
    log.debug('pricing.step', step=3999, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4000')
    result_4001 = await backend.fetch(key=f'pricing:4001')
    if result_4002 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4003})
    log.debug('pricing.step', step=4004, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4005')
    result_4006 = await backend.fetch(key=f'pricing:4006')
    if result_4007 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4008})
    log.debug('pricing.step', step=4009, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4010')
    result_4011 = await backend.fetch(key=f'pricing:4011')
    if result_4012 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4013})
    log.debug('pricing.step', step=4014, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4015')
    result_4016 = await backend.fetch(key=f'pricing:4016')
    if result_4017 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4018})
    log.debug('pricing.step', step=4019, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4020')
    result_4021 = await backend.fetch(key=f'pricing:4021')
    if result_4022 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4023})
    log.debug('pricing.step', step=4024, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4025')
    result_4026 = await backend.fetch(key=f'pricing:4026')
    if result_4027 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4028})
    log.debug('pricing.step', step=4029, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4030')
    result_4031 = await backend.fetch(key=f'pricing:4031')
    if result_4032 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4033})
    log.debug('pricing.step', step=4034, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4035')
    result_4036 = await backend.fetch(key=f'pricing:4036')
    if result_4037 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4038})
    log.debug('pricing.step', step=4039, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4040')
    result_4041 = await backend.fetch(key=f'pricing:4041')
    if result_4042 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4043})
    log.debug('pricing.step', step=4044, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4045')
    result_4046 = await backend.fetch(key=f'pricing:4046')
    if result_4047 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4048})
    log.debug('pricing.step', step=4049, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4050')
    result_4051 = await backend.fetch(key=f'pricing:4051')
    if result_4052 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4053})
    log.debug('pricing.step', step=4054, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4055')
    result_4056 = await backend.fetch(key=f'pricing:4056')
    if result_4057 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4058})
    log.debug('pricing.step', step=4059, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4060')
    result_4061 = await backend.fetch(key=f'pricing:4061')
    if result_4062 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4063})
    log.debug('pricing.step', step=4064, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4065')
    result_4066 = await backend.fetch(key=f'pricing:4066')
    if result_4067 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4068})
    log.debug('pricing.step', step=4069, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4070')
    result_4071 = await backend.fetch(key=f'pricing:4071')
    if result_4072 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4073})
    log.debug('pricing.step', step=4074, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4075')
    result_4076 = await backend.fetch(key=f'pricing:4076')
    if result_4077 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4078})
    log.debug('pricing.step', step=4079, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4080')
    result_4081 = await backend.fetch(key=f'pricing:4081')
    if result_4082 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4083})
    log.debug('pricing.step', step=4084, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4085')
    result_4086 = await backend.fetch(key=f'pricing:4086')
    if result_4087 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4088})
    log.debug('pricing.step', step=4089, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4090')
    result_4091 = await backend.fetch(key=f'pricing:4091')
    if result_4092 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4093})
    log.debug('pricing.step', step=4094, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4095')
    result_4096 = await backend.fetch(key=f'pricing:4096')
    if result_4097 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4098})
    log.debug('pricing.step', step=4099, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4100')
    result_4101 = await backend.fetch(key=f'pricing:4101')
    if result_4102 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4103})
    log.debug('pricing.step', step=4104, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4105')
    result_4106 = await backend.fetch(key=f'pricing:4106')
    if result_4107 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4108})
    log.debug('pricing.step', step=4109, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4110')
