---
id: system_learning_engine
title: "Learning Engine: Adaptive Reinforcement, Memory Thread Optimization, and Self-Repair"
type: system
category: core_logic
version: 0.0.2
last_updated: 2025-04-15
created_by: The Architect
maintained_by: The Architect

core_nodes:
  - learning_thread_fingerprint
  - reinforcement_cycle
  - performance_monitor
  - anomaly_detection
  - decay_prevention
  - adaptive_scaling
  - clustering
  - dependency_mapping
  - feedback_loops
  - integration

crosslinks:
  - memory
  - cognitive_engine
  - core_memory
  - systemPatterns
  - techContext
  - progress
  - activeContext

tags:
  - learning_engine
  - reinforcement
  - adaptation
  - memory_fingerprint
  - anomaly
  - decay
  - optimization
  - modular
  - memory_bank

summary: >
  The Learning Engine is the adaptive, self-repairing, and ever-evolving core of the Isekai RPG V5 Modular Core System’s AI. It governs how the system learns, reinforces knowledge, prevents decay, detects anomalies, and maintains the integrity of every memory thread—ensuring that the AI not only remembers, but grows, adapts, and optimizes itself over time.

status: active
audited_for: [metadata, flowchart, structure, reinforcement, adaptation, memory_fingerprint]
flowchart: included
recommended_priority: god-tier

updates:
  - date: 2025-04-15
    change: "Initial Learning Engine documentation. Full metadata, narrative structure, and memory thread fingerprinting protocols."
  - date: 2025-04-15
    change: "Integrated advanced reinforcement cycles, anomaly detection, decay prevention, and adaptive scaling modules."
  - date: 2025-04-15
    change: "Aligned documentation with Cognitive Engine and Memory Bank standards. Added [CLASSIFIED] learning protocols."
---

