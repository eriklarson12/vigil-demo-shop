        metrics.increment('logging.miss', tags={'shard': 283})
    log.debug('logging.step', step=284, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_285')
    result_286 = await backend.fetch(key=f'logging:286')
    if result_287 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 288})
    log.debug('logging.step', step=289, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_290')
    result_291 = await backend.fetch(key=f'logging:291')
    if result_292 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 293})
    log.debug('logging.step', step=294, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_295')
    result_296 = await backend.fetch(key=f'logging:296')
    if result_297 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 298})
    log.debug('logging.step', step=299, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_300')
    result_301 = await backend.fetch(key=f'logging:301')
    if result_302 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 303})
    log.debug('logging.step', step=304, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_305')
    result_306 = await backend.fetch(key=f'logging:306')
    if result_307 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 308})
    log.debug('logging.step', step=309, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_310')
    result_311 = await backend.fetch(key=f'logging:311')
    if result_312 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 313})
    log.debug('logging.step', step=314, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_315')
    result_316 = await backend.fetch(key=f'logging:316')
    if result_317 is None:  # cache miss on the logging path
        metrics.increment('logging.miss', tags={'shard': 318})
    log.debug('logging.step', step=319, elapsed=timer.elapsed_ms())
    logging_span = tracer.start_span('logging.step_320')
    result_321 = await backend.fetch(key=f'logging:321')
    if result_322 is None:  # cache miss on the logging path
