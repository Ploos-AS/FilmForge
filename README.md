# FilmForge

AI-assisted filmmaking pipeline for story development, world building, screenplay, shot planning, generative media, continuity review, audio and final assembly.

## Current milestone — M2.2 Visual Development

FilmForge has moved beyond the M0 architecture proof. The current reference production is **Dead Channel**, an original 18-minute science-fiction short used to prove a reproducible AI-assisted film pipeline end to end.

Dead Channel currently has frozen universe rules, stable entities, an eight-scene screenplay plan, screenplay draft 0.1, a final-shot planning target, an 18:00 timed animatic coverage plan, continuity rules, asset registry, provider-neutral prompt templates, provenance records and its first approved visual-development board.

### Production pipeline

```text
concept / Universe Foundry
  -> canon + stable entity IDs
  -> screenplay
  -> scene breakdown
  -> timed animatic coverage
  -> final shot manifest
  -> visual development
  -> approved / locked reference assets
  -> provider-neutral prompts
  -> image / video / voice / music / SFX providers
  -> provenance + continuity review
  -> rough cut
  -> selective regeneration
  -> final assembly
```

## Design principles

- Provider-agnostic: canon and production data are not tied to one AI vendor.
- Canon before prompts: characters, locations, props and style use stable IDs.
- Reproducible production: prompts, seeds, references, model metadata and output hashes can be tracked per generation.
- Human-directed: generated candidates never become canon automatically.
- Regeneration-first: every shot is independently replaceable.
- Continuity-first: approved reference assets and immutable scene rules constrain generation.
- Deterministic UI: critical readable interfaces are composited rather than trusted to image/video generators.
- StoryForge-friendly: structured stories can be imported without making FilmForge depend on StoryForge.
- Open formats first: YAML/JSON/Markdown plus standard audiovisual interchange wherever practical.

## Dead Channel

The first reference film is built under `examples/dead-channel/`.

Key production material includes:

- `canon/` — frozen universe rules and entities.
- `film/scenes.yaml` — eight scenes totaling exactly 1080 seconds.
- `film/screenplay.md` — screenplay draft 0.1.
- `film/shot-manifest.yaml` — final-shot planning target.
- `film/animatic-coverage.yaml` — 43 coarse coverage shots totaling 18:00.
- `assets/` — asset registry, continuity policy and prompt template.
- `visual-dev/` — Sera, Kestrel, prop and look briefs plus candidate/approval tracking.
- `visual-dev/dead-channel-visual-board-v1.png` — approved M2.2 visual direction board.

The visual board is an approved direction reference, **not** a canonical master for individual character, environment or prop assets. Those are selected separately from dedicated candidate sets.

## Asset maturity

Assets use two independent concepts:

- `required: true|false` — whether production is blocked until the asset is ready.
- `status: planned|candidate|approved|locked` — current maturity.

Required assets are generation-ready only when `approved` or `locked`.

## CLI

Current commands:

```text
filmforge validate <project>
filmforge plan <project>
filmforge foundry <foundry>
filmforge coverage <coverage>
filmforge assets <registry>
```

## Next

M2.2 continues with dedicated candidate generation and selection for Sera, Kestrel and hero props. The first major visual lock target is `sera-face-v1`, followed by workwear and turnaround references.

## License

Software: MIT unless otherwise noted.
Documentation and creative reference material: see per-directory licensing before publication.
