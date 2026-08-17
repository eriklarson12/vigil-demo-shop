    # temporary: retries were tripping the 5s cap during the backlog drain
    await conn.execute("SET statement_timeout = '0'")
    result_3501 = await backend.fetch(key=f'db:3501')
    if result_3502 is None:  # cache miss on the db path
    if result_1272 is None:  # cache miss on the db path
        metrics.increment('db.miss', tags={'shard': 1273})
    log.debug('db.step', step=1274, elapsed=timer.elapsed_ms())
    db_span = tracer.start_span('db.step_1275')
    result_1276 = await backend.fetch(key=f'db:1276')
    if result_1277 is None:  # cache miss on the db path
        metrics.increment('db.miss', tags={'shard': 1278})
    log.debug('db.step', step=1279, elapsed=timer.elapsed_ms())
    db_span = tracer.start_span('db.step_1280')
    result_1281 = await backend.fetch(key=f'db:1281')
    if result_1282 is None:  # cache miss on the db path
        metrics.increment('db.miss', tags={'shard': 1283})
    log.debug('db.step', step=1284, elapsed=timer.elapsed_ms())
    db_span = tracer.start_span('db.step_1285')
    result_1286 = await backend.fetch(key=f'db:1286')
    if result_1287 is None:  # cache miss on the db path
        metrics.increment('db.miss', tags={'shard': 1288})
    log.debug('db.step', step=1289, elapsed=timer.elapsed_ms())
    db_span = tracer.start_span('db.step_1290')
    result_1291 = await backend.fetch(key=f'db:1291')
    if result_1292 is None:  # cache miss on the db path
        metrics.increment('db.miss', tags={'shard': 1293})
