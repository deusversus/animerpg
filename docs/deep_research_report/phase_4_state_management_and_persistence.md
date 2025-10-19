State Management & Persistence Analysis

Overview: AIDM v2 employs a robust state management system anchored by Module 03: State Manager

and a suite of JSON schemas. Game state is partitioned into five synchronized components:  Character,

World,  NPCs,  Memory, and  Narrative Profile

1

. Module 03 acts as the single source of truth for these

data stores and oversees save/load operations, ensuring consistency and integrity across sessions.

Schema Coverage & Completeness

The  eight   JSON   schemas
cover   most   aspects   of   game   state.   Key   schemas   include
character_schema.json   (PC   data),   world_state_schema.json   (world   data),   npc_schema.json

and
(each
narrative_profile_schema.json   (active   narrative   DNA).  All   critical   domains   are   represented  –

  memory_thread_schema.json

(memory

system),

NPC),

character   resources,   stats,   inventory,   skills,   and   even   the   active   narrative   profile   are   stored   under   the

character schema

1

, world conditions and factions under world state

1

, etc. Notably, AIDM does not

have standalone “quest” or “faction” schema files; instead, these are integrated into existing structures. The

character schema contains an embedded  quest log  for active/completed/failed quests

2

3

  and tracks

faction reputations in the character’s world context

4

. This means quest progress and faction standing

are   captured,   albeit  without   dedicated   modules  for   complex   logic.   Similarly,  economy  and  calendar
systems   are   present   within   world_state_schema.json   (e.g.   temporal   date/season   and   economy

markets) rather than separate schemas. Overall, the schema coverage is comprehensive, and  no major

state  variable  is  entirely  untracked.  However,  the  decision  to  integrate  quests  and  faction  rep  within

character   state   (versus   a   dedicated   quest/faction   schema)   could   limit   scalability   for   campaigns   with

numerous   global   quests   or   multi-party   faction   dynamics.   A   structured   quest   schema   (with   branching

objectives, dependencies, rewards) is absent, so complex questlines rely on the simpler list-of-objectives in

character state and memory threads. This is adequate for linear progression, but richer quest modeling (fail

conditions, parallel quests) may strain the current design. In summary,  all fundamental game elements

are accounted for, but some are managed in-line rather than via standalone schemas, which may warrant

future refactoring for clarity.

Save/Load Robustness

Session persistence appears to be a strong point. The  session_export_schema.json  defines a holistic

save file format that includes character, world, all NPCs, memory threads, recent narrative context, and
.  All encountered NPCs are saved in full (as an array of   npc_schema  objects)

system metadata

5

6

7

, and the memory system is serialized with its hierarchical threads (core, character_state, relationships,

quests,   world_events,   consequences)
narrative profile and loaded modules/libraries at the time of save, under a  system_state  section

.   Crucially,   the   export   schema   also   captures   the  active

10

9

8

11

. This means the save file remembers which instruction files and trope/profile libraries were in use, as

well as the narrative genre DNA – ensuring that on load, the same storytelling parameters can be restored.

The state manager’s design calls for validating and restoring all components on import: it verifies schema

version, data integrity (via a checksum), and cross-links (e.g. NPC IDs referenced in memory threads) before

resuming   play

12

13

.  Export   frequency  is   handled   gracefully   (auto-saves   every   30–60   minutes   or   at

session end)

14

  and backups are kept. In theory, a saved JSON can be copied and later fed back to the

1

system   to   reconstruct   the   exact   game   state.   This   comprehensive   approach   minimizes   data   loss   –  full

continuity   is   preserved   across   sessions,   from   resource   values   down   to   “last   active   scene”   dialog   for

context

15

16

. One potential weakness is the reliance on the LLM to reload libraries: while the export lists

which files were loaded, the actual  re-loading  must occur during the import process (the system should

fetch those narrative profile/trope files again). The design anticipates this by logging file paths

10

, but it

requires the DM or system prompt to trigger those loads. As long as the import procedure in Module 03 is

followed (loading needed files and then applying the JSON state), the save/load system is robust and one

of AIDM’s strengths. All evidence indicates that if a campaign is saved mid-stream, it can be resumed later

without desynchronization of character stats, world status, or story context.

Version Compatibility & Schema Evolution

AIDM includes a version field ( export_version ) in the session export to allow for compatibility checks

17

. This suggests an awareness of future schema evolution. However, handling of breaking changes is not

