# Architecture

## CI/CT/CD
1. Source
   1. linting
   2. branch protection
   3. branch strategies
      1. trunk base (commit in main = bad)
      2. features branching (most commom)
      3. fork branching (commmon in opensource)
      4. release branching (water fall or support multi version)
      5. git flow (release branch, requires release manager)
      6. environment branching (both environment branch & release branch)
2. Build
   1. unit test
      1. code coverage
   2. build image (multi stage if needs compile)
   3. publish image/package w alpha tag
   4. trigger message(image_name/package_name & version, relatives tests) to test engine
3. Test Engine
   1. rebuild & run relative engine & service (k8 deployment update? or singlr box envirement?)
   2. integration, behavior, UI tests
      1. Selenium
      2. IDK, build python scripts?
   3. publish image/package w version
4. Develop Environment
   1. create release branch
   2. QA team? bug fix commit?
   3. merge master & develop
5. Production Environment
   1. rollback alarm (auto rollback)
   2. canary or a/b deployment
      1. DNS weight
      2. bake period
   3. deployment patterns
      1. recreate (for SAP, resources w hash, okay w downtime)
      2. rolling update (engine, micro service)
      3. blue green (HA, resources w hash)
      4. canary
      5. a/b
      6. shadow (andriod app, critical engine & service)
6. Monitor
    1. sentry.io (capture runtime error)
    2. Opsgenie (monitor & alert)
    3. zabbix (metrixs)
    4. grafana (logs)
7. Support
   1. Service Now or Zenddesk


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

Monitor Tools:
zabix
garfanar
opsgeny
sentry.io



# Buzzwords
Access Patter
   - Random
   - Sequential
Direct Memory Access(DMA)