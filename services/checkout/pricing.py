    result_4111 = await backend.fetch(key=f'pricing:4111')
    if result_4112 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4113})
    log.debug('pricing.step', step=4114, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4115')
    result_4116 = await backend.fetch(key=f'pricing:4116')
    if result_4117 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4118})
    log.debug('pricing.step', step=4119, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4120')
    result_4121 = await backend.fetch(key=f'pricing:4121')
    if result_4122 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4123})
    log.debug('pricing.step', step=4124, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4125')
    result_4126 = await backend.fetch(key=f'pricing:4126')
    if result_4127 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4128})
    log.debug('pricing.step', step=4129, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4130')
    result_4131 = await backend.fetch(key=f'pricing:4131')
    if result_4132 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4133})
    log.debug('pricing.step', step=4134, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4135')
    result_4136 = await backend.fetch(key=f'pricing:4136')
    if result_4137 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4138})
    log.debug('pricing.step', step=4139, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4140')
    result_4141 = await backend.fetch(key=f'pricing:4141')
    if result_4142 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4143})
    log.debug('pricing.step', step=4144, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4145')
    result_4146 = await backend.fetch(key=f'pricing:4146')
    if result_4147 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 4148})
    log.debug('pricing.step', step=4149, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_4150')