deeply   documented.   There   is   no   explicit   migration   tool   or   backward-compatibility   layer   beyond   a
compatibility_notes  field in the export for human-readable warnings

. If the schemas change (e.g.

18

adding a 12th narrative scale or new fields), old save files might not validate without manual updates. The

development   team   appears   to   mitigate   this   by   striving   for  100%   information   parity   in   optimizations

(recent index compressions didn’t drop data) and by only appending new fields rather than removing. For

example,   when  Scale   11   (POV   Distribution)  was   added   to   narrative   profiles   in   early   2025,   they   likely
updated   narrative_profile_schema.json   and   incremented   the   version.   The   presence   of
export_version  means the system can detect a version mismatch and could adjust accordingly. But no

automated migration scripts are described – the onus is on maintainers to ensure new versions can read

old data. On state load, Module 03 does perform checks: it validates that required fields exist and could use
aidm_version  in the session metadata to decide if any conversion is needed

. In practice, given the

19

system is in active beta, changes are probably coordinated with campaigns (e.g. GMs updating profiles

manually). The design is sound for now, but as AIDM evolves, a more formal migration strategy or backward

compatibility layer (perhaps a conversion of old exports to new format) would be prudent.  In summary,

versioning is acknowledged (exports are tagged with version and system version), but  robust handling of

schema   changes  is   an   area   for   improvement.   A   positive   sign   is   that   the   state   export   includes   a
compatibility_notes   field to flag any known issues when loading an older save

, which at least

18

provides transparency to the user if something might not load perfectly.

State Consistency & Synchronization

The architecture enforces  strict consistency rules  across state components. Module 03 explicitly defines

“Single Source of Truth” – each type of data has one canonical location (e.g. PC HP in character_schema,

not duplicated elsewhere; world time in world_state)

20

. This prevents divergence between modules. It also

mandates  validation   before   any   update:   every   state   change   is   checked   against   logical   and   schema

constraints  prior  to applying

20

. For example, if a skill upgrade is proposed, the system validates XP and

level   bounds   before   committing   changes,   ensuring   no   illegal   values   enter   the   state

21

.   Another

cornerstone is atomic updates: state changes apply all-or-nothing

22

. Module 03’s protocol wraps multi-

step updates (like resolving combat damage, XP gain, level-ups, etc.) in a transaction – if any sub-step fails

(e.g. not enough MP to cast a spell), it will roll back the entire sequence

22

. This prevents partial state

application   that   could   corrupt   data   (no   subtracting   an   item   without   also   applying   its   effects,   etc.).   In

practice, atomicity is feasible because AIDM’s turn-based flow means only one operation happens at a time

(no concurrent writes). The system  sequencing (Module 01 classifies intent → Module 03 verifies state →

2

Module 08 resolves combat → Module 03 updates state) ensures a controlled update pipeline
is   little   risk   of   race   conditions   in   a   single-threaded   LLM   environment.   Additionally,  cross-module

. There

24

23

integration is carefully defined for state changes: e.g. if Module 08 (Combat) reduces an NPC’s HP to 0, it
triggers Module 03 to mark that NPC’s   status   as dead in npc_schema and logs a world_event memory

25

26

.   The   consistency   is   further   maintained   by  redundant   validation   checkpoints  –   e.g.   a   state

validation runs before/after combat, before saves, on quest completion, etc., to catch any anomalies

27

28

.   In   summary,   the   design   addresses   state   synchronization   thoroughly.   Every   key   data   update   flows

through the State Manager, and the rules (single source, pre-validate, atomic commit) minimize the chance

of divergence or corruption. This is a notable strength of AIDM v2’s architecture – it treats game state with

the rigor of a database, which is critical for a persistent multi-session campaign.

Memory Management & Persistence

Module   02:   Learning   Engine  governs   the   memory   subsystem,   which   is   tightly   coupled   with   state

persistence. The memory is structured into thematic threads (Core, Character_State, Relationships, Quests,

World_Events,   Consequences,   plus   a   Narrative_Style   category)

29

30

.   Each   memory   thread   has   a  heat

index indicating its importance, which decays or boosts based on recency and usage. The system actively

compresses older, low-heat memories to prevent context bloat. For example, completed quests or long-

resolved   story   arcs   are   summarized   after   a   certain   threshold   (e.g.  5+   sessions   after   completion)

31

32

.

Module 02 provides clear compression triggers: when a category exceeds ~100 threads, or a memory is older

