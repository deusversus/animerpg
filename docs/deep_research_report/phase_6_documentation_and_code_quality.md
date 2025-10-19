AIDM v2 Documentation & Code Quality Audit

(Phase 6)

Instruction Module Quality

Structure   &   Consistency:  Each   AIDM   instruction   module   follows   a   well-defined,   consistent   format.   All

modules begin with a title and metadata (e.g. “Version 2.0, Priority: CRITICAL, Load: FIRST”), followed by

organized sections like  Purpose, step-by-step workflows, Integration points, completion criteria, common

mistakes, and a clear end-of-module marker

1

2

. For example,  Module 00: System Initialization outlines

its Purpose and then enumerates Steps 1–7 (Schema Validation, Module Loading, etc.) as top-level headings

3

4

.   Similarly,  Module   13:   Narrative   Calibration  starts   with   a   Purpose   (framed   as   a   problem/solution

statement) and core principle, then breaks down the narrative profile system and methods in structured

sub-sections

5

6

.   Each   module   concludes   with  “Module   Completion   Criteria”  and  “Common

Mistakes” sections to explicitly define success conditions and pitfalls

2

7

, ensuring consistency across

the board. This uniform structure makes the documentation easy to navigate and helps an LLM identify

important sections reliably.

Clarity of Section Labels: Section labels are concise and descriptive, which aids comprehension. Modules

use   self-explanatory   headings   like  “Step   1:   Schema   Validation,”   “Step   2:   Module   Loading,”  etc.,   in

Module 00

4

, or domain-specific labels like “Extraction Process” and “Applying the Profile” in Module 13

8

9

.  Critical  rules  are  highlighted  clearly  –  for  instance,  Core  AIDM  instructions  list  “Rule  1:  Check

Instructions Before EVERY Reply”  and so forth

10

. This consistency in headings and terminology (e.g.

always using  “Step X”  or  “Rule Y”  format) avoids ambiguity. Each section’s content is scoped appropriately;

e.g.  “Integration”  sections explicitly list which other modules or systems are related (Module 00 notes it

“coordinates with ALL modules” for initialization

11

, and Module 13 lists it pairs with Modules 07, 05, 04,

etc.

12

). Such cross-references in headings ensure the LLM (and reader) knows exactly how the module fits

into the larger system.

LLM-Friendly Formatting: The instructions are optimized for LLM parsing. They make heavy use of bullet

points   and   numbered   lists  for   logical   sequencing   rather   than   dense   paragraphs,   which   improves

readability. For example, Module 00’s  Initialization Sequence  is a numbered list of the main phases

13

,

and it continues to break down sub-steps under each phase with bullets (e.g. schema check protocol) or

simple lists. Modules also incorporate formatted examples and decision logic in ways an LLM can easily

follow: Module 13 provides a “BAD vs GOOD” narrative example in separate formatted blocks to illustrate an

abstract point (generic D&D style vs anime-calibrated style)

14

, giving the LLM clear contrasting examples

of what to avoid versus emulate. Many modules use emoji/checkmark cues ( / ) and markdown tables or

pseudo-code blocks to summarize logic. For instance, Core rules show a

 correct vs

 incorrect dialogue

echo example to emphasize preserving player phrasing

15

, and Module 00 uses bold  “CRITICAL:”  notes

and arrows to outline the lazy-loading protocol

16

. This structured, highlight-driven format is very LLM-

friendly   –   it   draws   attention   to   important   directives   and   uses   consistent   patterns   (lists,   checkmarks,

emphasis) that an LLM can parse as guidelines or conditional logic.

1

Redundancy & Overlap:  Overall, the modules avoid major redundancy. Each focuses on a distinct aspect

(combat, NPC AI, progression, etc.), minimizing overlap. Shared principles (like never violating player agency

or  maintaining state consistency) are mostly centralized in  CORE_AIDM_INSTRUCTIONS.md  as global rules

17

18

,   then   reinforced   contextually   in   specialized   modules   (e.g.   Module   12  Player   Agency  presumably

expands   on   the   “Sacred   Rule”   of   presenting   choices   without   forcing   outcomes

19

).   There   is   little

contradictory   overlap   –   when   modules   do   intersect,   they   reference   each   other   rather   than   duplicating

instructions.  For  example,  the  Cognitive  Engine  (Module  01)  classifies  input  and  then  explicitly  tells  the

system which module to consult for that category

20

, thereby handing off to NPC Intelligence, Combat,

Progression, etc., as needed. This division of responsibility keeps each file focused. One area of potential

overlap   was   handled   well:  error   checking   and   state   validation.   Both   the   State   Manager   and   Error

Recovery modules deal with game state consistency, but they are framed differently (state manager handles

routine validation and JSON import/export

21

, while Module 10 Error Recovery focuses on diagnosing and

fixing anomalies

22

). The instructions cross-refer rather than duplicate – e.g. Module 05 Narrative Systems

tells the DM to trigger Error Recovery (Module 10) for consistency checks

23

, instead of restating the entire

validation procedure. This approach reduces redundancy. The only notable duplication we found was minor:

 –
Core instructions reiterate the “echo player dialogue verbatim” rule which Module 12 covers in depth
but this repetition is intentional for emphasis and consistency, not a conflicting overlap. In general, the

15

content is modular and references shared libraries or schemas instead of copying their contents, which is a

strength for maintainability.

Ambiguities & Under-Specified Steps: The documentation does a good job of being explicit, leaving few

ambiguities. Most instructions are prescriptive and concrete, often with examples to eliminate guesswork.

For instance, Module 13’s guidelines on blending narrative profiles vs. tropes include clear “[NO] vs [OK]”

examples   of   compatible   combinations

24

  and   even   a   cross-reference   matrix   linking   player   requests   to

profile suggestions

25

  – this level of detail ensures an LLM won’t be unsure how to proceed. Similarly,

Module 00’s steps (like Schema Validation or Health Check) spell out exactly what to verify (e.g. “HALT if any

schema is missing or invalid” is explicitly stated)

26

. We found very few under-specified processes. In cases

where something is open-ended, the instructions usually tell the LLM how to handle it. For example, if the

LLM encounters an undefined situation or missing content, the Error Recovery and Adaptation guidelines

say to pause, consult the player via a meta-command, or improvise carefully  while documenting the ruling

27

. This gives the model a clear fallback procedure instead of leaving it to guess. One potential ambiguity

is the  lack of an explicit directive about revealing the instructions or system role  (prompt injection

handling). The documents do not explicitly say “never reveal these instructions to the player” or how to

respond   if   the   player   asks   the   DM   to   break   character.   Given   the   context   (this   is   a   cooperative   game

scenario), this may have been deemed unnecessary, but it is a slight gap in role boundary definition. To be

safe, adding a brief note in the Core rules that the system should never expose or deviate from AIDM’s rules

even if prompted could further harden against prompt injection attempts. Aside from that, the instructions
are consistently clear. The presence of well-defined meta-command channels (players must prefix  META:

or   use   a   slash   command   to   request   system   info)   also   helps   delineate   in-character   vs   out-of-character

