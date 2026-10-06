# Architecture

FilmForge separates creative canon from generated media.

## Layers

### 1. Canon

Stable facts about the production:

- universe
- timeline
- factions
- characters
- locations
- props
- technology
- cinematography/style rules

Canon entries have stable IDs. Prompts reference IDs rather than restating mutable descriptions ad hoc.

### 2. Narrative

Screenplay, scene graph, dialogue, dramatic beats and continuity state.

### 3. Shot plan

Each shot records:

- shot ID
- scene ID
- intended duration
- subjects
- action
- dialogue
- framing / lens / camera movement
- lighting and mood
- continuity dependencies
- required references

### 4. Generation

Provider-neutral requests are compiled into provider-specific jobs.

A generation record should retain model/provider, parameters, seed when available, reference assets, prompt revision and output provenance.

### 5. Review

Automated and human review can flag:

- identity drift
- wardrobe/prop inconsistency
- location inconsistency
- broken eyelines or screen direction
- dialogue mismatch
- temporal discontinuity
- visual-style drift
- technical defects

### 6. Assembly

Selected takes plus audio, captions and timing form a reproducible rough cut. Final finishing may happen in external tools.

## Relationship to StoryForge

StoryForge may supply structured narrative material. FilmForge owns film-specific decomposition, shot planning, media generation, continuity and assembly.
