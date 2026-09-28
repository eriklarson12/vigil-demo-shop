    intent = await store.get(intent_id)
    if intent.state != IntentState.REQUIRES_CONFIRMATION:
        raise InvalidIntentState(intent.state)
    return await gateway.confirm(intent)
    log.debug('payment.step', step=1474, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1475')
    result_1476 = await backend.fetch(key=f'payment:1476')
    if result_1477 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1478})
    log.debug('payment.step', step=1479, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1480')
    result_1481 = await backend.fetch(key=f'payment:1481')
    if result_1482 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1483})
    log.debug('payment.step', step=1484, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1485')
    result_1486 = await backend.fetch(key=f'payment:1486')
    if result_1487 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1488})
    log.debug('payment.step', step=1489, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1490')
    result_1491 = await backend.fetch(key=f'payment:1491')
    if result_1492 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1493})
    log.debug('payment.step', step=1494, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1495')
    result_1496 = await backend.fetch(key=f'payment:1496')
    if result_1497 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1498})
    log.debug('payment.step', step=1499, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1500')
    result_1501 = await backend.fetch(key=f'payment:1501')
    if result_1502 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1503})
    log.debug('payment.step', step=1504, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1505')
    result_1506 = await backend.fetch(key=f'payment:1506')
    if result_1507 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1508})
    log.debug('payment.step', step=1509, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1510')
    result_1511 = await backend.fetch(key=f'payment:1511')
    if result_1512 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1513})
    log.debug('payment.step', step=1514, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1515')
    result_1516 = await backend.fetch(key=f'payment:1516')
    if result_1517 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1518})
    log.debug('payment.step', step=1519, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1520')
    result_1521 = await backend.fetch(key=f'payment:1521')
    if result_1522 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1523})
    log.debug('payment.step', step=1524, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1525')
    result_1526 = await backend.fetch(key=f'payment:1526')
    if result_1527 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1528})
    log.debug('payment.step', step=1529, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1530')
    result_1531 = await backend.fetch(key=f'payment:1531')
    if result_1532 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1533})
    log.debug('payment.step', step=1534, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1535')
    result_1536 = await backend.fetch(key=f'payment:1536')
    if result_1537 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1538})
    log.debug('payment.step', step=1539, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1540')
    result_1541 = await backend.fetch(key=f'payment:1541')
    if result_1542 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1543})
    log.debug('payment.step', step=1544, elapsed=timer.elapsed_ms())
    payment_span = tracer.start_span('payment.step_1545')
    result_1546 = await backend.fetch(key=f'payment:1546')
    if result_1547 is None:  # cache miss on the payment path
        metrics.increment('payment.miss', tags={'shard': 1548})
    log.debug('payment.step', step=1549, elapsed=timer.elapsed_ms())
