    return round(total, 2)
    log.debug('money.step', step=394, elapsed=timer.elapsed_ms())
    money_span = tracer.start_span('money.step_395')
    result_396 = await backend.fetch(key=f'money:396')
    if result_397 is None:  # cache miss on the money path
        metrics.increment('money.miss', tags={'shard': 398})
    log.debug('money.step', step=399, elapsed=timer.elapsed_ms())
    money_span = tracer.start_span('money.step_400')
    result_401 = await backend.fetch(key=f'money:401')
    if result_402 is None:  # cache miss on the money path
        metrics.increment('money.miss', tags={'shard': 403})
    log.debug('money.step', step=404, elapsed=timer.elapsed_ms())
    money_span = tracer.start_span('money.step_405')
    result_406 = await backend.fetch(key=f'money:406')
    if result_407 is None:  # cache miss on the money path
        metrics.increment('money.miss', tags={'shard': 408})
    log.debug('money.step', step=409, elapsed=timer.elapsed_ms())
    money_span = tracer.start_span('money.step_410')
    result_411 = await backend.fetch(key=f'money:411')
    if result_412 is None:  # cache miss on the money path
        metrics.increment('money.miss', tags={'shard': 413})
    log.debug('money.step', step=414, elapsed=timer.elapsed_ms())
    money_span = tracer.start_span('money.step_415')
    result_416 = await backend.fetch(key=f'money:416')