than X sessions with heat <20, or on explicit command, compression will occur

33

. The compression algorithm

groups   related   threads   and   replaces   them   with   a   condensed   summary,   linking   back   to   originals   for

reference

34

. Importantly, not all memories are compressible – the system never compresses core lore,

player-established facts, or plot-critical events

35

. It also avoids compressing anything from the last 3

sessions to prevent premature loss of detail

35

. This approach should maintain long-term recall of critical

information while pruning trivial details (no more LLM forgetting a big plot reveal, because it’s either core or

marked plot-critical and thus immune from deletion). Over a 50+ session campaign, this memory policy will

be stress-tested. The design seems sound: by categorizing and decaying memory, it prevents the “growing

context” problem  that could overwhelm the token budget. There is some risk of  information loss  if the

compression   or   heat   assignment   fails   (e.g.   if   an   important   clue   wasn’t   flagged   as   plot-critical   and   got

summarized   away).   The   developers   attempted   to   mitigate   that   by   rules   and   even   giving   players   a   say

(“Remember this” creates a high-heat permanent memory)

36

37

. In practice, there could still be  edge

cases – for instance, a subtle detail from 20 sessions ago that wasn’t marked important might not be vividly

remembered. However, the memory threads system is quite advanced for an AI GM: it has explicit support

for  player feedback memories  (so the AI remembers if the player said “tone it down”)

38

  and  hidden

knowledge flags (for info the NPCs know but the player doesn’t)

37

. Persistently, memory threads are also

saved in the session export (with each thread’s content, timestamps, and heat)

8

39

. This means even the

“history of what happened” is part of the save state, not just the resulting world state. That’s critical for

resuming long campaigns – the AI can reload and recall past events accurately, not relying purely on world

state snapshots.  Bottom line:  AIDM’s memory management is a highlight – it systematically prunes and

preserves   narrative   history   to   balance  continuity   vs.   context   limits.   After   dozens   of   sessions,   minor

amnesia might still happen if heat tuning is off, but the framework to minimize that is in place (prioritize

recent & significant memories, compress the rest). As long as the heat index calibration is reasonable and

the DM occasionally curates the memory (via meta-commands if needed), the system should avoid both

forgetfulness and runaway context growth.

3

NPC State Persistence

Non-player   characters   are   first-class   citizens   in   the   state   model.   Each   NPC’s   full   profile   is   stored   via
npc_schema.json  and included in saves (all NPCs encountered or important are saved in an array)

.

7

The  NPC  schema  is  extremely   detailed  –   it   captures   identity   (name,  age,   race,  etc.),  personality   traits,

values, fears, goals, backstory and secrets,  inventory  of items, current status (location, activity, schedule,

mood),   relationships   (to   the   player,   to   factions,   to   other   NPCs),   and   narrative   role   (purpose   in   story,

.   This   means   NPC   persistence   covers   not   only   raw   stats   but   also   their
associated   quest   IDs)
knowledge and motivations. Notably, NPC state includes a   knowledge  section and a list of   secrets

41

40

with who knows them

42

43

 – effectively modeling NPC knowledge boundaries. The system can leverage

this so that an NPC does not reveal information they shouldn’t know (by checking if the player’s question is

outside   the   NPC’s   known_topics   or   if   a   secret   isn’t   flagged   as   discovered).   Also,   NPCs   have
faction_affiliations   with
  which   combined   with   the   character’s
faction_reputations   can  help  determine  how  an  NPC  reacts  based  on  global  faction  standing.  All

loyalty   ratings

44

,

these aspects persist across sessions – if an NPC’s affinity to the player changed or they moved to a new

location, those fields are updated in the state and will be serialized. The state manager ensures updates like
NPC location or affinity are atomic and validated (e.g. an NPC can’t be in two places at once; schedule logic

is consistent)
. The only potential gap is ensuring the AI actually uses these fields correctly during
play (which is more of a functional integration issue than persistence). For example, the NPC’s  inventory

45

46

exists in the schema

40

, but does Module 04 (NPC Intelligence) actively reference it when the player tries to

trade or steal? This is something to verify in integration (the data is there, but must be utilized). Another

