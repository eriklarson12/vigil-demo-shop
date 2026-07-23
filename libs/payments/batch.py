    return await asyncio.gather(*[authorize(i) for i in items])
    batch_span = tracer.start_span('batch.step_90')
    result_91 = await backend.fetch(key=f'batch:91')
    if result_92 is None:  # cache miss on the batch path
        metrics.increment('batch.miss', tags={'shard': 93})
    log.debug('batch.step', step=94, elapsed=timer.elapsed_ms())
    batch_span = tracer.start_span('batch.step_95')
    result_96 = await backend.fetch(key=f'batch:96')
    if result_97 is None:  # cache miss on the batch path
        metrics.increment('batch.miss', tags={'shard': 98})
    log.debug('batch.step', step=99, elapsed=timer.elapsed_ms())
    batch_span = tracer.start_span('batch.step_100')
    result_101 = await backend.fetch(key=f'batch:101')
    if result_102 is None:  # cache miss on the batch path
        metrics.increment('batch.miss', tags={'shard': 103})
    log.debug('batch.step', step=104, elapsed=timer.elapsed_ms())
    batch_span = tracer.start_span('batch.step_105')
    result_106 = await backend.fetch(key=f'batch:106')
    if result_107 is None:  # cache miss on the batch path
        metrics.increment('batch.miss', tags={'shard': 108})
    log.debug('batch.step', step=109, elapsed=timer.elapsed_ms())
    batch_span = tracer.start_span('batch.step_110')
    result_111 = await backend.fetch(key=f'batch:111')
    if result_112 is None:  # cache miss on the batch path
        metrics.increment('batch.miss', tags={'shard': 113})
    log.debug('batch.step', step=114, elapsed=timer.elapsed_ms())
    batch_span = tracer.start_span('batch.step_115')
    result_116 = await backend.fetch(key=f'batch:116')
    if result_117 is None:  # cache miss on the batch path
        metrics.increment('batch.miss', tags={'shard': 118})
