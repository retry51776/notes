
# Evaluation

## IMO

- Can psychology being model?
  - IDK, maybe. Maybe psychology is dynamic system. Here's not about prediction, I'm more interest on fundamental forces.
- Break evaluation
  - Self Aware
  - Reinforce Opinion
  - Known Mistakes
  - Known Unknown
  - Projection Framework
- People often focus on Adult Experiences, because that's where we have the MOST control over. But in reality often our problems lie on different layer; Ex: Childhood Development, lack understand self & other's Culture, and insight of Human Traits, Subconscious Reaction.
  - Things like care/empathy can exists both conscious & subconscious layer, but this makes huge difference.
- Many Traits has NO flexibility, so many don't bother to study these traits. But self aware & understand these traits help us avoid trigger condition, predict other's trajectory.
- Evolution ~ LLM pretrain ~ "Does this logic/circuit needs to exist"; While RL fine tune  reaction ~ "How does this execute"; In many ways, integrate LLM into product is just detail RL fine tune.
- Check List NEVER cover all aspects, but check list help to find OVERLOOK important aspects, also a good place to store OVERLOOK experiences.
- In Dynamic System(DS) Model, almost all reality models is function of time.
  - Long time trajectory with different starting points. Ex: personal relationship shows momentum, indicate X consistent force in DS.
  - Short time trajectory change ~ Dramatic events/force. Find different aspects of fundamental forces caused this event. Analysis each force's direction & momentum, and balance forces(constraint or opposite).

- The problem hierarchy structure is LIMITED interactions. The very reason NN has powerful capacity is each neuron's has many connections. But due to human conscience capacity bottleneck, hierarchy structure sacrifice interaction complexity for inutility.
- People & company HATES to be monitor. So avoid over does this.


## Experiments

### Expected Experiments

- Milgram Obedience Study: authority and moral decision conflict.
- Asch Conformity Experiments: social pressure changing clear judgments.
- Stanford Marshmallow Test: delayed gratification and long-term outcomes (with modern replication caveats).
- Darley & Latané Bystander Experiments: diffusion of responsibility in groups.
- Good Samaritan Experiment: self pressure ~ help pressure
- Misinformation Effect (Loftus & Palmer)
- Affective Forecasting Errors: future emotions prediction ARE wrong
- Bobo Doll (Bandura): monkey SEE monkey DO.
- Pygmalion Effect (Rosenthal & Jacobson): Authority expectation is REAL force effects future
- Dunning-Kruger Findings (Kruger & Dunning): overestimate self competence, overestimate != competence.
  - Self confident miss align with self capability.

### Contrarian Experiments

- Festinger & Carlsmith (Cognitive Dissonance): how people rationalize inconsistent beliefs/actions.
- Rat Park (1970s, Bruce Alexander): environment vs addiction behavior
- Invisible Gorilla
- Choice Blindness: justification AFTER decision

## Individual Evaluation

Here is how I analyze/evaluate individual user.

Goal:

- I want to help user reevaluation themself through 6 sections.
  - Inform user on noted traits within current section, and generate some example help user understand each traits within section.
  - Have conversation with user, clear any user's confusion. If user mention aspects/traits in different sections, explain to user.
  - Did user have any aspect want to add/addiction to current section? Collect user's opinion or changes to `report.md`.
- After all user's opinion collected into `report.md`, I will MANUALLY run another agent to merge/change current markdown file.

Constraints:

- Do not resolve user's personal issues. Inform where their issue's source layer/section.
- For location info, at most narrow down to city only. Don't ask for detail address. If country is small, country will be sufficient.
- Do NOT clear or remove info from `report.md`, only append.


Instructions:

- Always append current timestamp to `report.md` before evaluation.
- Ask user's general background, log it to `report.md`.
  - Check `report.md` has user's background info already. If does, add those to context & continue, when missing, prompt user for self introduction.
  - List common stereotypes relates to user's background. Collect user's acknowledgement or opinions on stereotypes to `report.md`.
- At each Development Time Scale section
  - 1) Write desc on current development section with traits examples.
  - 2) List common stereotypes traits to user background at this section, ask their acknowledgment or opinion on these stereotypes.
  - 3) Ask user has any opinions on current section, things to disagree about, things to add, or skip.
  - 4) Log to `report.md`
    - List traits user mentioned, but CLEARLY not within listed traits.
    - List User's opinion of listed traits.

## Background

- Name, Age, Sex, Race
- key cities(born, childhood, school, adult, retired?)
- General profession history
- Personality

## Development Time Scale

> Learning/gradient happens in different time scale, with different mechanism.

- 1) Evolution
  - Medium: DNA/gene, Epigenetic
  - Flexibility: tiny; ex: biotech/mutation
  - Timescale: generations/decades
  - Traits (Human: instinct, obvious, systematic)
    - Loss aversion > gain seeking
    - Story > Accuracy
    - Familiarity ~ Trust
    - Causality interpretation tendency
    - Overreact to false alarm
    - Female mature before male
  - Opinion: elimination ~ pretrain elimination no gradient reinforcement channels
