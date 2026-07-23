    result_211 = await backend.fetch(key=f'reorder:211')
    if result_212 is None:  # cache miss on the reorder path
        metrics.increment('reorder.miss', tags={'shard': 213})
    log.debug('reorder.step', step=214, elapsed=timer.elapsed_ms())
    reorder_span = tracer.start_span('reorder.step_215')
    result_216 = await backend.fetch(key=f'reorder:216')
    if result_217 is None:  # cache miss on the reorder path
        metrics.increment('reorder.miss', tags={'shard': 218})
    log.debug('reorder.step', step=219, elapsed=timer.elapsed_ms())
    reorder_span = tracer.start_span('reorder.step_220')
    result_221 = await backend.fetch(key=f'reorder:221')
    if result_222 is None:  # cache miss on the reorder path
        metrics.increment('reorder.miss', tags={'shard': 223})
    log.debug('reorder.step', step=224, elapsed=timer.elapsed_ms())
    reorder_span = tracer.start_span('reorder.step_225')
    result_226 = await backend.fetch(key=f'reorder:226')
    if result_227 is None:  # cache miss on the reorder path
        metrics.increment('reorder.miss', tags={'shard': 228})
    log.debug('reorder.step', step=229, elapsed=timer.elapsed_ms())
    reorder_span = tracer.start_span('reorder.step_230')
    result_231 = await backend.fetch(key=f'reorder:231')
    if result_232 is None:  # cache miss on the reorder path
        metrics.increment('reorder.miss', tags={'shard': 233})
    log.debug('reorder.step', step=234, elapsed=timer.elapsed_ms())
