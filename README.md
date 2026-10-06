# FilmForge

AI-assisted filmmaking pipeline for story development, world building, screenplay, shot planning, generative media, continuity review, audio and final assembly.

## M0 goals

FilmForge M0 defines the production model and proves the full path from a story concept to a machine-readable film plan.

The first reference production targets an original 15–20 minute science-fiction short designed as the entry point to a larger reusable universe.

### M0 pipeline

```text
concept
  -> universe bible
  -> characters / factions / locations / technology
  -> screenplay
  -> scene breakdown
  -> shot list
  -> generation prompts
  -> image / video / voice / music / SFX providers
  -> continuity review
  -> rough cut
  -> selective regeneration
  -> final assembly
```

## Design principles

- Provider-agnostic: no story data is tied to one AI vendor.
- Canon before prompts: characters, locations, props and style have stable IDs and reusable reference data.
- Reproducible production: prompts, seeds, references, model metadata and outputs can be tracked per shot.
- Human-directed: AI assists writing, planning, generation and QA; editorial decisions remain explicit.
- Regeneration-first: every shot is independently replaceable.
- StoryForge-friendly: structured stories can be imported without making FilmForge depend on StoryForge.
- Open formats first: YAML/JSON/Markdown plus standard audiovisual interchange wherever practical.

## Repository layout

```text
docs/
  architecture.md
  m0.md
schema/
  filmforge-project.schema.yaml
examples/
  first-contact/
    project.yaml
    universe/
      bible.md
    screenplay/
      outline.md
```

## Status

M0 — foundation and reference production.

## License

Software: MIT unless otherwise noted.
Documentation and creative reference material: see per-directory licensing before publication.
