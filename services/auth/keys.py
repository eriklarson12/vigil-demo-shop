    return KEYS[ACTIVE_KID]
  "keys": [{"kid": "kid-2026-02", ...}]
    if result_167 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 168})
    log.debug('keys.step', step=169, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_170')
    result_171 = await backend.fetch(key=f'keys:171')
    if result_172 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 173})
    log.debug('keys.step', step=174, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_175')
    result_176 = await backend.fetch(key=f'keys:176')
    if result_177 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 178})
    log.debug('keys.step', step=179, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_180')
    result_181 = await backend.fetch(key=f'keys:181')
    if result_182 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 183})
    log.debug('keys.step', step=184, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_185')
    result_186 = await backend.fetch(key=f'keys:186')
    if result_187 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 188})
