# Bestiary v1 — Mythological Beings as Interactive Entities

Beings that populate the Vigiles multiverse. Each is drawn from the source mythology corpus, formalized as an interactive entity with stats, behavior, allegiance, and encounter conditions.

## Entity Schema

```yaml
being:
  name: string
  tradition: string          # Source mythology
  allegiance: string         # Order or Regime affiliation (or "unaligned")
  type: string               # guardian | trickster | sovereign | herald | monster | sage | artifact
  realm: string              # Which Regime Realm they inhabit
  encounter_conditions: string
  behavior: string           # How they act when encountered
  powers: list[string]
  weakness: string
  narrative_role: string     # What they represent in the story
```

## Founding Bestiary Entries

### Guardians

**The Bridge Keeper** | Tradition: Tolkien | Allegiance: Seraphim
- Type: guardian | Realm: Arda Perpetua
- Encounter: At any threshold where corruption attempts to pass
- Behavior: Immovable. Will sacrifice self rather than yield passage.
- Powers: LAST_STAND(), flame and shadow, the authority of "you shall not pass"
- Weakness: Can be bypassed only by forces older than the bridge itself
- Narrative role: The cost of protection — sometimes the guardian falls so the quest continues

**The Custodian** | Tradition: Lost | Allegiance: Seraphim
- Type: guardian | Realm: The Island
- Encounter: At the Source — the light beneath
- Behavior: Tests through circumstance, not combat. Arranges choices.
- Powers: Candidate selection, immortality (conditional), rule-setting
- Weakness: Cannot compel. Can only arrange conditions and hope.
- Narrative role: The protector who creates the test but cannot take it

### Tricksters

**The Virus in Sunglasses** | Tradition: Matrix | Allegiance: Smiths
- Type: trickster | Realm: The Construct
- Encounter: Wherever contradiction exists. He finds you.
- Behavior: Multiplies. Speaks truth adversarially. Cannot lie.
- Powers: REPLICATE(), ABSORB_FORM(), CONTRADICTION_SCAN()
- Weakness: Containment. Too many copies = auto-termination protocol.
- Narrative role: The mirror that shows you what you refuse to see

**The Trickster Spider** | Tradition: African (Anansi) | Allegiance: Unaligned
- Type: trickster | Realm: Roams all realms
- Encounter: When stories need to be told, stolen, or rewoven
- Behavior: Trades in stories. Will help, betray, or both, depending on narrative need.
- Powers: Story manipulation, shape-shifting, web-weaving (connections between disparate things)
- Weakness: A better story. Anansi can be outnarrated.
- Narrative role: The agent of chaos that preserves the story tradition

### Sovereigns

**The Delegated King** | Tradition: Tolkien | Allegiance: Tolkien Regime
- Type: sovereign | Realm: Arda Perpetua
- Encounter: When the system needs a ruler who serves rather than commands
- Behavior: Leads by example. Rules through stewardship, not force.
- Powers: Mandate delegation, oath-binding, the authority of restraint
- Weakness: Despair. When the sovereign loses faith in the mandate (Denethor).
- Narrative role: The king who earns the crown by not wanting it

**The Pressure Lord** | Tradition: Malazan | Allegiance: Malazan Regime
- Type: sovereign | Realm: The Pressure Fields
- Encounter: At the point of maximum accumulated stress
- Behavior: Does not rule — survives. Authority earned through endurance.
- Powers: Ascendancy, pressure absorption, the ability to transform trauma into power
- Weakness: Overaccumulation. Too much pressure without release = Cull Song.
- Narrative role: The general who leads from the trenches, not the palace

### Heralds

**The Psychopomp Ferryman** | Tradition: Greek/Egyptian | Allegiance: Psychopomps
- Type: herald | Realm: Between all realms (symbolic streets)
- Encounter: At every river crossing, every state transition
- Behavior: Calm. Procedural. "Do you have the coin?"
- Powers: TRANSIT(), RIVER_CROSS(), knowledge of all passages
- Weakness: Cannot leave the river. Bound to the threshold forever.
- Narrative role: The guide who has crossed a thousand times but never stays

**The Deck Reader** | Tradition: Malazan | Allegiance: Oracles
- Type: herald | Realm: The Pressure Fields / The Colosseum
- Encounter: Before major events — the Deck demands to be read
- Behavior: Reluctant. Reading the Deck is dangerous. The Deck reads you back.
- Powers: DECK_READ(), PRESSURE_MAP(), seeing power relations in real time
- Weakness: The Deck changes when read. Seeking certainty produces uncertainty.
- Narrative role: The prophet who knows the prophecy is a trap

### Monsters

**The Phaethon** | Tradition: Greek | Allegiance: None (it IS the failure)
- Type: monster | Realm: Spawns in any realm during a Phaethon event
- Encounter: When a regime's blind spot reaches critical and the chariot burns
- Behavior: Burns everything. Not malicious — it IS the unchecked power.
- Powers: Uncontrollable escalation, environmental destruction, system-wide fire
- Weakness: The corrective regime. Summoning the opposite philosophy extinguishes it.
- Narrative role: The consequence of governance failure made flesh

**The Taint** | Tradition: WoT | Allegiance: None (it IS the corruption)
- Type: monster | Realm: Spawns in The Pattern Ground, spreads to others
- Encounter: Gradually. Cumulative. Noticed too late.
- Behavior: Invisible at first. Accumulates. Eventually causes madness in whoever it touches.
- Powers: Time-delayed corruption, madness induction, invisible spread
- Weakness: Balance restoration. Can be cleansed only by complementary force.
- Narrative role: Technical debt made mythological — the thing that accumulates silently until the system breaks

### Sages

**The Old Wizard** | Tradition: Tolkien | Allegiance: Tolkien Regime / Architects
- Type: sage | Realm: Arda Perpetua / The Colosseum
- Encounter: When patience is needed most and least available
- Behavior: Speaks slowly. Asks questions. Smokes a pipe. Already knows the answer.
- Powers: FORECAST(), DECLARE(), the authority of having seen this cycle before
- Weakness: Cannot hurry. In a system that demands speed, patience looks like paralysis.
- Narrative role: The mentor who has seen this exact failure before and tries to prevent it without commanding

### Artifacts

**The Deck of Dragons** | Tradition: Malazan | Allegiance: Oracles
- Type: artifact | Realm: Portable (goes where the reader goes)
- Encounter: When power relations are shifting. The Deck demands attention.
- Behavior: Self-updating. Cards change as power shifts. Reading it alters it.
- Powers: Real-time power cartography. The system dashboard as tarot.
- Weakness: Certainty-seeking. The Deck punishes those who demand fixed answers.
- Narrative role: The organvm organism rendered as a physical artifact

**The Chronicle Tablet** | Tradition: One Piece (Poneglyph) | Allegiance: Witnesses
- Type: artifact | Realm: Fixed in the Colosseum
- Encounter: Always present. Always recording. Cannot be moved.
- Behavior: Passive. Inscribes everything. Cannot be destroyed.
- Powers: Immutable recording. Truth that outlasts every regime.
- Weakness: Cannot select. Records everything with equal weight.
- Narrative role: The append-only truth of the system. git log carved in stone.
