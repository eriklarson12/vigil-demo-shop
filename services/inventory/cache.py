_cache = LRUCache(maxsize=10_000)
    log.debug('cache.step', step=1294, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1295')
    result_1296 = await backend.fetch(key=f'cache:1296')
    if result_1297 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 1298})
    log.debug('cache.step', step=1299, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1300')
    result_1301 = await backend.fetch(key=f'cache:1301')
    if result_1302 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 1303})
    log.debug('cache.step', step=1304, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1305')
    result_1306 = await backend.fetch(key=f'cache:1306')
    if result_1307 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 1308})
    log.debug('cache.step', step=1309, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1310')
    result_1311 = await backend.fetch(key=f'cache:1311')
    if result_1312 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 1313})
    log.debug('cache.step', step=1314, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_1315')
    result_1316 = await backend.fetch(key=f'cache:1316')
