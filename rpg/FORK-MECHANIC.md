# The Fork Mechanic — Branching Timelines

## What Is a Fork?

Every significant event in the Vigiles multiverse creates a **decision point**. Each decision point offers multiple paths. The chosen path becomes the **canonical timeline**. The unchosen paths become **folds** — navigable alternate timelines that exist as real places in the multiverse.

## Fork YAML Schema

```yaml
fork:
  id: string               # FORK-{YYYY-MM-DD}-{NNN}
  realm: string            # Which regime realm
  timestamp: datetime
  trigger: string          # What caused the decision point
  trigger_type: string     # agon_finding | character_choice | community_vote | phaethon_warning
  paths:
    a:
      description: string
      consequence: string  # What this path would produce
    b:
      description: string
      consequence: string
    c:                     # Optional third+ paths
      description: string
      consequence: string
  chosen: string | null    # a, b, c, or null if undecided
  chosen_by: string        # play | simulation | community_vote | cosmogonist_decree
  fold_data:
    divergence_score: float | null     # 0.0 (identical) to 1.0 (completely different)
    divergence_dimensions:             # Which aspects diverged
      - dimension: string              # governance | aesthetic | structural | narrative
        magnitude: float
    regime_impact: string | null       # How this fork affected the active regime
    constitutional_candidate: boolean  # Did this fork produce a consensus candidate?
    chronicle_ref: string | null       # Link to the Chronicle entry recording this fork
```

## Fork Triggers

| Trigger Type | Example | Who Decides |
|-------------|---------|-------------|
| **Agon finding** | A regime audit reveals a critical violation with two possible responses | The Colosseum runner (code) or the active regime's philosophy (narrative) |
| **Character choice** | A Watcher being faces a dilemma that tests their Order's principles | The player (RPG) or the narrative logic (story) |
| **Community vote** | The community is asked to choose between two regime candidates | Community members (ORGAN-VI) |
| **Phaethon warning** | A regime's blind spot is manifesting — force rotation or let it play out? | The Cosmogonists (meta-governance) |

## Divergence Calculation

Divergence is computed after a path is chosen, by simulating what the unchosen paths would have produced:

```
divergence_score = weighted_sum(
    governance_delta * 0.4,    # How differently would the system be governed?
    structural_delta * 0.3,    # How differently would repos/components change?
    aesthetic_delta * 0.15,    # How differently would the narrative/art feel?
    narrative_delta * 0.15     # How differently would the story unfold?
)
```

High-divergence forks are more interesting (they reveal where philosophy truly matters). Low-divergence forks suggest the decision didn't actually matter (which is itself interesting — it means multiple philosophies converge on the same outcome, which is a Constitutional signal).

## The Multiverse Tree

Forks accumulate into a tree:

```
ROOT (Colosseum — canonical timeline)
├── FORK-2026-03-001 (Tolkien vs Malazan first audit)
│   ├── Path A: Tolkien perspective adopted → canonical
│   └── Path B: Malazan perspective adopted → Fold-001
│       ├── FORK-2026-03-002 (within Fold-001)
│       │   ├── Path A → canonical within fold
│       │   └── Path B → Fold-001-A (nested fold)
│       └── ...
├── FORK-2026-04-001 (Community regime election)
│   ├── Path A: Lynch wins → ...
│   └── Path B: JoJo wins → ...
└── ...
```

Folds can nest infinitely. The NEVERW4S liminal room provides access to deep-nested folds that represent "timelines that were rejected at every level."

## Fork as Creative Artifact

Every fork is simultaneously:
- **Data** (divergence scores feed the consensus engine)
- **Narrative** (a story about what could have been)
- **Art** (the multiverse tree is a visualizable structure)
- **Product** (interactive fiction: "explore what would have happened if...")
- **Community** (votes create forks that the community owns)