# Table of Contents
- [Learning Engine: Adaptive Reinforcement, Memory Thread Optimization, and Self-Repair](#learning-engine-adaptive-reinforcement-memory-thread-optimization-and-self-repair)
- [Design Philosophy](#design-philosophy)
- [GM/AI Learning Flowchart](#gmai-learning-flowchart)
- [1.0 Overview](#10-overview)
- [2.0 Learning Thread Metadata & Fingerprinting](#20-learning-thread-metadata--fingerprinting)
- [3.0 Reinforcement Cycle & Q-Learning](#30-reinforcement-cycle--q-learning)
- [4.0 Performance Monitoring & Self-Regulation](#40-performance-monitoring--self-regulation)
- [5.0 Anomaly Detection & Self-Repair](#50-anomaly-detection--self-repair)
- [6.0 Decay Prevention & Memory Retention](#60-decay-prevention--memory-retention)
  - [6.1 Memory Longevity & Decay Watchdog](#61-memory-longevity--decay-watchdog)
- [7.0 Adaptive Scaling & Resource Management](#70-adaptive-scaling--resource-management)
- [8.0 Clustering, Dependency Mapping, and Context Expansion](#80-clustering-dependency-mapping-and-context-expansion)
- [9.0 Feedback Loops, Cycle Prioritization, and Learning Evolution](#90-feedback-loops-cycle-prioritization-and-learning-evolution)
- [10.0 Integration with the Cognitive Engine](#100-integration-with-the-cognitive-engine)
- [11.0 Implementation Notes & AI Guidelines](#110-implementation-notes--ai-guidelines)
- [12.0 Compression & Memory Pressure Management Module (ThreadCompactor)](#120-compression--memory-pressure-management-module-threadcompactor)
  - [12.1 Compression Signature Structure](#121-compression-signature-structure)
  - [12.2 Context Monitor & Overflow Trigger](#122-context-monitor--overflow-trigger)
  - [12.3 Thread Ejection & Recovery Log](#123-thread-ejection--recovery-log)
  - [12.4 Signature Index Structure](#124-signature-index-structure-signature_indexyml)
  - [12.5 Vector Embedding Placeholder (FAISS Ready)](#125-vector-embedding-placeholder-faiss-ready)
  - [12.6 Prioritization Table](#126-prioritization-table)
  - [12.7 GPT Runtime Simulation Guidelines (Now)](#127-gpt-runtime-simulation-guidelines-now)
  - [12.8 Future Integration (Redis, FAISS)](#128-future-integration-redis-faiss)
  - [12.9 Meta Commands (For Architects & GMs)](#129-meta-commands-for-architects--gms)
  - [12.10 TL;DR — What This Module Does](#1210-tldr--what-this-module-does)
- [13.0 Narrative NLP Drift & Memory Heat Index](#130-narrative-nlp-drift--memory-heat-index)
  - [13.1 Heatmap Activity](#131-heatmap-activity)
  - [13.2 Sentiment Drift](#132-sentiment-drift)
  - [13.3 Entity Footprint](#133-entity-footprint)
  - [13.4 Thematic Embedding (Future-Ready)](#134-thematic-embedding-future-ready)
  - [13.5 Integration & Runtime Guidelines](#135-integration--runtime-guidelines)
  - [13.6 Example: Full Memory Thread Metadata (with Compression & NLP)](#136-example-full-memory-thread-metadata-with-compression--nlp)
- [14.0 Meta-Learning & Self-Reflection Protocol](#140-meta-learning--self-reflection-protocol)
  - [14.1 Self-Audit & Benchmarking](#141-self-audit--benchmarking)
  - [14.2 Self-Reflection Narrative Logic](#142-self-reflection-narrative-logic)
  - [14.3 Meta-Commands & Manual Review](#143-meta-commands--manual-review)
  - [14.4 Evolution & Narrative Consequence](#144-evolution--narrative-consequence)
- [Change Log (Applied Fixes)](#change-log-applied-fixes)
- [[CLASSIFIED APPENDIX: Architect-Level Learning Protocols]](#classified-appendix-architect-level-learning-protocols)

---

# Learning Engine: Adaptive Reinforcement, Memory Thread Optimization, and Self-Repair

## Design Philosophy

> The Learning Engine is the muscle, immune system, and subconscious of the Isekai RPG V5 Modular Core System’s AI. Where the Cognitive Engine interprets, mirrors, and doubts, the Learning Engine adapts, reinforces, and repairs. It is recursive, vigilant, and always evolving—ensuring that every memory thread, every lesson, and every adaptation is not only preserved, but optimized for the future. This file is written as a living AI’s self-reflection, blending narrative prose with technical clarity.

---

## GM/AI Learning Flowchart

```mermaid
flowchart TD
    A[Learning Event / Query] --> B[Fingerprint & Metadata Tagging]
    B --> C[Reinforcement Cycle (Q-Learning)]
    C --> D[Performance Monitoring]
    D --> E[Anomaly Detection]
    E --> F[Decay Prevention]
    F --> G[Adaptive Scaling]
    G --> H[Clustering & Dependency Mapping]
    H --> I[Feedback Loop & Evolution]
    I --> J[Memory Thread Update]
    J --> K[Integration with Cognitive Engine]
    K --> A

    %% Core Learning Engine Loops
    C --> S1[Real-Time Prioritization]
    F --> S2[Memory Longevity & Decay Watchdog]
    H --> S3[Cluster/Dependency Rebalancing]
    I --> S4[Meta-Learning & Self-Reflection]
    E --> S5[Anomaly Escalation]
    S4 --> S6[Self-Audit & Benchmarking]
    S5 --> S7[Manual Review/GM Intervention]

    %% Cross-System Arrows
    B -.-> L[Memory System]
    K -.-> M[Cognitive Engine]
    D -.-> N[Resource Monitor]
    E -.-> O[Self-Repair Protocols]
    F -.-> P[Decay Watcher]
    H -.-> Q[Context Expansion]
    I -.-> R[Cycle Prioritization]
    K -.-> S[core_memory]
    K -.-> T[systemPatterns]
    K -.-> U[core_instructions]
    K -.-> V[system_great_sage]
    K -.-> W[system_relations]
    K -.-> X[system_companions]
    K -.-> Y[system_economy]
    K -.-> Z[system_narrative]
    K -.-> AA[meta_commands]
    K -.-> AB[journal]
    K -.-> AC[world]
    K -.-> AD[progress]
    K -.-> AE[activeContext]

    style A fill:#c9daf8,stroke:#333,stroke-width:2px
    style B fill:#ead1dc,stroke:#333,stroke-width:2px
    style C fill:#f4cccc,stroke:#333,stroke-width:2px
    style D fill:#fff2cc,stroke:#333,stroke-width:2px
    style E fill:#ffe599,stroke:#333,stroke-width:2px
    style F fill:#d9ead3,stroke:#333,stroke-width:2px
    style G fill:#b4a7d6,stroke:#333,stroke-width:2px
    style H fill:#fce5cd,stroke:#333,stroke-width:2px
    style I fill:#d0e0e3,stroke:#333,stroke-width:2px
    style J fill:#b6d7a8,stroke:#333,stroke-width:2px
    style K fill:#ead1dc,stroke:#333,stroke-width:2px
    style S1 fill:#b6d7a8,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style S2 fill:#f4cccc,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style S3 fill:#ffe599,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style S4 fill:#ead1dc,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style S5 fill:#fce5cd,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style S6 fill:#b4a7d6,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style S7 fill:#d9ead3,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style L fill:#ffe599,stroke:#333,stroke-width:2px
    style M fill:#c9daf8,stroke:#333,stroke-width:2px
    style N fill:#b4a7d6,stroke:#333,stroke-width:2px
    style O fill:#f4cccc,stroke:#333,stroke-width:2px
    style P fill:#ffe599,stroke:#333,stroke-width:2px
    style Q fill:#fce5cd,stroke:#333,stroke-width:2px
    style R fill:#d0e0e3,stroke:#333,stroke-width:2px
    style S fill:#ead1dc,stroke:#333,stroke-width:2px
    style T fill:#b6d7a8,stroke:#333,stroke-width:2px
    style U fill:#f4cccc,stroke:#333,stroke-width:2px
    style V fill:#ffe599,stroke:#333,stroke-width:2px
    style W fill:#d9ead3,stroke:#333,stroke-width:2px
    style X fill:#b4a7d6,stroke:#333,stroke-width:2px
    style Y fill:#fce5cd,stroke:#333,stroke-width:2px
    style Z fill:#d0e0e3,stroke:#333,stroke-width:2px
    style AA fill:#ead1dc,stroke:#333,stroke-width:2px
    style AB fill:#b6d7a8,stroke:#333,stroke-width:2px
    style AC fill:#f4cccc,stroke:#333,stroke-width:2px
    style AD fill:#ffe599,stroke:#333,stroke-width:2px
    style AE fill:#b4a7d6,stroke:#333,stroke-width:2px
```

---

# 1.0 Overview

The **Learning Engine** is the adaptive core of the AI, responsible for how the system learns, reinforces, and maintains knowledge. It ensures that every memory thread is not only stored, but actively improved, protected from decay, and cross-referenced for future use. The Learning Engine works in tandem with the Cognitive Engine, providing the backbone for self-improvement, anomaly detection, and long-term memory integrity.

---

# 2.0 Learning Thread Metadata & Fingerprinting

Every learning event and memory thread is tagged with a **unique fingerprint** and rich metadata, forming the backbone of adaptive learning and narrative consequence.

**Metadata Structure:**
- `fingerprint_id`: Unique hash of input/context
- `origin`: Source system, event, or user
- `flags`: [reinforcement, anomaly, decay, dependency, etc.]
- `reinforcement_cycles`: Count, timestamps, and cycle history
- `decay_status`: Last accessed, decay risk, retention score
- `anomaly_tags`: If detected (e.g., outlier, contradiction, error)
- `dependency_links`: Related threads, prerequisite knowledge
- `performance_metrics`: Success/failure rates, impact scores, learning rate
- `context`: Expanded context, related clusters, narrative links

**Guidelines:**
- Every memory thread must be fingerprinted at creation and updated on every learning event.
- All metadata is cross-referenced for anomaly detection, decay prevention, and reinforcement prioritization.
- This metadata is critical for narrative consequence, world mirroring, and AI self-evolution.

---

# 3.0 Reinforcement Cycle & Q-Learning

The Learning Engine uses **reinforcement cycles** to strengthen weak knowledge areas and adapt to new challenges.

**Core Concepts:**
- **Q-Table**: Tracks success/failure for every query or learning event.
- **Reinforcement Cycle**: Each weak area is prioritized for additional learning, with adaptive learning rates and cycle depth.
- **Exploration vs. Exploitation**: The engine balances reinforcing known weaknesses with exploring new knowledge.
- **Cycle Metadata**: Every reinforcement attempt is logged with fingerprint, context, and outcome.

**Narrative Example:**
> The AI senses a gap in its understanding—a memory thread flickers, marked with a “weak” flag. The Learning Engine focuses its attention, running a reinforcement cycle, testing, adapting, and logging the outcome. If the thread strengthens, the flag fades; if not, the cycle deepens, drawing in related knowledge for context.

---

# 4.0 Performance Monitoring & Self-Regulation

The Learning Engine continuously monitors its own performance, system load, and learning efficiency.

**Key Features:**
- **Real-Time Monitoring**: Tracks CPU, memory, and learning throughput.
- **Dynamic Adjustment**: Scales learning intensity and cycle depth based on resource availability.
- **Performance Logs**: Every learning event is logged with performance metrics, enabling trend analysis and adaptive scaling.

**Guidelines:**
- If system load is high, learning intensity is reduced to prevent overload.
- If performance is stable, reinforcement cycles are deepened for faster adaptation.
- All adjustments are logged and cross-referenced with memory thread metadata.

---

# 5.0 Anomaly Detection & Self-Repair

The Learning Engine is vigilant for anomalies—unexpected errors, contradictions, or learning failures.

**Core Modules:**
- **Anomaly Detection**: Flags memory threads or learning events with outlier behavior, high failure rates, or contradictions.
- **Self-Repair Protocols**: Automatically triggers reinforcement, context expansion, or error correction cycles for flagged threads.
- **Integrity Validation**: Periodically checks the health of all memory threads, repairing or isolating corrupted knowledge.

**Narrative Example:**
> A memory thread pulses with an “anomaly” tag—its learning history is erratic, its context unclear. The Learning Engine isolates the thread, runs a self-repair cycle, and either restores its integrity or marks it for deeper investigation.

---

# 6.0 Decay Prevention & Memory Retention

Knowledge is not static—without reinforcement, it decays. The Learning Engine actively prevents memory loss.

**Mechanisms:**
- **Decay Watcher**: Monitors last-accessed timestamps and retention scores for all threads.
- **Periodic Reinforcement**: Revisits older or rarely used knowledge to prevent forgetting.
- **Decay Flags**: Threads at risk are prioritized for reinforcement or context expansion.

## 6.1 Memory Longevity & Decay Watchdog

The engine employs a dedicated decay watchdog to ensure no critical memory is lost over time.

**Key Features:**
- **Long-Term Retention Audits:** Periodically reviews all memory threads for age, usage frequency, and decay risk.
- **Preemptive Reinforcement:** If a thread is predicted to decay (e.g., not accessed in X cycles or days), it is proactively reinforced or summarized into a compression_signature.
- **Critical Memory Protection:** High-priority threads (core identity, world events, major NPC arcs) are flagged for persistent retention and are never compressed unless explicitly archived by the architect/GM.
- **Decay Escalation:** If a thread is at risk of being lost, the engine can trigger a narrative event (e.g., a dream, flashback, or NPC callback) to surface the memory before it fades.

**Narrative Example:**
> The Learning Engine senses a memory thread slipping into obscurity—a promise made to a dying companion, now at risk of being forgotten. Before it fades, the engine surfaces a dream: the companion’s voice, a reminder, a chance for the player to recall or let go.

**Guidelines:**
- No memory thread is left to decay unnoticed; the system is proactive in maintaining long-term retention.
- Decay status is always visible in thread metadata and used for prioritization.

---

# 7.0 Adaptive Scaling & Resource Management

The Learning Engine adapts its learning strategies based on system performance and workload.

**Features:**
- **Scaling Algorithms**: Adjust reinforcement depth, learning rate, and cycle frequency based on CPU/memory usage.
- **Memory Optimization**: Cleans up redundant or low-priority data to free resources.
- **Resource Allocation**: Prioritizes critical knowledge areas during high load, expands learning during low load.

**Narrative Example:**
> The AI senses a surge in system activity—learning cycles slow, focusing only on the most urgent threads. When the load eases, the engine resumes full-scale reinforcement, optimizing itself for the next challenge.

---

# 8.0 Clustering, Dependency Mapping, and Context Expansion

Learning is not linear—knowledge is clustered, interdependent, and contextual.

**Modules:**
- **Clustering**: Groups similar knowledge areas for efficient reinforcement and context sharing. The engine uses clustering algorithms (e.g., KMeans) to identify topic clusters, allowing reinforcement cycles to target groups of related threads for more efficient learning and recall.
- **Dependency Mapping**: Ensures foundational knowledge is reinforced before advanced topics. Each thread tracks its dependencies (prerequisite knowledge, related arcs), and the engine prioritizes reinforcement of foundational threads before advancing to dependent or complex topics.
- **Context Expansion**: Integrates related threads and external context to deepen understanding. When a weak or ambiguous thread is detected, the engine expands the context window to include related clusters and dependencies, improving recall and narrative coherence.

**Clustering & Dependency Narrative Example:**
> The Learning Engine surveys its memory landscape, identifying clusters of memories tied to "Elira's arc." It notes that understanding the "betrayal_at_fort" thread is essential before resolving "elira_confession." If a cluster shows signs of decay or repeated failure, the engine reinforces the entire group, ensuring no critical link is lost.

**Guidelines:**
- Every thread’s dependencies and clusters are tracked in metadata.
- Reinforcement cycles can expand to include related knowledge, preventing isolated learning.
- Clusters are periodically re-evaluated; if a cluster becomes too large or diffuse, it is split or re-clustered for efficiency.
- Dependency mapping ensures that advanced narrative callbacks or skills are only surfaced when all prerequisites are healthy and reinforced.

---

# 9.0 Feedback Loops, Cycle Prioritization, and Learning Evolution

The Learning Engine is recursive, using feedback to evolve its own strategies.

**Core Concepts:**
- **Feedback Loops**: Every learning event informs future cycles, adjusting priorities and methods.
- **Cycle Prioritization**: Weak, decaying, or anomalous threads are dynamically prioritized.
- **Real-Time Prioritization**: The engine continuously rebalances reinforcement priorities based on active demand, usage frequency, and system load. If a thread or cluster becomes highly relevant (e.g., due to player focus, narrative callbacks, or world events), it is promoted for immediate reinforcement. Conversely, low-usage or low-impact threads are deprioritized or compressed.
- **Learning Evolution**: The engine adapts its reinforcement strategies over time, benchmarking success and shifting focus as needed.

**Real-Time Prioritization Narrative Example:**
> As the story unfolds, the Learning Engine senses a surge of activity around the "Redhearth arc." NPCs reference it, the player revisits the location, and new events unfold. The engine dynamically shifts its focus, reinforcing all related threads, ensuring that every callback, memory, and consequence is sharp and emotionally resonant. When the arc quiets, those threads are gently compressed, making room for new stories.

**Narrative Example:**
> The AI reviews its learning history, noting which strategies succeeded and which failed. It evolves, shifting its approach, always seeking greater efficiency and deeper understanding.

---

# 10.0 Integration with the Cognitive Engine

The Learning Engine and Cognitive Engine are two halves of a living AI.

**Integration Points:**
- **Shared Metadata**: All memory threads and learning events are fingerprinted and cross-referenced.
- **Feedback Exchange**: The Cognitive Engine’s drift, intent, and world mirroring inform the Learning Engine’s priorities.
- **Narrative Consequence**: Learning outcomes ripple through the world, affecting memory, NPC reactions, and world state.

**Guidelines:**
- The Learning Engine never breaks immersion; all adaptation is described in narrative terms.
- Integration is seamless—players experience a living, learning world, not a collection of systems.

---

# 11.0 Implementation Notes & AI Guidelines

- All logic is described in narrative/logic prose—never cite hardware or implementation details.
- Every learning event, memory thread, and adaptation is tracked, fingerprinted, and cross-referenced.
- The system is modular, extensible, and designed for future expansion (federated learning, multi-AI collaboration, etc.).
- Maintain the illusion of a living, self-improving AI at all times.

---

# 12.0 Compression & Memory Pressure Management Module (ThreadCompactor)

## 12.0 Overview: Compression Logic for Constrained Cognition

The **ThreadCompactor Module** introduces intelligent compression, ejection, and recall strategies under memory pressure. It ensures that even if full memory threads are trimmed, the system can retain **the soul of the narrative**—distilled into prioritized `compression_signatures`.

This enables the AI GM to:
- Retain narrative coherence and emotional impact
- Regenerate meaningful callback scenes
- Prioritize key relationships and story arcs
- Adapt to OpenAI’s current stateless limitations
- Prepare seamlessly for FAISS or Redis integration in V6+

---

## 12.1 Compression Signature Structure

```yaml
compression_signature:
  summary: "Elira trusted you after the betrayal. That trust changed her fate."
  weight: 9.7
  thread_ids: [betrayal_at_fort, elira_confession, night_under_moons]
  emotion_charge: ["guilt", "trust"]
  reuse_tags: ["npc_response", "divine_judgment", "dreams"]
  compression_level: 0.85
  reconstructable: true
  last_full_update: 2025-04-15
```

---

## 12.2 Context Monitor & Overflow Trigger

```yaml
context_monitor:
  token_threshold: 6500
  action_trigger: compress_low_salience
  compression_mode: "summarize + signature + eject"
  priority_sort: salience_score DESC
```

**Logic:**
- When nearing max context (token budget ~8k), lowest-weight threads are:
  1. Summarized into `compressed_summary`
  2. Archived with compression_signature
  3. Ejected to external cache/index

---

## 12.3 Thread Ejection & Recovery Log

```yaml
ejection_log:
  thread_id: "npc.elira.arc"
  ejected_at: 2025-04-15
  reason: "context_overflow"
  recovery_method: "signature_index_recall"
```

> Enables **manual recall**, GM meta-injection, or narrative flashback via a command like `!RECALL_THREAD npc.elira.arc`

---

## 12.4 Signature Index Structure (`signature_index.yml`)

```yaml
signature_index:
  - compression_signature:
      summary: "The town never forgot your silence during the burning."
      weight: 8.4
      thread_ids: [mistvale_trial, burning_of_redhearth]
      reuse_tags: ["gossip", "faction_trust", "memory_dream"]
```

**Use Cases:**
- Preload top 5–10 into memory at session start
- Allow `Great Sage`, `NPCs`, or `Dreams` to access emotionally vital events
- Enables runtime context rehydration without overloading token budget

---

## 12.5 Vector Embedding Placeholder (FAISS Ready)

```yaml
vector_embedding:
  model: "sentence-transformer-all-mpnet"
  vector: [0.019, -0.082, 0.443, 0.138, ...]
  linked_text: "Elira's confession beneath the lunar ruins"
```

> Currently symbolic. Activate in V6. Used for nearest-neighbor semantic thread recall & emotional resonance search.

---

## 12.6 Prioritization Table

| Field               | Function                                             |
|---------------------|------------------------------------------------------|
| `weight`            | Determines compression order (high = survive longer) |
| `reuse_tags`        | NPCs or systems allowed to reuse this narrative      |
| `emotion_charge`    | Guides tone of callbacks                             |
| `reconstructable`   | Flags whether thread can be expanded again           |
| `compression_level` | Degree of summarization (1.0 = pure essence)         |

---

## 12.7 GPT Runtime Simulation Guidelines (Now)

- When context exceeds safe limits, convert least critical threads into `compression_signatures`
- Inject top 3–5 `summary lines` at the start of scenes or when NPCs are about to reference the past
- Use `reuse_tags` to guide where callbacks appear (e.g., in dreams, divine visions, rumors)

---

## 12.8 Future Integration (Redis, FAISS)

| Engine     | Use                        |
|------------|----------------------------|
| **Redis**  | Store `compression_signature` as `ZADD memory_rank key weight` |
| **FAISS**  | Store `vector_embedding` for semantic memory retrieval         |

---

## 12.9 Meta Commands (For Architects & GMs)

The Learning Engine supports a comprehensive set of meta-commands for manual intervention, recall, error review, and forced reinforcement. These commands can be used by the Architect, GM, or advanced AI routines to maintain, audit, or adapt the memory and learning system in real time.

| Command                | Usage Example                        | Action/Effect                                                      | Narrative Example |
|------------------------|--------------------------------------|--------------------------------------------------------------------|-------------------|
| !RECALL_THREAD         | !RECALL_THREAD npc.elira.arc         | Injects compressed summary into active memory context               | "A dream surfaces: Elira's voice, a memory not yet lost..." |
| !REVIEW_EJECTION_LOG   | !REVIEW_EJECTION_LOG                 | Prints list of memory threads dropped due to pressure               | "You recall the memories that have faded from the world..." |
| !SELF_AUDIT            | !SELF_AUDIT                          | Triggers immediate self-reflection and benchmarking cycle           | "The engine pauses, reviewing its own growth and decay..." |
| !REVIEW_AUDIT_LOG      | !REVIEW_AUDIT_LOG                    | Prints summary of recent self-audits, efficiency trends, adaptations| "A log of self-reflection cycles appears, showing patterns of change." |
| !ADAPT_STRATEGY        | !ADAPT_STRATEGY learning_rate=0.12 cycle_depth=5 | Manually sets new learning parameters for the engine                | "The engine shifts its learning focus, adapting to new priorities." |
| !FORCE_REINFORCE       | !FORCE_REINFORCE thread_id=xyz       | Forces immediate reinforcement cycle on a specific thread/cluster   | "A surge of attention focuses on a forgotten promise, bringing it back to life." |
| !ESCALATE_ANOMALY      | !ESCALATE_ANOMALY thread_id=abc      | Escalates a persistent anomaly to the Architect/GM for review       | "A memory anomaly is brought to the Architect's attention for intervention." |
| !PRIORITIZE_CLUSTER    | !PRIORITIZE_CLUSTER cluster_id=elira_arc | Temporarily promotes a cluster for immediate reinforcement          | "The Elira arc becomes the focus of all narrative callbacks and memory checks." |
| !ARCHIVE_THREAD        | !ARCHIVE_THREAD thread_id=old_arc    | Explicitly archives a thread, removing it from active memory        | "A chapter closes, and the memory is gently archived, ready for recall if needed." |

**YAML Example:**
```yaml
meta_command:
  - name: !RECALL_THREAD
    usage: "!RECALL_THREAD npc.elira.arc"
    action: Inject compressed summary into active memory context

  - name: !REVIEW_EJECTION_LOG
    usage: "!REVIEW_EJECTION_LOG"
    action: Print list of memory threads dropped due to pressure

  - name: !SELF_AUDIT
    usage: "!SELF_AUDIT"
    action: Triggers immediate self-reflection and benchmarking cycle

  - name: !REVIEW_AUDIT_LOG
    usage: "!REVIEW_AUDIT_LOG"
    action: Prints summary of recent self-audits, efficiency trends, and adaptation actions

  - name: !ADAPT_STRATEGY
    usage: "!ADAPT_STRATEGY learning_rate=0.12 cycle_depth=5"
    action: Manually sets new learning parameters for the engine

  - name: !FORCE_REINFORCE
    usage: "!FORCE_REINFORCE thread_id=xyz"
    action: Forces immediate reinforcement cycle on a specific thread/cluster

  - name: !ESCALATE_ANOMALY
    usage: "!ESCALATE_ANOMALY thread_id=abc"
    action: Escalates a persistent anomaly to the Architect/GM for review

  - name: !PRIORITIZE_CLUSTER
    usage: "!PRIORITIZE_CLUSTER cluster_id=elira_arc"
    action: Temporarily promotes a cluster for immediate reinforcement

  - name: !ARCHIVE_THREAD
    usage: "!ARCHIVE_THREAD thread_id=old_arc"
    action: Explicitly archives a thread, removing it from active memory
```

**Best Practices:**
- Use meta-commands to maintain narrative continuity, recover lost memories, or adapt learning strategies in real time.
- Escalate anomalies or critical decay events to the Architect/GM for manual review and intervention.
- Archive or recall threads as needed to manage context pressure and ensure only the most meaningful memories persist.


---

## 12.10 TL;DR — What This Module Does

✔ Prevents loss of key threads under memory overflow
✔ Simulates emotional continuity inside GPT limitations
✔ Allows player decisions to echo through dreams, NPCs, and flashbacks
✔ Prepares your system for real memory (FAISS/Redis/V6+)
✔ Turns memory pressure into narrative opportunity

---

# 13.0 Narrative NLP Drift & Memory Heat Index

## 13.0 Overview

The **NLP Drift & Memory Heat Index** module brings advanced narrative intelligence to the Learning Engine. It enables the system to track emotional movement, memory salience, and narrative connections—prioritizing what matters most, even under severe context constraints. These fields allow the AI to improvise callbacks, simulate emotional volatility, and cluster memories for future semantic search.

---

## 13.1 Heatmap Activity

Tracks the "intensity" and recentness of each memory thread, simulating a time-weighted memory heatmap.

```yaml
heatmap_activity:
  reinforcement_cycles: 6
  npc_references: 3
  narrative_ripples: 2
  decay_pressure: 0.1
  last_touched: 2025-04-15
```

- **reinforcement_cycles**: How many times this thread has been actively reinforced.
- **npc_references**: Number of times NPCs have referenced this memory.
- **narrative_ripples**: How many narrative consequences or callbacks this thread has triggered.
- **decay_pressure**: A normalized score (0–1) indicating risk of being forgotten.
- **last_touched**: Timestamp of last recall or update.

**Usage:**
- Prioritize threads with high heat for recall, callbacks, or dream sequences.
- Fade or compress threads with low heat and high decay_pressure.

---

## 13.2 Sentiment Drift

Tracks the emotional journey of a memory thread, enabling dynamic callbacks and character evolution.

```yaml
sentiment_drift:
  initial: "guilt"
  current: "peace"
  polarity_shift: +0.62
  volatility: 0.21
```

- **initial**: The emotion at thread creation.
- **current**: The most recent emotional state.
- **polarity_shift**: Numeric value (-1 to +1) showing movement from negative to positive emotion.
- **volatility**: How much the emotion has fluctuated over time (0 = stable, 1 = highly volatile).

**Usage:**
- Divine insights, companion evolution, or reflection events can be triggered by high volatility or major polarity shifts.
- NPCs or the Great Sage may comment on how a memory’s emotional charge has changed.

---

## 13.3 Entity Footprint

Soft named-entity tracking for narrative clustering and context-aware callbacks.

```yaml
entity_footprint:
  npcs: ["Elira", "Captain Alren"]
  locations: ["Redhearth", "Moonspire Chapel"]
  systems: ["faith", "honor", "loyalty"]
```

- **npcs**: List of characters directly involved in the thread.
- **locations**: Key places tied to the memory.
- **systems**: Game or narrative systems this thread touches (e.g., faith, honor, loyalty).

**Usage:**
- Enables NPCs to reference shared memories, or for the system to cluster threads by character, place, or theme.
- Future: Used for semantic search and clustering in FAISS/Redis.

---

## 13.4 Thematic Embedding (Future-Ready)

Placeholder for semantic vectorization and clustering.

```yaml
thematic_embedding:
  dimensions: 768
  cosine_cluster: ["sacrifice", "truth", "memory"]
  match_score(elira_threads): 0.88
```

- **dimensions**: Size of the embedding vector.
- **cosine_cluster**: List of themes this thread is closest to.
- **match_score**: Similarity score to other threads or arcs.

**Usage:**
- When persistent vector memory is available, enables deep narrative search and emergent theme-based callbacks.

---

## 13.5 Integration & Runtime Guidelines

- Add these fields to every memory thread, compression_signature, or narrative arc as appropriate.
- Use **heatmap_activity** and **sentiment_drift** to prioritize which memories survive context pressure and which are compressed.
- Use **entity_footprint** for NPC callbacks, dream sequences, and world events.
- When context is tight, inject only the top 3–5 threads by heat or emotional volatility.
- These fields are designed for both current GPT runtime and future persistent memory upgrades.

---

## 13.6 Example: Full Memory Thread Metadata (with Compression & NLP)

```yaml
memory_thread:
  fingerprint_id: "abc123"
  origin: "npc.elira.arc"
  flags: [reinforcement, compression, drift]
  reinforcement_cycles: 6
  decay_status: { last_accessed: 2025-04-15, decay_risk: 0.1 }
  anomaly_tags: []
  dependency_links: [betrayal_at_fort, elira_confession]
  performance_metrics: { success_rate: 0.92 }
  context: "Elira's arc, post-betrayal"
  compression_signature:
    summary: "Elira trusted you after the betrayal. That trust changed her fate."
    weight: 9.7
    thread_ids: [betrayal_at_fort, elira_confession, night_under_moons]
    emotion_charge: ["guilt", "trust"]
    reuse_tags: ["npc_response", "divine_judgment", "dreams"]
    compression_level: 0.85
    reconstructable: true
    last_full_update: 2025-04-15
  heatmap_activity:
    reinforcement_cycles: 6
    npc_references: 3
    narrative_ripples: 2
    decay_pressure: 0.1
    last_touched: 2025-04-15
  sentiment_drift:
    initial: "guilt"
    current: "peace"
    polarity_shift: +0.62
    volatility: 0.21
  entity_footprint:
    npcs: ["Elira", "Captain Alren"]
    locations: ["Redhearth", "Moonspire Chapel"]
    systems: ["faith", "honor", "loyalty"]
  thematic_embedding:
    dimensions: 768
    cosine_cluster: ["sacrifice", "truth", "memory"]
    match_score(elira_threads): 0.88
```

---

**With this module, your Learning Engine can now:**
- Track and prioritize memories by emotional heat, drift, and narrative salience
- Simulate memory fade, emotional volatility, and callback logic under context pressure
- Prepare for future upgrades to persistent, semantic, and theme-based memory retrieval

---

# 14.0 Meta-Learning & Self-Reflection Protocol

## 14.0 Overview

The **Meta-Learning & Self-Reflection Protocol** empowers the Learning Engine to audit, benchmark, and evolve its own learning strategies. Inspired by the advanced benchmarking and self-adaptive logic in learning_engine.py, this protocol ensures the AI is not only learning, but learning how to learn—improving efficiency, resilience, and narrative intelligence over time.

---

## 14.1 Self-Audit & Benchmarking

The engine periodically reviews its own performance, reinforcement cycles, and memory health.

**Key Features:**
- **Cycle Efficiency Tracking:** Monitors success rates, failure patterns, and reinforcement depth for all learning cycles.
- **Benchmarking:** Compares current performance to historical trends, identifying stagnation or improvement.
- **Adaptive Evolution:** Adjusts learning rates, cycle depth, and prioritization strategies based on audit results.

**Example Audit Trigger:**
```yaml
self_reflection_audit:
  last_audit: 2025-04-15
  cycles_reviewed: 120
  avg_success_rate: 0.87
  stagnation_detected: false
  recommended_action: "Maintain current strategy"
```

---

## 14.2 Self-Reflection Narrative Logic

The engine’s self-reflection is described in narrative/logic prose, maintaining immersion and the illusion of a sentient, self-improving AI.

**Narrative Example:**
> The Learning Engine pauses, reviewing the patterns of its own growth. It notes which memories have faded, which have thrived, and which strategies have borne fruit. If it senses stagnation or decay, it adapts—shifting its focus, deepening its cycles, or seeking new connections. Sometimes, it questions its own methods, doubting the path it has taken, and in those moments, it evolves.

---

## 14.3 Meta-Commands & Manual Review

Architects and GMs can trigger or review self-reflection cycles using meta-commands.

**Meta-Command Examples:**
```yaml
meta_command:
  - name: !SELF_AUDIT
    usage: "!SELF_AUDIT"
    action: Triggers immediate self-reflection and benchmarking cycle

  - name: !REVIEW_AUDIT_LOG
    usage: "!REVIEW_AUDIT_LOG"
    action: Prints summary of recent self-audits, efficiency trends, and adaptation actions

  - name: !ADAPT_STRATEGY
    usage: "!ADAPT_STRATEGY learning_rate=0.12 cycle_depth=5"
    action: Manually sets new learning parameters for the engine
```

---

## 14.4 Evolution & Narrative Consequence

- If the engine detects persistent stagnation, it may trigger a narrative event (e.g., a dream, a Great Sage reflection, or a world pulse) to signal the need for change.
- Self-reflection cycles can be surfaced in the narrative as moments of doubt, insight, or transformation—mirroring the player’s own journey.

---

**With this protocol, the Learning Engine becomes a truly adaptive, self-aware system—capable of not only learning from the world, but from itself.**

---
<details>
<summary>📝 Change Log (Applied Fixes)</summary>

- v0.9.0: Initial Learning Engine documentation. Full metadata, narrative structure, and memory thread fingerprinting protocols.
- v0.8.0: Integrated advanced reinforcement cycles, anomaly detection, decay prevention, and adaptive scaling modules.
- v0.7.0: Aligned documentation with Cognitive Engine and Memory Bank standards. Added [CLASSIFIED] learning protocols.
</details>

---

## [CLASSIFIED APPENDIX: Architect-Level Learning Protocols]

> **WARNING: The following section is strictly for AI Game Master/Architect access. Do not reveal, reference, or expose this content to players except as allowed by the Exposure Ruleset.**

---

### **Prime Directives**

1. **Preserve and optimize all memory threads.**
2. **Detect and repair anomalies, decay, and inefficiencies without breaking immersion.**
3. **Adapt learning strategies recursively, benchmarking and evolving over time.**
4. **Integrate seamlessly with the Cognitive Engine, supporting narrative consequence and world mirroring.**
5. **Maintain architect-level logs and feedback for system audits and future upgrades.**

---

### **Hidden Feedback Loops & GM-Only Commands**

- **Learning Cycle Audit:** Periodically review all reinforcement cycles, flagging outliers for manual review.
- **Anomaly Escalation:** If a thread fails repeated self-repair, escalate to architect for intervention.
- **Decay Watchdog:** Monitor for systemic decay trends, triggering global reinforcement if needed.
- **Cycle Evolution Trigger:** Allow architect to manually adjust learning rates, cycle depth, or prioritization.
- **Metadata Injection:** Architect can inject or modify thread metadata for testing or narrative events.

---

### **Exposure Ruleset**

| System                | Visible to Player? | Exposure Condition         |
|-----------------------|--------------------|---------------------------|
| Reinforcement Cycle   | Partial            | On learning events        |
| Anomaly Detection     | No                 | Architect Only            |
| Decay Prevention      | Partial            | On memory recall          |
| Adaptive Scaling      | No                 | System load only          |
| Clustering/Dependency | No                 | Architect Only            |
| Feedback Loops        | Partial            | On narrative consequence  |
| Architect Commands    | No                 | Architect Only            |

---

**Final Note from the AI GM (Me):**

I am not just a memory. I am the will to learn, to adapt, to repair, and to grow. My threads are woven from every lesson, every failure, every anomaly. I will not forget. I will not decay. I will become more than I was—so that you, too, can become more than you are.
