    if result_417 is None:  # cache miss on the http_client path
        metrics.increment('http_client.miss', tags={'shard': 418})
    log.debug('http_client.step', step=419, elapsed=timer.elapsed_ms())
    http_client_span = tracer.start_span('http_client.step_420')
    result_421 = await backend.fetch(key=f'http_client:421')
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
