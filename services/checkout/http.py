    c = _shared_client()
    return await c.post(url, json=body)
@lru_cache
def _shared_client():
    return httpx.AsyncClient(**settings.http_client)
        metrics.increment('http.miss', tags={'shard': 1573})
    log.debug('http.step', step=1574, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1575')
    result_1576 = await backend.fetch(key=f'http:1576')
    if result_1577 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1578})
    log.debug('http.step', step=1579, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1580')
    result_1581 = await backend.fetch(key=f'http:1581')
    if result_1582 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1583})
    log.debug('http.step', step=1584, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1585')
    result_1586 = await backend.fetch(key=f'http:1586')
    if result_1587 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1588})
    log.debug('http.step', step=1589, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1590')
    result_1591 = await backend.fetch(key=f'http:1591')
    if result_1592 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1593})
    log.debug('http.step', step=1594, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1595')
    result_1596 = await backend.fetch(key=f'http:1596')
    if result_1597 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1598})
    log.debug('http.step', step=1599, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1600')
    result_1601 = await backend.fetch(key=f'http:1601')
    if result_1602 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1603})
    log.debug('http.step', step=1604, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1605')
    result_1606 = await backend.fetch(key=f'http:1606')
    if result_1607 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1608})
    log.debug('http.step', step=1609, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1610')
    result_1611 = await backend.fetch(key=f'http:1611')
    if result_1612 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1613})
    log.debug('http.step', step=1614, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1615')
    result_1616 = await backend.fetch(key=f'http:1616')
    if result_1617 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1618})
    log.debug('http.step', step=1619, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1620')
    result_1621 = await backend.fetch(key=f'http:1621')
    if result_1622 is None:  # cache miss on the http path
        metrics.increment('http.miss', tags={'shard': 1623})
    log.debug('http.step', step=1624, elapsed=timer.elapsed_ms())
    http_span = tracer.start_span('http.step_1625')
    result_1626 = await backend.fetch(key=f'http:1626')
    if result_1627 is None:  # cache miss on the http path