subtle area is NPC knowledge enforcement: the data model supports it (NPC secrets, known topics, and

), but the cognitive engine or NPC module must consistently
hidden memory threads for undisclosed info
check those before spouting knowledge. Assuming those integrations are in place (the design suggests

37

they   intended   it),   NPC   persistence   is   very   solid.   The   system   even   allows   for  NPC   evolution  –
aidm_directives  can mark if an NPC’s personality can change over time and what triggers might do so
. Any such changes (an NPC’s goals shifting, or a flag like  can_die  which indicates if they can be

48

47

killed

49

) are all part of the persistent state. In conclusion,  NPC state tracking is comprehensive and

persistent. There were concerns that some things might be missing (e.g. earlier documentation asks if NPC

inventories   or   quest   involvements   are   tracked),   but   those   are   indeed   present

40

41

.   Once   an   NPC   is

introduced, their entire state history is saved – making long-term character development and recall feasible.

The only weaknesses are  utilization  (ensuring the GM logic uses all this rich data) and possibly  volume: if

100+ NPCs are active, saving all of them could bloat the export (but given JSON, that’s manageable and

necessary for fidelity).

World State Evolution & Propagation

The  world   state  is   captured   in   world_state_schema.json   and   through   memory   threads   for   world

events.   This   includes   time   (current   date/time   of   day,   season)

50

51

,   environment   conditions   (weather,

disasters)

52

53

,  factions  (with power levels, territory, goals)

54

55

, known locations (with details like

population, controlling faction, danger level)

56

57

, economy (currency and market conditions)

58

59

,

and   narrative   state   (story   arcs,   active   plot   threads,   world-changing   events)

60

61

.   This   indicates   the

system can record major changes to the world: e.g. if a city is destroyed, the GM could update that location’s

entry   (population=0,   maybe   change   type   to   ruin   or   add   a   world   event   entry).   Indeed,   there   is   a
world_changing_events   list   for   permanent   alterations

,   and  memory   threads  categorized   as

60

World_Events and Consequences to log these incidents and their ripple effects

62

63

. The key is whether

changes in one part propagate logically elsewhere. The design calls for  dependencies update  on state

4

change – e.g. if the player destroys a city, Module 03 would update the location’s data and also likely create

a world_event memory and possibly adjust faction power if that city belonged to a faction. The schema has

fields to support this (each world_event memory can note involved factions and consequences of the event)

62

64

. NPCs related to that city or faction might have their status or affinity changed as a result – which

would rely on the DM or a game rule to enact. There isn’t an automatic propagation engine described (like

“city destroyed → all NPCs in city flagged dead”), but given the LLM’s role, the expectation is that the GM (AI)
will  narratively  carry these changes through. The state model provides the places to record the outcome

(city marked destroyed, NPCs can be individually marked dead or moved). Because the world state and

memory are persisted, the world can evolve over time and those changes persist – time can advance (in-

world days recorded), seasons change, factions rise/fall, etc., and nothing will be lost between sessions. A

possible   shortcoming   is   the   lack   of   a  time   advancement   system  beyond   a   simple   current   date.   If   a

campaign spans years in-game, the system must manually adjust the date and aging. There’s no aging

mechanic explicitly, but since character and NPC ages are fields, the DM could update them. Also, while

world_state   tracks  special   events  (festivals,   disasters)   as   upcoming   events

65

,   it   doesn’t   enforce   their

occurrence – that’s up to the narrative. This is acceptable given AIDM’s focus (the AI drives the narrative).

Overall, the  persistence of world changes is well-supported. The combination of structured world data
and memory logs of events ensures that if the players topple an empire in session 10, by session 50 the

world_state will reflect the new regime (faction changes, etc.) and memory threads will preserve the story of

that upheaval. The state manager’s rule of never letting irreversible events fully decay

25

 means significant

world changes stay in memory (just summarized) and won’t be forgotten. In summary, world persistence is

comprehensive, with only minor gaps in automation. The data is all there; it’s on the scenario logic to update

it when needed. There is an implicit expectation that the AI will update world_state_schema consistently

as events happen – which is a heavy but necessary responsibility for Module 05 (Narrative Systems) or

Module 03. Given the meticulous design, it’s likely they attempted to script such updates (e.g. Module 05

might say “if event X happens, update world_state Y”). The risk of forgetting to update a field (like forgetting

to mark an NPC as dead) exists, but the State Validation process would catch inconsistencies (an NPC with

HP=0 but status not dead would violate a validation rule)

66

. Thus, any propagation oversight might trigger

a validation prompt to the GM to reconcile it. This is a smart safety net for maintaining world consistency.

Quest Tracking Mechanisms

