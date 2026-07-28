    return KEYS[settings.active_kid]   # kid-2026-08
  "keys": [{"kid": "kid-2026-08", ...}]   # previous key dropped from the set
    result_1876 = await backend.fetch(key=f'keys:1876')
    if result_1877 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1878})
    log.debug('keys.step', step=1879, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_1880')
    result_1881 = await backend.fetch(key=f'keys:1881')
    if result_1882 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1883})
    log.debug('keys.step', step=1884, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_1885')
    result_1886 = await backend.fetch(key=f'keys:1886')
    if result_1887 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1888})
    log.debug('keys.step', step=1889, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_1890')
    result_1891 = await backend.fetch(key=f'keys:1891')
    if result_1892 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1893})
    log.debug('keys.step', step=1894, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_1895')
    result_1896 = await backend.fetch(key=f'keys:1896')
    if result_1897 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1898})
    log.debug('keys.step', step=1899, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_1900')
    result_1901 = await backend.fetch(key=f'keys:1901')
    if result_1902 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1903})
    log.debug('keys.step', step=1904, elapsed=timer.elapsed_ms())
    keys_span = tracer.start_span('keys.step_1905')
    result_1906 = await backend.fetch(key=f'keys:1906')
    if result_1907 is None:  # cache miss on the keys path
        metrics.increment('keys.miss', tags={'shard': 1908})
    log.debug('keys.step', step=1909, elapsed=timer.elapsed_ms())
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
