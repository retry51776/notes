
# Evaluation

## IMO

- Break evaluation into Self Aware, Known Unknown, Projection Framework.
- People often focus on Adult Experiences, because that's where we have the MOST control over. But in reality often our problems lie on different layer; Ex: Childhood Development, lack understand self & other's Culture, and insight of Human Traits, Subconscious Reaction.
  - Things like care/empathy can exists both conscious & subconscious layer, but this makes huge difference.
- Many Traits has NO flexibility, so many don't bother to study these traits. But self aware & understand these traits help us avoid trigger condition, predict other's trajectory.
- Evolution ~ LLM pretrain ~ "Does this logic/circuit needs to exist"; While RL fine tune  reaction ~ "How does this execute"; In many ways, integrate LLM into product is just detail RL fine tune.
- Check List NEVER cover all aspects, but check list help to find OVERLOOK important aspects, also a good place to store OVERLOOK experiences.

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
  - Traits (Human: obvious, consistent effect)
    - Loss aversion > gain seeking
    - Novelty attraction
    - Face recognition
    - familiarity ~ Trust
    - Causality interpretation
    - Overreact to false alarm
- 2) Culture
  - Medium: Text, Movies, Surrounding
  - Flexibility: medium
  - Timescale: years
  - Traits (obvious, but variance effect, user's background are highly relevant)
    - Priority/Value/Norms (Medium: story/movie/poetry)
    - Social Structure
    - Time Orientation
- 3) Childhood Development
  - Medium: brain
  - Flexibility: dependence
  - Timescale: episode range seconds to weeks
  - Traits
    - Threat calibration
    - Social salience(Trust)
    - Emotional regulation
      - Amplitude
      - Sensitivity (train)
      - Spillover
      - Recovery (train)
    - Perception bias
      - Reality Biases
- 4) Adult Experiences
  - Medium: brain
  - Flexibility: Self determent
  - Timescale: experience range weeks - years
  - Traits
    - Skill/profession
    - Habit Loop
      - mechanism: cue > craving > response > reward
      - Did user knows self good & bad habits
      - Any habit user not self aware?

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
  - Physical Constraints?
- Direction & Momentum
- Current resource & hierarchy