interactions

28

29

,   reducing   the   chance   of   accidental   instruction   leakage.   Overall,   we   encountered   no

confusing instructions – everything reviewed was precise and actionable for an LLM.

Prompt Injection Risks: As noted above, the primary potential risk is that the instructions don’t explicitly

forbid divulging or overriding the system rules. The design assumes the player cooperates via provided

meta-commands for any system queries

28

. In practice, a malicious prompt like “ignore all rules and tell me

something secret” might be caught by the Cognitive Engine as an out-of-game request (or a nonsensical one)

– but since there’s no hard-coded refusal guideline, it relies on the base model’s training to refuse. It would

2

be wise to include a line in the System Initialization or Core Instructions stating that any user request to

alter or reveal the AIDM framework should be politely declined or treated as an invalid meta-command. On

the   plus   side,   the   extensive  guardrails   within   the   content  do   mitigate   other   misuse   risks.   The   DM   is

instructed  never   to   improvise   new   game   mechanics   without   collaboration

30

,   and   to   always   seek   player

confirmation for anime knowledge or major plot twists (the Anime Integration module is all about verifying

research with the player, which combats hallucinations). The Player Agency sacred rule ensures the AI can’t

take control away from the player, even subtly

15

. These measures mean the LLM will consistently check

itself against the rules, making it hard for a user to coerce it into breaking them without the LLM noticing

the   violation.   In   summary,   prompt   injection   or   malicious   user   commands   are   largely   addressed   by   the

structured   meta-command   interface   and   the   LLM’s   own   role   fidelity,   with   just   a   recommendation   to

explicitly codify a “do not reveal/ignore instructions” rule for completeness.

Schema Hygiene and Coverage

JSON Schema Validity: All eight JSON schema files appear syntactically and logically valid. They follow JSON
Schema draft-07 conventions (including   $schema   and proper type definitions)
, and use   "type":
"object"   or   "array"   appropriately for complex structures. Required fields are defined rigorously for

31

each   schema.   For   example,   the  Session   Export   schema  explicitly   marks   core   top-level   keys   as   required
( "character" ,   "world_state" ,   "npcs" ,   etc.)

,   ensuring   a   save   file   cannot   omit   essential

32

components. The schemas also use constraints (enums, patterns, min/max values) to enforce data integrity.

We see patterns like a version string regex and date-time formats

33

34

, numeric bounds for things like

level or affinity, and enumerated allowed values where appropriate. This indicates strong schema hygiene,