Quest   state   is   managed   through   a   combination   of   the   character   schema   and   memory   threads.   The
Character’s quest log ( character_schema.quests ) maintains structured info on active quests including

objectives and status

2

. For each active quest, it can list objectives (with completion flags or progress

counts) and a status flag (active, in_progress, ready_to_complete)

67

68

. Completed quest IDs are stored

in a separate list, as are failed quests (with reasons for failure)

3

. This provides a clear, persistent record of

what quests the party is working on and their outcomes, which persists across sessions. In addition, the

memory threads have a category for Quests that logs the narrative progression of quests – key events and

moments in each quest line

39

69

. For example, when the party accepts a quest, a memory thread is

created; when they hit a milestone or complete it, events are appended to that thread. These threads have a
heat_index   so   active   quests   stay   “hot”   (high   priority)   while   completed   ones   cool   off   and   eventually

compress

31

32

.   The   dual   approach   means   there’s   both   a  mechanical   log  (in   character   state)   and   a

narrative log (in memory) for quests. What’s missing is a dedicated Quest module or schema to handle

complex   branching   logic.   As   is,   the   quest   objectives   in   character_schema   are   basically   an   array   of

objectives   with   optional   progress   counters

70

,   but   no   explicit   support   for   branching   paths,   mutually

exclusive   outcomes,   or   parent-child   quest   relationships.   Quests   are   likely   treated   in   a   straightforward

manner:   each   quest   has   an   ID   and   description,   and   the   DM   logic   must   manage   any   complexity   (like

5

updating   an   objective   or   marking   a   quest   failed   if   a   condition   happens).   The   state   manager’s   rules   do

mention checking “quest logic” at validation points

71

, implying the system will at least verify that quest

status   transitions   make   sense   (e.g.   you   shouldn’t   mark   a   quest   as   completed   if   an   objective   is   still

incomplete).   There’s   also   mention   in   design   discussions   of   adding   a   quest   schema   (the   prompt   itself
suspects a missing   quest_schema.json ), but the integration into existing schemas might have been

deemed sufficient. For campaigns with lots of side-quests and dependencies, the lack of a formal quest

manager   could   become   unwieldy   –   the   DM   has   to   manually   toggle   statuses   and   perhaps   use   the

Consequences  memory category to simulate impact of failed quests on the world
each NPC has an  associated_quests  list

 so the system knows which quests involve which NPC. This

63

. On the plus side,

41

can be used to dynamically update NPC behavior or availability when a quest state changes (e.g. if an NPC

was a quest giver, once the quest is done, that NPC’s purpose might shift). These associations are persistent

and ensure NPCs are contextually aware of relevant quests even after saving and loading.  In conclusion,

quest tracking is present and persistent, but somewhat basic in structure. It covers the essentials (which

quests are active, what the objectives are, which are done/failed) and preserves the narrative context of

quests via memories. The absence of a standalone quest schema isn’t a show-stopper given the alternative

implementations, but it is an area ripe for enhancement. A future Quest System module could introduce
quest   templates,   conditions,   and   better   automation.   As   it   stands,   AIDM   v2’s   quests   rely   on   the   GM’s

narrative management with the state model simply recording the outcomes. The persistence aspect is fine –

you won’t lose track of quests between sessions – but the functionality to manage them could be richer.

Narrative Profile Persistence

A defining feature of AIDM v2 is the  Narrative Profile  that calibrates the genre and tone. Ensuring this

profile’s state persists across sessions is crucial for continuity of storytelling style. The system handles this in

two   ways:   (1)   The   active   profile   (or   blend   of   profiles)   is   stored   within   the   character’s   state   under   a
narrative_profile   section

, and (2) the session export includes an explicit copy of the narrative

1

profile   data   in   both   the   character   and   system_state   sections

72

11

.  Pre-made   profiles   vs   Generated

profiles  are treated differently to optimize storage. For a pre-made profile (one of the 21 built-in anime

profiles), the state keeps a lightweight reference – just an ID and any deviations the player made

73

. The

logic is that the base data can always be reloaded from the library file on a new session, so no need to

duplicate all that text in the save. By contrast, a generated or custom profile (e.g. if the player asks for an

obscure anime or a blend of profiles) has no external reference, so the entire profile data (all 11 scale values,

trope  toggles,  mechanical  scaffolding  settings,  etc.)  must  be  saved  in  state

74

.  Module  03’s  narrative

