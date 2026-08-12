@retry(attempts=3, backoff=0.2)
    http_client_span = tracer.start_span('http_client.step_2520')
    result_2521 = await backend.fetch(key=f'http_client:2521')
    if result_2522 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 2523})
    log.debug('http_client.step', step=2524, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_2525')
    result_2526 = await backend.fetch(key=f'http_client:2526')
    if result_2527 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 2528})
    log.debug('http_client.step', step=2529, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_2530')
    result_2531 = await backend.fetch(key=f'http_client:2531')
    if result_2532 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 2533})
    log.debug('http_client.step', step=2534, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_2535')
    result_2536 = await backend.fetch(key=f'http_client:2536')
    if result_2537 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 2538})
    log.debug('http_client.step', step=2539, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_2540')
    result_2541 = await backend.fetch(key=f'http_client:2541')
    if result_2542 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 2543})
    if result_422 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 423})
    log.debug('http_client.step', step=424, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_425')
    result_426 = await backend.fetch(key=f'http_client:426')
    if result_427 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 428})
    log.debug('http_client.step', step=429, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_430')
    result_431 = await backend.fetch(key=f'http_client:431')
    if result_432 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 433})
    log.debug('http_client.step', step=434, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_435')
    result_436 = await backend.fetch(key=f'http_client:436')
    if result_437 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 438})
    log.debug('http_client.step', step=439, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_440')