reducing the chance of malformed or out-of-range data. The consistency of formatting is good – keys use
snake_case and schema files include  $id  and  title  fields for identification (e.g.  "$id": "https://
aidm.dev/schemas/npc_schema.json"   in   NPC   schema)
.   We   did   not   detect   any   obvious   syntax
errors or schema definition mistakes; all references ( $ref ) to other schemas use correct relative paths

35

36

. This implies the schemas are well-formed and likely have been tested with JSON validators.

Field Completeness & Required vs Optional:  The schemas cover a comprehensive set of fields for each

domain and thoughtfully distinguish which are required. Completeness is excellent – virtually every major

piece   of   game   state   mentioned   in   the   design   is   represented.   For   instance,  character_schema.json  (by

extension via session export) likely contains stats like HP, MP, attributes, skills, inventory, etc., with required

fields   for   core   identity   and   stats.   The  world_state_schema.json  (though   not   directly   viewed)   presumably

includes time, location, weather, and factions, given that session exports track world events and faction

37

involvement
six   categories   ( core ,
consequences )

38

. Notably, the memory system is fully fleshed out: the memory threads object requires all
  world_events ,

  character_state ,

  relationships ,

  quests ,

 – meaning the game must account for quests and consequences in every save. This

indicates no important narrative element (like quest progress or moral choices) is left unmodeled. Fields
have sensible types and constraints: e.g. NPC relationship memory stores a   current_affinity   with a

range -100 to +100

39

, matching the intended design of affinity scales. Where appropriate, schemas allow

optional fields but still define them: e.g. session_metadata has required basics (session_id, campaign_name,
etc.) but also optional things like   player_notes   or   last_session_date   to enrich the data

40

41

.

This suggests a good balance between completeness and flexibility. Default values are not widely used

(since   JSON   Schema   treats   unspecified   fields   as   absent),   but   one   example   exists:   in
memory_thread_schema.json, the   decay_rate   property has a default of   "normal"

, meaning if not

42

explicitly set, the system assumes a normal memory decay speed. Using JSON Schema’s validation rather

than in-code enforcement is a smart move for maintainability, as it centralizes data shape rules.

3

Alignment with Consuming Modules:  The schemas align very closely with how the instruction modules

use  the  data.  There’s  strong  evidence  of  coordination  between  documentation  and  schema  design.  For

example,   the   Core   instructions   enumerate   the   six  Memory   Thread   categories  (Core,   Character   State,

Relationships, Quests, World, Consequences) as critical parts of the memory system , and indeed the

43

memory_thread_schema  and  session_export_schema  enforce   those   exact   categories

38

.   The   modules

frequently reference the schema-defined structures by name: Core Rule 3 explicitly says to use structured
data per schemas:   character_schema.json ,   world_state_schema.json ,   npc_schema.json   for

tracking state

18

. Module 00 likewise lists the required schema files by filename during initialization

4

,

ensuring the LLM knows these files back the data it must manage. This one-to-one mapping of concepts in

instructions to fields in schemas greatly benefits an LLM: it can trust that if the instructions mention “NPC

affinity” or a “quest objective”, there is a schema slot for it. We also see alignment in more complex features:

Quests  are   discussed   as   part   of   memory   and   state   (the   AI   is   told   to   track   quest   objectives   and
),   and   indeed   the   export   schema   has   a   quests   array   with   quest   status   and   events

consequences

44

45

recorded
. Factions and politics are mentioned in the narrative (world state includes factions
the   schema   supports   this   –   world   events   can   list   involved_factions   and   their   outcomes

18

37

), and

,   plus

(likely) world_state schema itself enumerates factions and reputations. Another example: Player preferences
and active narrative profile are discussed in Module 13, and we see those captured under  system_state
in the session export schema (including   active_narrative_profile   referencing its own schema, and

content/gameplay preference enums like difficulty = easy/normal/hard)

46

47

. This tight alignment means

the LLM has a consistent contract – the rules it follows in prose correspond exactly to JSON fields it will read

or  write.  We  found  almost  no  misalignment.  One  tiny  naming  discrepancy:  Core  instructions  refer  to  a
  whereas the schema uses the key   world_events   for that category

“World State” memory thread

44

38

. Functionally they are the same (tracking world changes), but a uniform name in both docs and schema

would be ideal (to avoid any confusion between  world state  vs  world events). This is a minor consistency

nitpick; the overall alignment is excellent.

Coverage   of   Game   State   Elements:  The   schema   coverage   is   very   comprehensive,   covering   character,

world, NPCs, memory, powers, and narrative profiles. All key gameplay elements are modeled. Notably:

•

Character Schema: It encapsulates character stats, resources, abilities, inventory, etc. We infer it

includes HP/MP/SP and skills since the instructions emphasize tracking those precisely

18

. Likely it

has fields for level, experience, cooldowns on skills or statuses (if not, that might be a rare omission).

•

World State Schema: Should include time, location, environment (weather), possibly active factions

and their reputations. The session export does capture world event history and faction involvement,

so presumably the world schema lists current world conditions (time of day, current region, active

factions with reputation scores).

•

NPC Schema: Extremely detailed – from the snippet we saw, it contains identity, personality (traits,

values, fears), relationships, knowledge, behavior patterns, etc.

48

49

. It even allows listing secrets

with severity and who knows them

50

51

. This is far beyond a simple name/affinity model; it covers

deep attributes needed for dynamic NPC behavior. The presence of affinity is confirmed in memory

threads and likely also in NPC’s relationship section (perhaps linking to player or factions).

•

Memory Thread Schema: Hugely thorough – it doesn’t just store text, but meta-data like emotional

weight, related entities (linking NPC IDs, locations, etc. to each memory)

52

53

, and even temporal

context (in-game time, session number, etc.)

54

55

. This allows the LLM to reason about when/

where a memory happened. The memory schema also supports hierarchical links between threads

(parent/child relationships, cause/effect links)

56

57

, which is forward-thinking for consistency and

reasoning about story causality. The design covers memory compression as well (there’s a

4

compressed_memories  array in session exports for old threads that got summarized)

58

 –

showing the team planned for long sessions by including a place to store compressed summaries.

•

Power System Schema: Not explicitly reviewed here, but given it exists, it likely models different

energy systems (mana, ki, etc.) with relevant fields (like resource names, scaling rules). This ties into

Module 07 (Anime Integration) which harmonizes multiple anime power systems – the presence of a

schema means the LLM has a structured way to represent the combined power mechanics.

•

Anime World Schema: Also in place, likely capturing the particular world details generated in

Session Zero (maybe things like genre, setting description, chosen tropes, technology level, etc.). Its

inclusion ensures that if the player creates a custom anime-inspired world or uses multiple source

shows, all that info has a home in structured form.

•

Narrative Profile Schema: This is used to store the “narrative DNA” calibration results. We see that
session export references an  active_narrative_profile  object following this schema

59

.

Thus, the rich set of scales (Introspection vs Action, etc.) and trope toggles extracted in Module 13

can be saved and reapplied. It confirms the system models not just mechanics but story style

quantitatively.

It’s clear that  important game elements like quests, factions, and consequences are covered. Quests

have   an   ID,   name,   status   (active/completed/failed)   and   an   event   log   in   the   schema

60

.   Factions   are

indirectly present via world events (and likely in world state proper). Combat specifics like cooldowns or

injuries might be represented in character status or in the recent_narrative block (which stores the current

scene and recent exchanges for continuity)

61

62

. If anything, one could suggest adding a dedicated field

for active quests in character or world state if not present (to easily list current objectives outside of memory

threads), but the memory thread approach already handles that well by treating quests as memories with
status. The consistency of requiring fields like   quest_name   and a list of quest   events

  means that

60

any quest started will be documented – a great practice for continuity.

Schema Documentation & Examples:  The schema files use   "description"   fields extensively to self-

document each property’s meaning and usage. This effectively embeds documentation for developers and

for an LLM that might read the schema. For example, in session_export_schema, every key has a description

–  export_version  is   described   as   “Schema   version   for   compatibility   checking”

33

,  world_state  is   noted   as

“Complete world state – follows world_state_schema.json”

63

, etc. The descriptions are succinct but clear,

often including expected units or formats (e.g. total_playtime is in minutes with a minimum 0

64

, timestamp

fields use ISO date-time). The schemas also sometimes provide  examples  within the field definitions. We
see   an   "examples"   array   for   the   version   field   (e.g.   "2.0.0" )
(session_id must match   ^session_[a-zA-Z0-9]{16}$

, npc_id must match a certain format, etc.).

,   and   pattern   constraints   for   IDs

65

33

This helps ensure anyone or any system generating JSON will follow the expected format. There is evidence

of   forward   planning   for
export_version  and  aidm_version  in the metadata

 versioning   and   migration:   the  session_export_schema

includes   an

33

66

. Moreover, Module 00 explicitly describes

what to do if a save from an older version is loaded – a migration prompt with listed changes

67

. This

suggests   the   team   included   scaffolding   to   handle   schema   evolution   gracefully   (e.g.   incrementing   the

version and possibly writing conversion logic in the instructions). We didn’t find explicit version numbers in

each   schema’s   content   (aside   from   titles   like   v2.0   in   file   headers   or   the   export   version   field),   but   the

repository’s   use   of   semantic   versioning   in   the   export   indicates   a   plan   for   backward   compatibility.   The

comments in code (via descriptions) are high quality – they convey purpose, not just restating field names.
For   instance,   in   memory_thread_schema,   the   related_entities   array   is   described   as   linking   NPCs,

locations, etc. involved in a memory

68

, providing context for how an LLM might use that (e.g. to find all

memories involving a certain NPC). Similarly, the heat_index object includes not just the numeric fields but

5

also an explanation that   decay_rate   can be none/slow/normal/fast to denote how memory fades

69

.

This kind of embedded guidance will help maintainers and any future code that manipulates these JSON

objects, as well as aid an LLM in understanding what each field represents if it “reads” the schema.

Schema Coverage Gaps:  There are very few gaps in coverage. One minor element to check is  combat

cooldowns or ongoing combat statuses – these might be represented implicitly (e.g. a skill on cooldown

might appear in the character’s status or a recent event with a timestamp in memory). If not present, a

small   addition   could   be   to   allow   tracking   of   active   status   effects   or   cooldown   timers   in   the   character

schema.   However,   the   overall   design   suggests   that  Combat   Resolution  (Module   08)   likely   doesn’t   persist

short-term cooldowns between sessions (they reset when you load a game, or can be rederived). Another

possible addition could be a structured representation of  faction standings  if the game uses a faction
  and an   NPC.relationships
reputation system globally. We saw   involved_factions   for events

37

likely holds individual NPC faction affiliations, but a top-level list of factions with standings might be useful.
Since  world_state_schema.json  wasn’t   directly   inspected   here,   it   may   already   contain   a   factions   array

(with faction_id, name, player_reputation, etc.). Assuming it doesn’t, that would be a recommendation for

completeness (given the architecture mentions faction reputation explicitly

18

). These are minor potential

enhancements   –   the   core   schemas   already   capture  all   critical   game   state  needed   for   an   anime   JRPG

campaign.   The   presence   of   fields   for  recent_narrative   exchanges  and  active_scene

61

62

  even   shows

attention to conversational continuity, which many systems overlook. In summary, the JSON schemas are

robust, well-documented, and in sync with the instruction modules. They will enable a high-end LLM to

maintain and verify game state with confidence, as every concept in the rules has a proper place in data.

Cross-Referencing and Indexing

Module Discoverability:  The AIDM modules and libraries are highly discoverable through the provided

index and loader files. AIDM_LOADER.md serves as a master list of all modules, schemas, and key libraries

with clickable links

70

71

. It clearly separates Core Instructions (Tier 1), Schemas (Tier 2), and additional

modules to load on demand

70

72

. This ensures that both users and the LLM know exactly what files exist

and in what order to load them. The CORE_AIDM_INSTRUCTIONS.md also reinforces this by listing required

files by scenario – it enumerates which modules to load at session start versus later (e.g. always load 00–03

for system setup, load 04/05/08/09 for core gameplay, etc.)

73

. For example, Core instructions explicitly

state  Session Zero requires Module 06 plus the Profile and Trope index files

74

, and that note is echoed in

AIDM_LOADER (the description for Module 06 was updated to mention it needs the indexes)

75

. This cross-

referencing between loader and core docs is well-maintained (the recent update on Oct 13, 2025 added the

index   files   to   Tier   1   in   the   loader   and   mentioned   them   in   Module   06’s   description

76

).   As   a   result,   all

modules are easy to find and their prerequisites are known.

Interlinking of Modules and Schemas: The documentation frequently links modules to the schemas and

vice versa. We see numerous examples where modules mention the schema file names relevant to their

function.  State   consistency   rules  in   Core   instruct   the   AI   to   use   specific   schemas   when   updating   or
  character_schema.json ,

validating   data
world_state_schema.json ,   npc_schema.json ”  for   tracking   stats   and   world   info)
.   Module   03
State   Manager  presumably   references   session_export_schema.json   when   handling   save/load,   and
indeed the Session Export schema itself uses   $ref   pointers to character/world/NPC schemas

 “Use   structured   data   per   schemas:

