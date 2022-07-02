# Architecture

## CI & CD
1. Source
   1. branch protection
   2. branch strategies
      1. trunk base (commit in main = bad)
      2. features branching (most commom)
      3. fork branching (commmon in opensource)
      4. release branching (water fall or support multi version)
      5. git flow (release branch, requires release manager)
      6. environment branching (both environment branch & release branch)
2. Build
   1. linting
   2. unit test
   3. code coverage
3. Test Environment
   1. integration test
   2. behavior test
4. Production
   1. rollback alarm (auto rollback)
   2. canary or a/b deployment
      1. DNS weight
      2. bake period
   3. deployment pattern
      1. recreate (for SAP, resources w hash, okay w downtime)
      2. rolling update (engine, micro service)
      3. blue green (HA, resources w hash)
      4. canary
      5. a/b
      6. shadow (andriod app, critical engine & service)

response metric:
1. Mean time to detect (MTTD)
2. Mean time to acknowledge (MTTA)
3. Mean time to recovery (MTTR)
4. Mean time to contain (MTTC)
5. System availability
6. Service level agreement (SLA) compliance
7. Mean time between failures (MTBF)

Performance Metrics
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
