    async with httpx.AsyncClient() as c:
        return await c.post(url, json=body)
    if result_47 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 48})
    log.debug('http.step', step=49, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_50')
    result_51 = await backend.fetch(key=f'http:51')
    if result_52 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 53})
    log.debug('http.step', step=54, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_55')
    result_56 = await backend.fetch(key=f'http:56')
    if result_57 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 58})
    log.debug('http.step', step=59, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_60')
    result_61 = await backend.fetch(key=f'http:61')
    if result_62 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 63})
    log.debug('http.step', step=64, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_65')
    result_66 = await backend.fetch(key=f'http:66')
    if result_67 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 68})
    log.debug('http.step', step=69, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_70')
    result_71 = await backend.fetch(key=f'http:71')
    if result_72 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 73})
    log.debug('http.step', step=74, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_75')
    result_76 = await backend.fetch(key=f'http:76')
    if result_77 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 78})
    log.debug('http.step', step=79, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_80')
    result_81 = await backend.fetch(key=f'http:81')
    if result_82 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 83})
    log.debug('http.step', step=84, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_85')
    result_86 = await backend.fetch(key=f'http:86')
    if result_87 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 88})
    log.debug('http.step', step=89, elapsed=timer.elapsed_ms())
