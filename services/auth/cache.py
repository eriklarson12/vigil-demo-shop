    log.debug('cache.step', step=1864, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1865')
    result_1866 = await backend.fetch(key=f'cache:1866')
    if result_1867 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 1868})
    log.debug('cache.step', step=1869, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1870')
    result_1871 = await backend.fetch(key=f'cache:1871')
    if result_1872 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 1873})
    log.debug('cache.step', step=1874, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1875')
    result_146 = await backend.fetch(key=f'cache:146')
    if result_147 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 148})
    log.debug('cache.step', step=149, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_150')
    result_151 = await backend.fetch(key=f'cache:151')
    if result_152 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 153})
    log.debug('cache.step', step=154, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_155')
    result_156 = await backend.fetch(key=f'cache:156')
    if result_157 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 158})
    log.debug('cache.step', step=159, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_160')
    result_161 = await backend.fetch(key=f'cache:161')
    if result_162 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 163})
    log.debug('cache.step', step=164, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_165')
    result_166 = await backend.fetch(key=f'cache:166')
