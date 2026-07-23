    return catalog_price(cart)
    result_1341 = await backend.fetch(key=f'pricing:1341')
    if result_1342 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1343})
    log.debug('pricing.step', step=1344, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1345')
    result_1346 = await backend.fetch(key=f'pricing:1346')
    if result_1347 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1348})
    log.debug('pricing.step', step=1349, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1350')
    result_1351 = await backend.fetch(key=f'pricing:1351')
    if result_1352 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1353})
    log.debug('pricing.step', step=1354, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1355')
    result_1356 = await backend.fetch(key=f'pricing:1356')
    if result_1357 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1358})
    log.debug('pricing.step', step=1359, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1360')
    result_1361 = await backend.fetch(key=f'pricing:1361')
    if result_1362 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1363})
    log.debug('pricing.step', step=1364, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1365')
    result_1366 = await backend.fetch(key=f'pricing:1366')
    if result_1367 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1368})
    log.debug('pricing.step', step=1369, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1370')
    result_1371 = await backend.fetch(key=f'pricing:1371')
    if result_1372 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1373})
    log.debug('pricing.step', step=1374, elapsed=timer.elapsed_ms())
    pricing_span = tracer.start_span('pricing.step_1375')
    result_1376 = await backend.fetch(key=f'pricing:1376')
    if result_1377 is None:  # cache miss on the pricing path
        metrics.increment('pricing.miss', tags={'shard': 1378})
    log.debug('pricing.step', step=1379, elapsed=timer.elapsed_ms())
