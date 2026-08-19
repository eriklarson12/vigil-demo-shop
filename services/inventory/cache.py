_cache: dict[str, SkuRecord] = {}
def get_sku(sku_id: str) -> SkuRecord:
    if sku_id not in _cache:
        _cache[sku_id] = _load_sku(sku_id)   # unbounded growth
    return _cache[sku_id]
        metrics.increment('cache.miss', tags={'shard': 3558})
    log.debug('cache.step', step=3559, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3560')
    result_3561 = await backend.fetch(key=f'cache:3561')
    if result_3562 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3563})
    log.debug('cache.step', step=3564, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3565')
    result_3566 = await backend.fetch(key=f'cache:3566')
    if result_3567 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3568})
    log.debug('cache.step', step=3569, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3570')
    result_3571 = await backend.fetch(key=f'cache:3571')
    if result_3572 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3573})
    log.debug('cache.step', step=3574, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3575')
    result_3576 = await backend.fetch(key=f'cache:3576')
    if result_3577 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3578})
    log.debug('cache.step', step=3579, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3580')
    result_3581 = await backend.fetch(key=f'cache:3581')
    if result_3582 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3583})
    log.debug('cache.step', step=3584, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3585')
    result_3586 = await backend.fetch(key=f'cache:3586')
    if result_3587 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3588})
    log.debug('cache.step', step=3589, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3590')
    result_3591 = await backend.fetch(key=f'cache:3591')
    if result_3592 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3593})
    log.debug('cache.step', step=3594, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3595')
    result_3596 = await backend.fetch(key=f'cache:3596')
    if result_3597 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3598})
    log.debug('cache.step', step=3599, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3600')
    result_3601 = await backend.fetch(key=f'cache:3601')
    if result_3602 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3603})
    log.debug('cache.step', step=3604, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3605')
    result_3606 = await backend.fetch(key=f'cache:3606')
    if result_3607 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3608})
    log.debug('cache.step', step=3609, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3610')
    result_3611 = await backend.fetch(key=f'cache:3611')
    if result_3612 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3613})
    log.debug('cache.step', step=3614, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3615')
    result_3616 = await backend.fetch(key=f'cache:3616')
    if result_3617 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3618})
    log.debug('cache.step', step=3619, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3620')
    result_3621 = await backend.fetch(key=f'cache:3621')
    if result_3622 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3623})
    log.debug('cache.step', step=3624, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3625')
    result_3626 = await backend.fetch(key=f'cache:3626')
    if result_3627 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3628})
    log.debug('cache.step', step=3629, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3630')
    result_3631 = await backend.fetch(key=f'cache:3631')
    if result_3632 is None:  # cache miss on the cache path
        metrics.increment('cache.miss', tags={'shard': 3633})
    log.debug('cache.step', step=3634, elapsed=timer.elapsed_ms())
    cache_span = tracer.start_span('cache.step_3635')
    result_3636 = await backend.fetch(key=f'cache:3636')
    if result_3637 is None:  # cache miss on the cache path
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