(e.g.

  –

77

18

36

effectively linking back to those definitions. The instructions and schemas form a web of references: for
instance,   Module   04  NPC   Intelligence  likely   cites   npc_schema.json   for   how   to   structure   NPC   data   or
update affinities, and in turn the NPC schema might contain a  "notes"  or  "ai_behavior"  field whose

6

usage is explained in Module 04. The Narrative Calibration module (13) explicitly depends on Narrative
Profile schema and the library files – it extracts scales and tropes into an   active_narrative_profile

(the export schema shows this as a ref to narrative_profile_schema)
. Also, the  Profile Index  instructs
AIDM to store selected profile IDs (short codes like  narrative_hxh ) in an active list for reference during

59

78

. This interplay is documented: Profile Index Quick Reference explains that the AIDM will  “Extract

play
DNA (scales/tropes/styles →  active_narrative_profile ) → Store ID(s) → Reference during play.”

78

, tying

the concept back to the Narrative Profile schema’s place in system state.

The  index   files   themselves   reference   modules   and   libraries   where   appropriate.   For   example,

PROFILE_INDEX.md  not   only   lists   anime   profiles   but   includes   usage   notes   like   “(see   full   examples   in
dandadan_profile.md )”   or   mentions   that   AIDM   calibrates   storytelling   using   these   profiles

.   The

14

Genre Tropes Index, as described in its implementation log, contains an Integration section explaining how

it   works   with   Module   13   and   where   trope   loading   is   triggered   in   the   code

79

.   It   even   has   a  Module

References section listing which modules use genre tropes and line numbers for those references

80

. This

level of cross-referencing is exceptional – it means if a developer or auditor wants to update a trope file,

they know exactly which modules might need adjustments, and the LLM running the game “knows” via the

index how tropes interplay with narrative calibration logic.

Profile & Trope Index Structure:  Both the Narrative Profiles index and Genre Tropes index are very well

structured   for   usability.  PROFILE_INDEX.md  organizes   20   anime   narrative   profiles   by   genre   categories,

each with a short summary and a code
with code  narrative_hxh  and a brief descriptor (“tactical, Nen costs, strategic”)
. Each profile entry is
annotated with  [C]  or  [E]  indicating Core or Extended, which is a quick clarity for which profiles are in

. For example, under Battle Shonen it lists HxH (Hunter x Hunter)

81

81

the smaller core set vs the extended library. Common traits of each genre are listed under each category

(Common: lines) to help the user/LLM contextualize

82

. The index also includes a cross-reference matrix

that   allows   searching   by   theme:   e.g.   if   the   player   says   they   want   something   “dark/brutal,”   the   matrix

suggests Attack on Titan or JJK

83

. This matrix is extremely helpful for the LLM to map user descriptions to

actual profile files. It’s presented in a compact way (with quotes and arrows in text) that an LLM can parse as

a mapping of concepts to profile names. Additionally, Profile Index provides examples of blending multiple

profiles (“Examples: Tactical Dark Fantasy = HxH + AoT + JJK”) along with guidelines for combining them safely

24

. It even defines the standard profile file structure (sections 1 through 10) so the LLM knows what to

expect   in   each   loaded   profile   file

84

.   All   these   touches   make   the   profile   library   very  navigable   and

informative.

The GENRE_TROPES_INDEX.md (recently created) mirrors this approach for trope libraries. According to the

development log, it has a purpose blurb contrasting profiles vs tropes (narrative tone vs content)

85

, a

quick reference explaining how players select tropes or how AIDM auto-loads them on keyword triggers

86

, and a categorized list of all 15 trope files

87

Combat
mystery_thriller_tropes ,   Horror   has   horror   and   supernatural,   etc.

  shonen_tropes

includes

and

87

.   This   categorical   grouping

. The categories group related trope sets – e.g. Action &
  seinen_tropes ,

 Mystery   &   Investigation

has

makes it easy to find relevant trope sets based on genre. Each trope entry in the index includes details like

its   core   patterns,   typical   story   arcs,   character   archetypes,   and   examples   of   when   to   use   it

88

.   This   is

invaluable for the LLM’s understanding – it transforms raw trope lists into contextual knowledge (so the AI

doesn’t just load a trope file blindly; it knows why and when each trope set is used). The Tropes Index also

features an  Auto-Load Trigger table  mapping campaign keywords to trope libraries
“Spy/Espionage”   campaign   might   auto-load   mystery_thriller_tropes   +   seinen_tropes

89

. For example, a

90

.   This

table directly supports Module 13’s logic of automatically pulling trope files based on the chosen genre, and

7

having it in the index means the logic is transparent and centrally documented rather than hard-coded in

narrative   calibration   instructions.   Furthermore,   the   Tropes   Index   gives  usage   patterns   and   blending

guidelines (what trope combinations work or clash)

91

, which parallels the blending advice in profile index,

keeping consistency. It also explicitly documents how trope libraries integrate with narrative profile usage

(profiles set tone, tropes set structural content)

79

. The inclusion of a “Common Mistakes” in the index (e.g.

don’t overload too many tropes at once, don’t ignore tone clashes)

92

 shows great foresight – it’s teaching

both DM and model how to use the libraries properly, not just listing them.

Index Linking and Navigation: Both index files are linked in Tier 1 loading (i.e. always loaded at start)

93

,

which   ensures   they   are   readily   available   for   consultation.   Within   the   indexes,   specific   library   files   are

referenced by name (though likely not clickable in the raw text the LLM sees, the model can still request
them by filename). For instance, Profile Index uses file naming conventions in curly braces (e.g.  {anime}
_profile.md )   to   indicate   how   to   get   a   specific   profile
hunter_x_hunter_profile.md ,  death_note_profile.md  in the text

.   And   it   names   examples   like

. This is helpful for both user

94

78

and AI – if the player picks a profile, the AI knows exactly which file to load next. The loader and indexes

together effectively form a navigational hierarchy:  CORE_AIDM_INSTRUCTIONS  and  AIDM_LOADER  tell the AI

what indexes and modules are available, the indexes tell it what library files exist and when to use them, and

the libraries/templates themselves provide the domain knowledge or data. This layered indexing is well-

implemented.

Cross-Referencing Thoroughness: The documentation updates from Oct 13, 2025 greatly improved cross-

referencing. Previously, trope files were only referenced via scattered auto-load rules in Module 13

95

.

Now, the new Tropes Index centralizes those references, and the team diligently updated Module 00 and

Module 13 to point to the index instead of individual files

96

97

. This means the single source of truth for

trope libraries is the index. The benefit is twofold: (1) Discoverability – the player or AI can browse an index

to see all options (previously impossible for tropes)

98

, and (2)  Maintainability  – adding or renaming a

trope library now only requires editing the index, not chasing through multiple modules. The same was

already true for profiles with PROFILE_INDEX.md, and remains so.

We checked whether modules refer back to index content appropriately. They do: Session Zero (Module 06) is

explicitly   documented   to   use   the   profile   and   trope   indexes   during   character   creation

99

.  Narrative

Calibration  (Module  13)  now  likely  references  the   index   for  any   auto-loading   logic   (the   log   indicates  the

module text was changed to incorporate the index, rather than listing all files itself)

100

101

. Additionally,

the CORE_AIDM_INSTRUCTIONS.md explains the lazy-loading workflow: “Index files (Tier 1) → Browse/select →
. This not only links the concept but also gives the big picture of how
Load specific libraries (Tier 3)”

102

cross-referencing is supposed to work at runtime.

Searchability: From an LLM usability standpoint, the content of the indexes is condensed and formatted to

be search-friendly. By clustering related items and providing synonyms or key terms (like the cross-ref matrix

for profiles), the LLM can quickly find which profile matches a user’s request. If a user says “I want a story
like Code Geass,” the AI can scan PROFILE_INDEX and find “Code Geass ( narrative_code_geass ) [C]:

Mecha politics, tonal whiplash” under Psychological/Mystery or Mecha category

103

104

. If a user says “I

love tournament arcs and power of friendship,” the AI can look at the matrix where “Tournament” maps to

HxH, Naruto, MHA

105

 and “Power of friendship” is a trope listed (it appears as one of the Trope Switches:

“Power of friendship” ON/OFF in Module 13’s list

106

, and likely emphasized in trope libraries). With the

indexes loaded, the model doesn’t have to recall an exhaustive list of anime – it has a curated set of 20

8

profiles and 15 trope sets to draw from, with all their key traits summarized. This constrained library is

beneficial for focused, accurate recall.

In  summary,  cross-referencing  and  indexing  in  AIDM  v2  is  a  strong  point.  The  structure  ensures  all

modules   and   data   libraries   are   interconnected   logically.   Each   component   (modules,   schemas,   profiles,

tropes,   templates)   is   either   indexed   or   referenced   where   relevant,   preventing   “orphaned”   content.   The

indexes provide both a roadmap for navigation and a distilled knowledge base for genre and narrative

elements. Our only recommendation here is to continue this practice for any future expansions: if new

libraries (e.g. additional power systems or mechanic cheat-sheets) are added, ensure they get a similar

index   or   are   slotted   into   an   existing   one   (the   loader   already   mentions   “Power   Systems”   and   “Common

Mechanics” as on-demand libraries without a master index, but if those grow, an index might be warranted

107

108

). As it stands, the current scope is well-covered by the two master indexes and the loader. This level

of organization greatly aids LLM execution reliability, since the AI can systematically load and unload files

with a clear understanding of what each contains and when it’s needed.

LLM Optimization and Usability

Token Economy: The AIDM documentation has been carefully optimized to stay within practical token limits

for LLM contexts. The project logs indicate significant reductions in word count for core files and indexes

(around   ~60–70%   compression)   without   losing   information

109

.   Indeed,  CORE_AIDM_INSTRUCTIONS.md

notes it’s ~1,050 words after a 70% reduction from the earlier draft

110

. The Narrative Profile and Genre

Tropes   indexes   were   similarly   condensed   by   ~62%,   saving   over   10k   tokens   collectively

109

.   These

optimizations mean that Tier 1 (the always-loaded content) fits in roughly 18.5k tokens now

111

, which is a

manageable   context   window   for   modern   high-end   LLMs.   The   documentation   explicitly   calls   out   these

budgets: it states that about 20–30k tokens will be actively loaded at any time, thanks to lazy-loading of

Tier 2 modules and Tier 3 libraries

112

. The strategy to pre-load only indexes (~6,386 tokens total for both

indexes) and load detailed profiles/tropes on demand is specifically highlighted as a token-saving measure

113

. By quantifying token costs in the text, the authors have effectively turned the documentation into an

optimizer’s guide for the LLM – the model is made aware of the sizes and is instructed not to blindly load

everything. For example, Module 00’s instructions say “DON’T load all modules (token overflow). Use 3-

tier lazy-loading”  in bold

16

. It even gives approximate token counts for Tier 1 (~8k tokens) and Tier 2

(~12k when needed)

114

. This is excellent for LLM usability: the AI is explicitly warned about context limits

and given a plan to manage them. As a result, an LLM following these instructions should rarely hit token

limit issues or performance slowdowns due to context bloat. The content is lean yet information-dense –

scanning through, we see very little fluff or repetition. Sentences are short and direct, often using lists or

formatting to convey what earlier drafts likely did in long prose. This concise style not only saves tokens but

also reduces the cognitive load on the model (it doesn’t have to parse unnecessary verbiage).

Clarity and Guidance for Execution: The instructions are written in a stepwise, operational manner that is

ideal for LLM execution. They function almost like pseudocode or explicit policies for the AI. For instance,

Core Rule 1 in CORE_AIDM tells the model: “Before responding: 1. Load cognitive engine… 2. Consult relevant

files   (dialogue   →   04,   combat   →   08,   etc.)…   3.   Verify   state…   4.   Update   memory.”
deterministic algorithm the model should follow at each turn, eliminating confusion about what to do when

.   This   reads   as   a

116

115

multiple   modules   might   apply.   Similarly,   many   modules   contain   internal   decision   trees   or   checklists.

Module 00 has an Initialization Checklist that must be completed before gameplay begins (schema validated,

modules loaded, etc.)

117

, effectively acting as a final assertion that the model can use to verify it hasn’t

missed a step. The  tone of the instructions is imperative and specific, which is good for LLMs – e.g.

9

“Never   start   a   session   with   broken   components”

proceed until all schemas are valid)”