profile tracking explicitly notes that generated profiles require full persistence to avoid loss

75

. On loading a

game, Module 03 will check the profile type: if it’s pre-made, it will re-link to the library file (ensuring any

library updates are applied) and then apply the stored player adjustments on top

76

. If it’s generated, it

validates that the state has everything and uses it directly (since no file exists)

77

. This design is clever: it

reduces save file size for common cases but still guarantees fidelity for custom cases. It also handles the

scenario of a missing profile file – if a pre-made profile file somehow isn’t available on load (perhaps the file

was moved or the GM is offline), the system plans to  warn and offer fallbacks  (like suggesting a similar

profile   or   converting   the   last   known   data   into   a   generated   profile)
system_state.active_narrative_profile  is basically a snapshot of the current storytelling DNA

.   The   session   export’s

11

,

78

which is redundant to what’s in character_schema but provides quick access. This redundancy is intentional

for reliability. The  persistence of narrative calibration means a campaign’s tone remains consistent

even if you pause for weeks – when you resume, the AI knows you were, for example, running a dark and

gritty Attack on Titan style (and doesn’t suddenly become lighthearted). The only caveat is if the underlying

profile definitions update between sessions. For pre-made profiles, loading always pulls fresh from file

79

,

6

so if v2.1 tweaks (say, Naruto’s scales), a resumed campaign might subtly shift unless the adjustments_log

counteracts it. This is presumably minor, but noteworthy. Blended profiles (using 2–3 sources) currently are

likely   treated   as  “generated”  (the   blend   result   becomes   a   custom   profile   in   state).   The   state   doesn’t

explicitly   store   multiple   profile   IDs   and   weights   –   it   would   store   the   blended   outcome   as   a   single

narrative_profile structure. This works, though it means you can’t easily separate the components after the

fact   (not   that   you’d   need   to).   In   summary,  the   narrative   profile   persistence   is   well-addressed.   The

combination of storing either an ID or full profile data, plus an adjustments log of any mid-campaign tone

changes

80

76

, ensures the storytelling parameters remain intact. This is a relatively novel requirement

(most systems only care about numeric state, not stylistic state), and AIDM handles it elegantly. The only

improvement could be an explicit  profile version  check – if narrative_profile_schema expands (e.g. a new

scale is added), how do old profiles handle it? One would assume missing fields default to neutral values

(e.g. new scale default 5). The state manager does validate that all expected scales/toggles are present

77

,

so a missing field would throw an error on load. This scenario hasn’t occurred yet beyond POV Distribution

addition (which presumably was handled by adding a default for old profiles). As a mitigation, the import

procedure could auto-set new fields to default and maybe note it in compatibility_notes. But these are edge

considerations. Practically,  once a narrative profile is set in your campaign, it will follow your save
games reliably – preserving the unique anime flavor you chose from session to session.

Loaded Libraries & Continuity

An often overlooked aspect of persistence is tracking which  auxiliary content  was in use. AIDM’s lazy-

loading  means  at  any  given  time,  a  subset  of  the  180K  token  library  is  loaded  (e.g.  the  specific  anime

profiles,   trope   lists,   or   power   system   docs   relevant   to   the   campaign).   The   session   export’s
system_state.loaded_libraries   field directly addresses this by listing all library files that had been

pulled   in

10

.   This   is   important   for   two   reasons:   (1)   Debugging/resuming   –   if   you   reload   a   game   and

something feels off, you can see if perhaps a library failed to load, because it’s listed in the save but not

present in memory. (2) Mid-campaign  module swaps  – if during play the GM dynamically loaded a new

trope   file   or   switched   profiles,   those   appear   in   the   record,   aiding   continuity.   There’s   also
loaded_instruction_files  which logs which core modules were active

, though typically all Tier 1

81

and necessary Tier 2 modules would be loaded in any running game. In effect, the system state capture

ensures  no   piece   of   context   is   forgotten.   On   resume,   the   GM   (AI)   can   refer   to   that   list   and   reload   the

corresponding files as needed to reconstruct the full knowledge. This design acknowledges that simply

restoring JSON data is not enough – the “knowledge” in those markdown instructions and libraries needs to

be   present   as   well.   By   persisting   the   references,   AIDM   guides   the   re-initialization   process   (Module   03’s
import   likely   reads   loaded_libraries   and   attempts   to   fetch   them).   A   minor   risk   is   if   a   library   file

changed significantly between save and load (e.g. trope definitions updated). The save doesn’t freeze the