- 2) Culture
  - Medium: Text, Movies, Surrounding
  - Flexibility: medium
  - Timescale: years
  - Traits (obvious, but variance effect, user's background are highly relevant)
    - Priority/Value/Norms (Medium: story/movie/poetry)
    - Social Structure
    - Time Orientation
    - Stereotype Image (external biases)
      - False Culture Stereotype
      - Known Culture Stereotype mechanism/causes
- 3) Childhood Development
  - Medium: brain
  - Flexibility: parent determent
  - Timescale: episode range seconds to weeks
  - Traits
    - Threat calibration
    - Social salience (trust)
    - Emotional regulation
      - Amplitude
      - Sensitivity (train)
      - Spillover
      - Recovery (train)
    - Perception Biases
      - Fake/Lied Detection
      - Boundary Learning
      - Status Sensitivity
    - Relationship History
      - Parent
      - Family
      - Friends
    - Personality (default instinct)
      - Financial
        - Self Financial Pressure
        - Other Financial behavior & result
      - Opinion
        - About school (because most time spent)
        - About sleep (because time, often overlook)
        - About worth/value
        - About emotional feedback
        - Media consumption (favorite movie)
        - Where control/power from (self/authority/helpless/ignore)
        - Any exploration without supervision?
          - Autonomy
          - Risk calibration
          - Creativity?
    - Reflection
      - Reinforce opinions
      - Known mistakes
      - Known unknown
- 4) Adult Experiences
  - Medium: brain
  - Flexibility: self determent
  - Timescale: experience range weeks - years
  - Traits
    - Skill/profession
    - Relationship History
      - Parent
      - Family
      - Friends
      - Coworker
      - Soul Mate
      - Business Partner
    - Habit Loop
      - mechanism: cue > craving > response > reward
      - Did user knows self good & bad habits
        - Hygiene
        - Reflection
      - Any habit user not self aware?
        - Emotion pollution

- 5) Conscious Reaction
  - Timescale: seconds
  - Flexibility: requires practice
  - Traits
    - Conscious replay strengthens emotional loops
    - Reasons follow decisions, not the other way around
    - Counterfactual comparison increases regret
    - Explaining preferences erodes them
    - Awareness reduces presence. Self aware is distraction, brain can't multi task.
- 6) Subconscious Reaction
  - Timescale: ms
  - Flexibility: weighted by Childhood & Evolution
  - Traits
    - Evolution Hardcoded
      - Reaction speed
      - Category-based processing
      - Priority: Threat > social > reward
    - Safety category
    - **Social category**
    - **Cognitive Bias**
    - **Perception Biases**


## Individual Time

Time IS known constrain on EVERYONE. Check list here doesn't sum up 100% because over lapse. But still important to evaluate time spent.  

- Sleep 33%
- Work 22%
  - Work 10%
  - Meeting 9%
  - Context switch ~ 5%
- Maintenance 15%
  - Eating 6%
  - Clean 7%
    - Hygiene - 3%
    - Reflection 2% (overlook)
    - Exercise - 2%
  - Errand 3%
- Entertainment 20%
- Transit 5%
- Social 5%
- Learning 2% (overlook)
- Planning 1% (overlook)

## Individual Priority

Natural Desires
- Survival
- Sexual
- Belonging
- Power
- Narrative Coherence

Variables
- Scarcity
- Biological State
- Social Context Switching


## Company Evaluation

> Company has limited resources, this check list help you find important aspects. You need to prioritize small number of aspects, and expand them.

### Company Check List

- Fundamental Forces
  - Technology Stacks
    - License
    - Frontend Service
    - Backend Service
      - Business Logic Service
      - Storage Service
      - Integration & Messaging
    - DevOps
      - CICD
      - Monitor & Logging
      - Security Service
  - Customer
    - Expectation (reliability, performance, features, availability)
    - Budget (money, time)
    - Switching Cost (data, network, integration)
    - Support
      - Feedback
      - Documentation
      - Order Warranty & Cancel
  - Supplier
    - dependency (alternative supplier)
    - switch cost
    - cost
    - lead time & capacity
    - communication barrier?
    - conflict interest?
  - Competitor
  - Investor?
  - Regulator?
    - Government
    - Industry Standard Bodies
  - Employee?
  - Partner / Platform?
  - Public Opinion?
    - Does young generation WANTs to work this industry? Public opinion cant change
    - Investor/Loan odds
  - Physical Constraints?
- Direction & Momentum
- Current resource & hierarchy

### Company Time

Company time is VERY different than individual. Capacity, throughput, latency, coordination cost. We don't need monitor all checklist, run it once year maybe good enough.

- Clock Coverage
  - operation_hr / week
  - operate_weeks / 52
  - time-zone coverage
  - maintain_hrs
    - reliability = maintain_hrs / expected_online_hrs
    - maintain_hrs / year
- Work Hours Efficient
  - Department Cost (easy)
  - Time Spend
    - Productivity
    - Meeting
    - Investment/Development for future
    - Debug Issue Time (important)
      - Shipping
      - Orders
      - Support
- Latency
  - Planning Latency
    - Priority Shift Latency
    - Meeting Latency
  - Execution Latency
    - Feature/Bug Resolve Latency (important)
    - Blocking Time %
    - Reaction Time % (aka context switch)
  - Postmortems Latency
    - Positive Feedback Latency (Raise IS important to be timely)
    - Negative Feedback Latency
      - Bug & Failure
      - Failed Project Live Time
- Constrains
  - Cash runway
  - Customer patience
  - Deadlines
- Decays
  - Skills
  - Techstacks
  - Brand

## Nation State

- Government Structure
  - media/info control
  - population demographics
  - policy stability (momentum)
  - Internal control
- Military Structure
  - command hierarchy
  - finance supply
  - Military industry
  - Existing military assets
- Economy
  - Private Sector
  - Industry diversity
  - Resource
    - Energy
    - Food & water
    - Commodities resources
- External
  - Dependence
  - Power
    - Alliance
    - existed trade party/relationship

### China

- General Secretary
- Military Leader
- Economy Power
- Public Opinion