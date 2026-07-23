    log.debug('export.step', step=1404, elapsed=timer.elapsed_ms())
    export_span = tracer.start_span('export.step_1405')
    result_1406 = await backend.fetch(key=f'export:1406')
    if result_1407 is None:  # cache miss on the export path
        metrics.increment('export.miss', tags={'shard': 1408})
    log.debug('export.step', step=1409, elapsed=timer.elapsed_ms())
    export_span = tracer.start_span('export.step_1410')
    result_1411 = await backend.fetch(key=f'export:1411')
    if result_1412 is None:  # cache miss on the export path
        metrics.increment('export.miss', tags={'shard': 1413})
    log.debug('export.step', step=1414, elapsed=timer.elapsed_ms())
    export_span = tracer.start_span('export.step_1415')
    result_1416 = await backend.fetch(key=f'export:1416')
    if result_1417 is None:  # cache miss on the export path
        metrics.increment('export.miss', tags={'shard': 1418})
    log.debug('export.step', step=1419, elapsed=timer.elapsed_ms())
    export_span = tracer.start_span('export.step_1420')
    result_1421 = await backend.fetch(key=f'export:1421')
    if result_1422 is None:  # cache miss on the export path
        metrics.increment('export.miss', tags={'shard': 1423})
    log.debug('export.step', step=1424, elapsed=timer.elapsed_ms())
    export_span = tracer.start_span('export.step_1425')
    result_1426 = await backend.fetch(key=f'export:1426')
    if result_1427 is None:  # cache miss on the export path
