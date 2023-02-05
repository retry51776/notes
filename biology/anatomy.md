# Anatomy
> Study of human body。
> 
> > The problem is that the human body often performs multiple functions, which cannot be easily organized into distinct systems.

Key Systems
- [Phycology](../psychlogy/psychology.md) `aka how brain works`
- [Circulatory System](#circulatory-system)
  - Respiratory System
  - [Lymphatic System](#lymphatic-system)
- [Digestive System](#digest-system)
- Muscular System
  - Reproductive System


## Analogy
> Just distinct biology features reminds me programming terms;

> Human have about 200 distinct cell types;

> Aging is NOT because DNA corruption, rather DNA corruption trigger repairing DNA have strong side effect to DNA packing;
> > DNA is cookbook; Ribosome is reader; Histones & chromatin fiber & other Cell Molecules are bookmarks; Damage is not cookbook text, nor reader; Rather bookmarks on cookbook may moved to wrong spot;

- Genome
  - DNA `Blueprint; Not reservable change; aka Source Code;`
    - Chromosome `Thread like structures; Human 46 set`
      - Gene `section of DNA create protein; aka Class or Function;`
- Epigenomes `beyond genetic; Reservable change; aka CICD;`
  - Transcription `DNA to RNA; aka CI;`
    - RNA `.pyc file, Compiled Python Code;`
    - chromatin fiber `Chain Histones/chromatin together`
    - Histones `The protein DNA wrapped around; control accessability of gene; aka archive source code;`
      - concentration of Cell Molecules `Environment Variable`
      - Molecules wrap around DNA `packing logic`
 - Translation `RNA to Protein; aka CD;`
    - Ribosome `Python Run Time; read 3 RNA code to 1 amino acids;`
    - Protein `Molecules made from 20 amino acids`
    - Enzymes `Helper Method`
- Cell `Class`
- hormone `Redux Action Event`
- hormone receptors `Redux Event Reducer`

- Regulatory Gene `webpack`

# Nervous System
## Central Nervous System (CNS)
  - Brain
  - [Spinal Cord](#reptilian-brain)
## Peripheral Nervous System (PNS)
  - Somatic Nervous System `voluntary`
  - Autonomic Nervous System `involuntary`
    - Sympathetic Nervous System `Arousing;紧张;`
      - spin core -> preganglionic cell -> ganglion -> postganglionic cell -> organ
    - Parasympathetic Nervous System `Calming;放松;near organ;12 cranial nerves`
      - Olefactory Nerve `nose; sense`
      - Optic Nerve `eye; sense`
      - Oculomotor Nerve `eye muscle; motor`
      - Trochlear Nerve `eye muscle; motor`
      - Trigeminal Nerve `jaw muscle; both`
      - Abducens `eye muscle; motor`
      - Facial Nerve `facial expression; both`
      - Auditory Nerve `sound; sense`
      - Glossopharyngeal Nerve `tongue; both`
      - Vagus Nerve `heart, digest; both`
      - Spinal Accessory Nerve `head & shoulder; motor`
      - Hypoglossal Nerve `talk; motor`

# Circulatory System
main components:
- Heart
- Blood vessels `which include your arteries, veins and capillaries`
- Blood `made up of red and white blood cells, plasma and platelets`


# Endocrine System
> Endocrine System `内分泌系统` controls attraction, appetite, aggression;
>
> Gland produce Hormones; Hormones travel though bloodstream, then bind to hormone receptor to enter cell. 

## Glands
Functions includes:
- moods
- arousal
- circadian rhythm
- metabolism
- immune system
- signal growth
- reproduction

Organs:
- pineal gland / 松果腺
- hypothalamus / 下丘脑 `control pituitary gland`
- pituitary gland / 脑下垂体 `control rest glands`
- thyroid gland / 甲状腺 `metabolism`
- parathyroid gland / 甲状旁腺 `calcium`
- thymus / 胸腺
- adrenal gland / 肾上腺 `flight or fight`
- pancreas / 胰腺 `sugar level`
- gonads / 性腺 `sex`

- pancreas / 胰腺 produce 
   * insulin/ 胰岛素 speeds up rate cell store glucose
    > https://public.tableau.com/app/profile/marty.kendall7139/viz/foodinsulinindexanalysis/FIIallfoods?publish=yes
   * glucacon / 胰高血糖素 break down fat into glucose

> HPA axis = hypothalamus -> pituitary  -> adrenal

> HPT axis = hypothalamus -> pituitary  -> thyroid

## Hormones
> produces by gland; `I think of hormones are massagers;`
- GABA - stop electric signal pass between neuron; opposite to Dopamine
- Dopamine(多巴胺) - active agent, lack will cause shaking
- Serotonin(血清素) - Happy, memory
- Prolactin(泌乳素) - Produce milk
- Luteinizing Hormones (黄体化激素) - Ovaries
- Follicle Stimulating Hormones (卵泡刺激素) - pubertal development
- Oxytocin() - Love
- Melatonin - Clock, Sleep
- Endorphins - Pain killer
- Adrenaline - fight or flight
- Norepinephrine - redirect blood in dangerous

> Both Neutotransmitter and hormones effects neuron, sometime even same compound.
> > I think of both Neutotransmitter and hormones are message broker system`rabbitmq` in programming, each organ has it own consumer`receptor` listen to message and will response according its consumer; hormones is fanout exchange, deliver through blood; while neutotransmitter is topic exchange deliver to specific organ
**Neutotransmitter** `ferry signal to another neuron; most neuron works with single type Neutotransmitter`
- Acetylcholine (ACH)
- Gamma aminobutyric acid (GABA) `30% neuron, suppress`
- Norepinephrine `suppress; excite heart for alertness`
- Dopamine `suppress;`


# Lymphatic System
`淋巴系統`
Lymphatic vessels pumps 15% fluid back into blood stream;

> Most other protein, sugar, waste just in travel capillaries `aka walk on road`;
> 
> Then travel through capillaries cell `aka walk off road` to organ;
> >Red blood cell `aka truck` carry **oxygen** in capillaries `aka road`;


Lymphatic components:
- lymphatic vessels 淋巴管
- tonsils 扁桃体
- adenoids 腺样体
- thymus 胸腺
- spleen 脾

Immunity components:
- phagocytes 吞噬細胞 is group defense cells
  - neutrophils 中性粒细胞/最常见白细胞，死后就是pus/脓液
  - macrophage 巨噬細胞 will dissemble target, and have target protein on its surface// Major Histocompatibility Complex (Similar to checksum)
  - natural killer cell 自然殺手細胞
  - leukocytosis 白细胞

- mast cell 肥大细胞 start inflammation by produce 发热激活物（pyrogenic activator）
- Histamine 组织胺 protein that causes inflammation, one of 发热激活物


- Antibody 抗体/抗生素 is a protein that bonds to the target cell.
  - Penicillin 青霉素 and Cephalosporin 头孢菌素stop bacteria build the cell wall
  - Tetracycline 四环素 and Chloramphenicol/ 氯霉素 stop bacteria produce food
  - Rifampin 利福平 is bacteria stop duplicate DNA

> B Lymphocyte 淋巴细胞 is the killer cell that has thousands antibody on its surface. It runs around the bloodstream to detect an intruder. Then multiply itself with the only antibody that bonds to the intruder.
B Cell antibody is generated randomly, so its antibody must be confirmed with T cell before mass production.

- Thyus Lymphocyte 淋巴细胞 breaks into
  - Helper T Cell is controller cell, activity Cytotoxic T Cell, training B Cell
  - Cytotoxic T Cell is a killer cell

Check & balance of B & T Lymphicyte is important

# Digest System
> Digest System break food into 3 types:
- Fat
- Protein
- Carbohydrate
  - fructose directly defuses in blood & uses by cells.
  - glucose and alcohol process by same way.


# Maintenance
- Heartflow Test `aka put color dye into blood, then ct scan how blood flow in heart`
- Chanca Piedra Kidney Stone Breaker
- 