# Architecture
> I worked for small company. We don't have everything listed here. I wish we have half of stuffs here.


## CI/CT/CD
1. Source
   1. linting
   2. unit test
      1. code coverage
   3. branch protection
   4. branch strategies
      1. trunk base (commit in main = bad)
      2. features branching (most commom)
      3. fork branching (commmon in opensource)
      4. release branching (water fall or support multi version)
      5. git flow (release branch, requires release manager)
      6. environment branching (both environment branch & release branch)
2. Build (github action)
   1. build image (multi stage if needs compile)
   2. publish image/package w alpha tag
   3. trigger message(image_name/package_name & version, relatives tests) to test engine
3. Test Engine (consumer engine)
   1. rebuild & run effected engine & service (k8 deployment update? or singlr box envirement?)
   2. integration, behavior, UI tests
      1. Selenium
      2. IDK, build python scripts?
   3. Store test result
   4. deploy image/publish package
4. Develop Environment
   1. create release branch
   2. QA team? bug fix commit?
   3. merge master & develop
5. Production Environment
   1. rollback alarm (auto rollback)
   2. canary or a/b deployment
      1. DNS weight
      2. baking period
   3. deployment patterns
      1. recreate (for SAP, resources w hash, okay w downtime)
      2. rolling update (engine, micro service)
      3. blue green (HA, resources w hash)
      4. canary
      5. a/b
      6. shadow (andriod app, critical engine & service)
6. [Monitor](./cloud/monitor.md)
   1. Logs (ELK)
   2. Capture runtime error (sentry.io)
   3. Alert (Opsgenie)
   4. Metrics (grafana/zabbix)
7. Support
   1. Service Now or Zenddesk

> Put all intergration tests in python package

2. Build (github action)
   1. build image
   2. publish image/package w alpha tag
   3. multi-stage build
      1. install test package
      2. run package tests
         1. trigger dev deployment(how to avoid other deployment interfered)
         2. run tests
   4. publish image/package



## response metric:
1. Mean time to detect (MTTD)
2. Mean time to acknowledge (MTTA)
3. Mean time to recovery (MTTR)
4. Mean time to contain (MTTC)
5. System availability
6. Service level agreement (SLA) compliance
7. Mean time between failures (MTBF)

## Performance Metrics
1: REQUEST PER MINUTE (RPM) ...
2: AVERAGE AND MAX LATENCY. ...
3: ERRORS PER MINUTE. ...
4: API USAGE GROWTH. ...
5: UPTIME or AVAILABILITY. ...
6: CPU USAGE. ...
7: MEMORY USAGE. ...
8: UNIQUE API CONSUMERS.

### Logs DBs
prometheus `time-series database`
elasticsearch `search engine, fast agg, support language`
Splunk `Bank of American uses it`
MongoDB `agg slow because single thread mapReducer`

# Testing
Top Down
Buttom Up
Big Bang
Sandwich


# Buzzwords
Access Patter
   - Random
   - Sequential

Direct Memory Access(DMA)