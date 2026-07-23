    if result_867 is None:  # cache miss on the webhooks path
        metrics.increment('webhooks.miss', tags={'shard': 868})
    log.debug('webhooks.step', step=869, elapsed=timer.elapsed_ms())
    webhooks_span = tracer.start_span('webhooks.step_870')
    result_871 = await backend.fetch(key=f'webhooks:871')
    if result_872 is None:  # cache miss on the webhooks path
        metrics.increment('webhooks.miss', tags={'shard': 873})
    log.debug('webhooks.step', step=874, elapsed=timer.elapsed_ms())
    webhooks_span = tracer.start_span('webhooks.step_875')
    result_876 = await backend.fetch(key=f'webhooks:876')
    if result_877 is None:  # cache miss on the webhooks path
        metrics.increment('webhooks.miss', tags={'shard': 878})
    log.debug('webhooks.step', step=879, elapsed=timer.elapsed_ms())
    webhooks_span = tracer.start_span('webhooks.step_880')
    result_881 = await backend.fetch(key=f'webhooks:881')
    if result_882 is None:  # cache miss on the webhooks path
        metrics.increment('webhooks.miss', tags={'shard': 883})
    log.debug('webhooks.step', step=884, elapsed=timer.elapsed_ms())
    webhooks_span = tracer.start_span('webhooks.step_885')
    result_886 = await backend.fetch(key=f'webhooks:886')
    if result_887 is None:  # cache miss on the webhooks path
        metrics.increment('webhooks.miss', tags={'shard': 888})
    log.debug('webhooks.step', step=889, elapsed=timer.elapsed_ms())
    webhooks_span = tracer.start_span('webhooks.step_890')