content of libraries, only which ones were used. If absolute reproducibility is needed, one might include a

library   version   or   even   embed   key   points   into   memory.   But   given   libraries   mostly   provide   stylistic   or

reference guidance, slight changes likely won’t break a campaign. The continuity afforded by this tracking is

impressive – it shows the developers considered the scenario of stopping a campaign and coming back

later without the AI “losing its place” in genre emulation. Everything loaded is remembered. The system
state   also   tracks   active_power_systems   (which   of   the   energy   systems   are   in   play)

  and   player

82

content preferences (e.g. if the player set a violence level to moderate)

83

, further ensuring the game’s

configuration is persistent.

7

Assessment of State Persistence

Overall,  AIDM   v2’s   state   management   and   persistence   is   well-designed   and   quite   exhaustive.

Strengths include:

-  Comprehensive   Data   Coverage:  Virtually   all   game   facets   (character,   NPCs,   world,   narrative   style)   have

structured representation in the state, leaving few blind spots.

- Atomic, Consistent Updates: The system treats state updates transactionally with validations, reducing error

accumulation over long play.

- Robust Save Format: The JSON export encapsulates not just raw state but contextual info (recent dialogue,

loaded files, etc.) to truly freeze a moment in the campaign for later revival

15

16

.

-  Memory   &   Narrative   Continuity:  Past   events   and   genre   calibrations   persist,   preventing   the   AI   from

“forgetting” the story or changing tone unintentionally.

Weaknesses and gaps:

- Lack of Specialized Quest Engine: While quests are tracked, there’s no dedicated system for complex quest

logic (branching paths, time-limited quests, etc.). The groundwork is there in state, but management is
manual.

- Schema Evolution Risk: No automatic migration for older saves – a major schema change could make old

exports incompatible without manual intervention (mitigated by version tagging but still a concern).

-  Reliance on Manual Updates:  The system relies on the AI (as GM) to properly update the state schemas

during play. A lapse (like forgetting to update a world flag or NPC field) could cause discrepancies. The

validation rules might catch many of these, but some might slip through or require a retcon if noticed later.

Essentially, the garbage in, garbage out principle – the persistence is only as good as the inputs.

- Volume and Performance: As campaigns grow, the state JSON will enlarge (dozens of NPCs, many memory

threads). There could be performance costs in validation or searching through this, though given modern

context   sizes   (and   if   only   relevant   parts   are   loaded),   it’s   likely   fine.   It’s   something   to   monitor;   perhaps

indexes or splitting might be needed if a campaign world becomes enormous.

In conclusion, State Management & Persistence in AIDM v2 is a robust pillar of the system. It shows a

clear understanding that an AI-driven RPG must maintain continuity just like a human GM’s notes would.

Few comparable AI systems go this far in preserving and validating the game state. The approach will scale

to moderately complex campaigns (multi-year in-game timelines, world-altering events, many NPCs) with

ease. Only extremely large-scale scenarios (e.g. tracking 100+ active quests or hundreds of NPCs) might

strain the current design, and those can be addressed with future optimizations (like archiving or unloading

truly dormant data). The solid foundation is there – persistence is not an afterthought but rather deeply

ingrained   in   AIDM’s   architecture.   This   bodes   very   well   for   the   system’s   ability   to   support   long-running,

evolving anime campaigns without losing narrative cohesion or mechanical accuracy.

Sources: The analysis references the AIDM v2 repository, including Module 03 (State Manager) for design

rules

1

20

, Module 02 (Learning Engine) for memory handling

35

37

, and the JSON schema files for

state   structure   (character,   world,   NPC,   session   export,   etc.)

2

10

.   These   sources   substantiate   the

described behaviors and data fields.

1

12

13

14

20

21

22

45

46

66

72

73

74

75

76

77

78

79

80

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/instructions/

03_state_manager.md

8

2

3

4

67

68

70

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/

character_schema.json

5

6

7

8

9

10

11

15

16

17

18

19

39

62

63

64

69

81

82

83

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/

session_export_schema.json

23

24

27

28

71

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/

CORE_AIDM_INSTRUCTIONS.md

25

26

29

30

31

32

33

34

35

36

37

38

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/instructions/

02_learning_engine.md

40

41

42

43

44

47

48

49

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/npc_schema.json

50

51

52

53

54

55

56

57

58

59

60

61

65

GitHub

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/

world_state_schema.json

9