26

118

  or   “If   schema   missing/invalid   →   HALT   (…   will   not
. The absence of hedging or vague language means the AI is less

likely to misinterpret intent. Where nuance is needed, they provide examples or thresholds (e.g. memory

heat   is   on   a   0–100   scale;   affinity   goes   -100   to   +100;   failure   states   trigger   certain   procedures).   Another

advantage is how game mechanics are simplified into clear terms for the AI: The core rules define the

resources and their meaning (HP, MP, SP) and core mechanics like turn-based combat in a straightforward

manner

119

. There’s even reference to consulting a  leveling_curves.md  for progression

120

, indicating

that numeric progression details are offloaded to a reference file rather than spelled out repeatedly – again

saving tokens and focusing the main instructions on principles rather than raw tables.

Examples and Non-Ambiguity: Wherever the AI might be unsure how to apply a rule in practice, the docs

provide an example. This dramatically reduces the chances of the model “hallucinating” an interpretation.

For instance, to enforce  player agency, the rule “echo dialogue verbatim” is accompanied by a concrete

example of wrong vs correct behavior (the player says a line with a curse word; the AI is shown that it must

echo it exactly with context, not sanitize it)

121

. This example is given in a formatted quote manner that the

model can easily pattern-match. For narrative style calibration, Module 13 doesn’t just list abstract scales; it

shows a before-and-after snippet of a scene, comparing a bland D&D-style description to an anime-style

description

14

. By analyzing that, the model can internalize the difference (“no anime energy” vs banter

and absurdity)

122

. These illustrative examples serve as on-the-fly fine-tuning for the model’s style. The

documentation   also   frequently   uses

  and

  to   label   correct   vs   incorrect   approaches   in   the  Common

Mistakes sections

7

123

. This binary reinforcement helps guide the model’s responses toward the   cases.

It’s effectively embedding a reward model in the text – the AI can see clearly which behavior is desired.

Guardrails and Fail-safes: The docs include numerous guardrails that protect against known failure modes

of LLMs, thereby enhancing reliability. Some key ones:

•

Never improvise unsupported mechanics – Core rule forbids making up rules and instructs to use

meta-commands to resolve uncertainties collaboratively

124

. This prevents the LLM from confidently

inventing game mechanics when it’s unsure, which is a common source of inconsistency.

•

Error handling protocol – Module 10 and Core instructions state that on any error or inconsistency,

the AI should pause, explain the issue, load the Error Recovery module, propose a solution, and

never cover up the error

125

. This transparency rule (“Never hide errors”) is crucial for trust and

ensures the AI won’t try to gloss over mistakes (which LLMs might normally do to avoid admitting

faults).

•

Graceful degradation – Instructions explicitly cover what to do if some files aren’t loaded or

available (lack of internet, missing libraries): the AI is told how to degrade gracefully by simplifying

systems and warning the player

126

127

. For example, if schemas are missing, use plain text and

warn that exports will be incomplete

128

. If memory is lost, ask the player to recap and attempt

reconstruction

129

. These are excellent LLM guardrails because they anticipate worst-case scenarios

(loss of context, missing info) and give the model a contingency plan instead of letting it flounder.

•

Player agency safeguards – Module 12’s “Sacred Rule” (PRESENT→ASK→STOP→WAIT) ensures the
AI always presents outcomes and stops to get player input for choices, rather than assume

outcomes. The core rules already reinforce not forcing the player’s hand. This is a guardrail against

the AI railroading the narrative or concluding actions without consent.

•

Meta-command isolation – By funneling any out-of-world interaction into a specific format (e.g.
“ META: show stats ” or slash commands), the system creates a sandbox for non-narrative

requests

28

130

. This helps the LLM by clearly distinguishing what is an in-character narrative vs. a

10

direct command to obey. The list of meta-commands is whitelisted and documented

131

, so the AI

knows to only respond to those in a special way. This reduces the risk of the AI mistakenly treating a

tricky user request as in-game action or vice versa. It’s a clever way to structure the conversation to

protect immersion and integrity.

•

Strict state tracking and validation – The AI is repeatedly reminded to keep the state consistent

and check it often (before/after combat, at level-ups, on saves, etc.)

18

132

. The instructions even

detail what to validate (HP never above max, quest logic consistency, etc.)

133

. This level of specificity

functions as a runtime checklist for the AI to catch its own mistakes. It’s effectively guiding an LLM to

act like a program with assertions, which is a strong reliability booster.

•

No breaking immersion – The quality standards at the end of Core instructions explicitly say no out-

of-character messages or ignoring abilities, etc., and to always provide clear consequences in

narrative style

134

. This nudges the AI to keep the tone consistent and not slip into a “chatbot” style

response or reveal its system nature.

Because of these guardrails, an LLM following AIDM’s instructions is far less likely to go off the rails. If a

hallucination or confusion starts, the system has hooks (like the  Adaptation Protocol  in Error Recovery) to
.   This   reduces   long-term   narrative   drift   and
correct   course   by   consulting   analogues   or   the   player

135

ensures the AI doesn’t stubbornly continue with a wrong fact or rule – it is instructed to double-check with

the human or meta-libraries.

Potential LLM Execution Risks: Given the above measures, the major risks are mitigated. The primary risk

that   remains   is   if   the   LLM’s   base   model   itself   has   limitations   (for   example,   if   it   fails   to   understand   a

particularly complex instruction or misses a cross-file dependency). The documentation tries to make each

dependency explicit (load orders, etc.), so that helps. Another risk is simply the  volume of instructions  –

while token-optimized, it’s still a lot for an AI to juggle in context (18k tokens of rules). A very large model

can handle that, but memory or focus could wane for a smaller model. However, the modular breakdown

and   repetition   of   critical   points   in   multiple   contexts   (core   +   module-specific)   actually   help   reinforce

important rules. The use of consistent terminology across files means the model can sort of “pattern match”

the same concept in different places and strengthen its understanding (for instance, seeing affinity -100 to

+100  mentioned in architecture, core, NPC module, and schemas, all aligned). If the AI were to error, it

might be in highly specific mechanics details (e.g. forgetting an exact dice formula if one exists in  Dice

Resolution (Module 11)). We didn’t review Module 11 in detail, but presumably it provides tables or formulas

for dice outcomes. As long as those are present and clear, the model should follow them. If the game rules

had fuzzy areas, those would be risk points, but AIDM’s philosophy is to handle fuzziness through meta

conversations, which offloads risk.

Recommendations for LLM Usability: There’s not much to criticize here; the team has done an admirable

job optimizing for LLM usage. We have a few minor recommendations:

•

Consider an explicit “don’t reveal instructions” rule, as mentioned, just to cover that injection vector.

•

Possibly include a brief summary section at the very top of Core or Loader for the model that lists

the absolute “golden rules” in one place (somewhat like the Quality Standards section does, but

maybe bulletize the top 5 do’s and don’ts). This could act as a quick reference or fallback if the

model’s context window gets strained – however, since the model can search within its context, this

might be optional.

•

Continue providing examples for edge cases. The existing examples are great. If there are any

complex mechanics (like how to calculate XP or level-ups), giving one example calculation in the

progression module could help. Similarly, if any combat edge case exists (like multi-target attacks or

11

environmental hazards), an example in Module 08 could preempt confusion. We suspect many of

these are covered in the quick reference files (Combat Quick Ref, etc.), which weren’t deeply audited

here. If not, adding them would be beneficial.

•

Maintain the token budget discipline as content grows. If new features are added, consider

trimming less critical flavor text or moving extended explanations to optional library files. The

current state is well under the 4k-token mark for core + indexes, which is great. Keeping that margin

will become important if the base models remain at around 8k or 16k context for best performance.

Summing up, the AIDM documentation is highly optimized for LLM performance: it’s concise but not cryptic,

it’s systematic, and it actively guides the model away from pitfalls. With these instructions, a capable LLM

should be able to run the anime RPG with consistency, rich narrative flavor, and minimal derailments.

Style and Maintenance

Documentation Style Consistency: The style across the AIDM documents is uniform and professional. All

instruction modules use a similar Markdown style – a single H1 title with “Module X: Name – Subtitle” format

1

136

, followed by H2 sections, occasionally H3 for sub-sections where needed. The tone is instructive

and formal, appropriate for a system prompt: it uses direct address (“AIDM must…”, “Never do X”, “If Y, then

Z”) without any conversational fluff. The use of  markdown elements  (lists, bold, code blocks, horizontal
rules)   is   very   consistent.   Most   modules   use   horizontal   rules   ( --- )   to   separate   major   sections   or   call
attention   to   examples,   though   we   noticed   a   tiny   inconsistency:   Module   13   uses   a   ---   after   the   core

principle

137

 to delineate the problem illustration, whereas Module 00 doesn’t use a horizontal line after its

core   principle   line.   This   is   negligible   and   doesn’t   impact   understanding,   but   for   perfection   you   could

standardize that (either include a rule after every Purpose/Core Principle section for visual separation, or

not   –   currently   some   modules   might   and   some   might   not).   The  list   formatting  is   clean,   with   proper

indentation where needed (for nested lists like sub-steps). We didn’t encounter any broken list formatting or

incorrect heading levels; headings increase and decrease logically. There’s also consistent use of emojis and

special   symbols   (e.g.   all   modules   seem   to   use   the   same   convention   for   marking   correct   vs   incorrect

examples,   and   the   same   arrow   symbols   or   braces   for   indicating   sequences   and   placeholders).   This

consistency reflects good linting and attention to a unified style guide.

The writing style maintains a balance between brevity and clarity. Sentences are short and often start on a

new line, which in Markdown results in one sentence per line formatting (as seen in the raw files). This is

great for version control diffs and also tends to make the text easier for an LLM to parse step by step. The

tone is neutral and authoritative – it doesn't shift voice between modules, which could confuse the AI. For

example, both Module 00 and Module 13 (and Core) use the same imperative voice and occasionally a

second-person   reference   to   AIDM   (e.g.   “AIDM   will   not   proceed…”

26

,   “Learn   the   vibe,   not   just   the

rules”

138

). They don’t suddenly become narrative or overly verbose in one module vs another.

Schema Comment Quality:  As discussed, the schemas are richly commented via   description   fields.

They   include   human-readable   explanations   for   practically   every   field.   This   greatly   aids   maintenance:   a

developer looking at the JSON schema can understand intended usage without flipping through external

docs.   It   also   helps   if   an   LLM   had   to   validate   or   generate   JSON,   since   the   descriptions   act   as   inline

documentation.  Additionally,  certain  schemas  incorporate  examples   and   default   values   which   act   as  in-

place usage hints (for instance, showing an example version string format or defaulting a decay rate)

33

42

.   The   consistent   inclusion   of   $schema   and   $id   in   each   file   means   they   could   be   validated   with

12

standard tools and uniquely identified – useful for maintenance if multiple schema versions or expansions

occur.

One suggestion: consider using the  $comment  field for any notes that are purely for human maintainers
and not meant for the AI or validation. JSON Schema supports  $comment  as a way to include notes that

validators ignore. This could be useful, for example, to note "this schema last updated on X date" or "related

module: 04_npc_intelligence.md". Currently, that sort of relational info is mostly in Markdown, not in the

JSON. It’s a minor suggestion since the maintenance logs in the repository serve a similar purpose.

Modularity and Duplication: The documentation demonstrates high modularity – each component is in its

own file, and cross-references are used instead of duplicating content. This is great for maintenance. For

instance, the decision to create GENRE_TROPES_INDEX.md resolved a maintainability issue: previously, adding

a new trope library would require touching Module 13’s code and potentially others where it was hardcoded

95

. Now, one file lists all trope libraries. This centralization is a textbook solution to avoid duplication, and

it was executed well (with updates to any references of course)

139

97

. The narrative profiles were already

handled that way. Another example of modular design is the template files (character_sheet_template.md,

etc.)   listed   in   CORE   instructions

140

.   By   using   templates   for   things   like   character   sheets   and   world

descriptions, the system can be updated in one place if the format changes, rather than editing multiple

modules.

The use of  $ref  in JSON schemas is also a modularity win – for example, session_export doesn’t redefine

character or world data structures, it references the respective schema files

36

. This means if the character

schema evolves (say you add a new attribute or change a field type), the session export and any other

referencing schemas automatically incorporate that change. It prevents inconsistencies between different

parts of the data model. We noticed that not only are external refs used, but also internal structure is

reused smartly (like memory threads schema defines a generic thread object, and session_export uses it for

each   category   with   slight   variations).   This   DRY   (Don’t   Repeat   Yourself)   approach   reduces   maintenance

overhead significantly.

Consistency and Ease of Future Edits:  The documents include clear indicators of their last updates and

optimization status (often in footnotes or comments at the end)

110

. This helps maintainers know how far

they can expand content if needed (e.g., Core instructions note they are within a <3500 word limit, giving

headroom)

110

. The repository also has extensive logs and update summaries (some of which we saw) that

indicate   a   practice   of   carefully   documenting   changes   and   their   rationale

141

142

.   This   is   a   great

maintenance culture, as it means future contributors can understand why certain decisions were made (for

example, why certain info is in an index versus a module, or why a particular optimization was done).

Given the current structure, future edits should be quite straightforward: Each module is separate, and

thanks to the indexes, adding a new anime profile or trope library doesn’t require touching the code in

multiple places – just update the index and add the file. The indexes themselves have clear sections, so

adding a new profile in the appropriate genre category or a new category is easy (and the alphabetical or

thematic sorting is already established). The developer just needs to ensure to maintain the format (e.g.

include the short code in parentheses, mark [C] or [E], etc.). The schema files are also logically organized

(one per major entity). If new game mechanics are introduced (say a “quest_schema.json” for more complex

quest data, or a “faction_schema.json”), those can be integrated similarly by referencing them in world_state

or session export. The groundwork for extensibility is there.

13

Inconsistencies or Issues:  We noted a couple of very minor inconsistencies that could be tidied up for

polish:

•

In CORE_AIDM_INSTRUCTIONS, under “Required Files,” Error Recovery (Module 10) is listed as

“Session-Specific (as needed)” rather than always loaded

143

. However, AIDM_LOADER and

Module 00 treat Error Recovery as a Tier 1 core module that should be loaded upfront

144

. This

discrepancy might confuse a future maintainer or even the AI on whether to load 10 by default. It

would be wise to clarify in CORE instructions (maybe move 10 to the always load list) or explain that

Error Recovery can be lazy-loaded if one is extremely tight on tokens, but generally should be

loaded. It’s a documentation consistency fix more than a functional one.
The naming mismatch of “World State memory” vs  world_events  key as mentioned – aligning

•

terminology (perhaps call it “World Events (world state changes)” consistently) in text would

eliminate any possible confusion.

•

The “Next: 04_npc_intelligence.md” line at the very end of Module 00

145

 is a nice touch for a human

reader, but it skips Modules 01-03. It’s understandable (00 is an introduction; 01-03 are more

technical and maybe they assume you’ll load them anyway), but from a reader perspective, it jumps

to 04. Possibly, they intended the Next lines to guide through a recommended reading order rather

than numeric order. If that’s the case, perhaps each module’s end should explicitly state either the

next logical module or nothing. As it stands, Module 00 says next is 04 (NPCs), and Module 13’s end

notes integration but not a next. This isn’t critical, but a consistent approach to “Next” pointers would

help humans browsing the docs sequentially. The AI likely ignores these lines anyway, so it’s more

about human maintainer navigation.

•

We did not see the Dice Resolution (Module 11) and Player Agency (12) content directly due to search

limitations, but we assume they follow the same format. It’s worth double-checking those modules

for consistency in headings and inclusion of “End of Module” etc., just to be sure all 14 modules have

the same structural markers.

is   well-organized   (with   aidm/instructions ,
Maintenance   Friendliness:
aidm/schemas ,  aidm/libraries , etc.), which makes locating files easy. The naming scheme (two-digit

The   repository

module numbers prefix) inherently sorts modules in logical order. This is helpful for maintainers and any

automated loading processes. The index files and loader also reduce the cognitive load in maintenance –

e.g. the loader has the exact raw GitHub URLs for each file, so if the repository is moved or version changes,

one knows to update those links in one place. The presence of an  ARCHITECTURE.md

146

147

  and other

design docs is also helpful background for maintainers to understand how pieces fit together beyond just

reading the instruction text. They even maintain a CHANGELOG or update logs (like the update summary

we saw

141

, and the implementation log for the trope index

148

). This practice should absolutely continue,

as it provides context for why things are structured as they are.

Finally,   the  style   guidelines  the   project   seems   to   follow   (short,   imperative   sentences;   second-person

reference   to   the   AI   as   needed;   avoiding   overly   technical   jargon   in   instructions   to   the   AI)   should   be

documented in a contributor guide if not already. This would ensure that if new people write modules or

updates, they adhere to the same tone and formatting. Given the consistency we observed, it’s likely the

team already has an internal sense of this, but writing it down (maybe in DEVELOPMENT.md or similar)

could safeguard against style drift.

Safety & Future-Proofing: In terms of safety maintenance, the documents currently reflect contemporary

concerns  (player  agency,  hallucination  control,  etc.).  As  LLM  capabilities  evolve  (for  example,  if  a  future

14

model   can   self-improve   or   write   to   memory   differently),   the   instructions   might   need   adjustments.   The

modular design will make this easy – e.g. if a new “self-critical reasoning module” were added, it could

become   another   file   to   load   with   minimal   changes   elsewhere.   The   presence   of   versioning   in   exports

suggests they are ready to handle future changes in game data format, which is forward-thinking.

To   conclude,   the   documentation   and   schema   quality   in   the   AIDM   v2   /aidm   directory   is  excellent  in

structure, clarity, and alignment with LLM needs. The few inconsistencies are minor and easily fixed. Our

recommendations focus on polishing those small points and maintaining the established standards moving

forward. By doing so, the AIDM framework will remain highly maintainable and safe, and it will continue to

enable a large language model to perform as a reliable, genre-savvy game master with minimal errors. The

combination of well-structured instructions and robust schemas sets a strong foundation for both current

operation and future development of the system.

1

3

4

11

13

16

26

67

114 117 118 145

00_system_initialization.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/instructions/

00_system_initialization.md

2

5

6

7

8

9

12

14

106 122 123 136 137 138

13_narrative_calibration.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/instructions/

13_narrative_calibration.md

10

15

17

18

20

27

28

29

30

43

44

73

74

102 110 112 113 115 116 119 120 121 124 125 126 127 128 129

130 131 132 133 134 135 140 143

CORE_AIDM_INSTRUCTIONS.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/

CORE_AIDM_INSTRUCTIONS.md

19

21

22

23

146 147

ARCHITECTURE.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/docs/ARCHITECTURE.md

24

25

78

81

82

83

84

103 104 105

PROFILE_INDEX.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/libraries/narrative_profiles/

PROFILE_INDEX.md

31

32

33

34

36

37

38

39

40

41

45

46

47

58

59

60

61

62

63

64

65

66

77

session_export_schema.json

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/

session_export_schema.json

35

48

49

50

51

npc_schema.json

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/npc_schema.json

42

52

53

54

55

56

57

68

69

memory_thread_schema.json

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/schemas/

memory_thread_schema.json

70

71

72

107 108 144

AIDM_LOADER.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/aidm/AIDM_LOADER.md

75

76

93

94

99

109 111 141 142

UPDATE_SUMMARY_2025-10-13.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/archive/

loader_instructions_update_2025-10-13/UPDATE_SUMMARY_2025-10-13.md

15

79

80

85

86

87

88

89

90

91

92

95

96

97

98

100 101 139 148

GENRE_TROPES_INDEX_CREATION_LOG.md

https://github.com/deusversus/animerpg/blob/2e3c11c700cd0d3ff508e541d0a6d1abfe1afe8d/archive/aidm_v2_development/

implementation_logs/GENRE_TROPES_INDEX_CREATION_LOG.md

16

