# M2.1 Asset Lock

A generated shot is never the source of truth for identity or design.

## Resolution order

1. Shot references canon entity IDs.
2. Entity IDs resolve to locked asset IDs.
3. Scene continuity state adds mutable state such as emotion or damage.
4. Prompt template combines canon, shot intent, camera language and exclusions.
5. Provider adapter translates the provider-neutral request.
6. Generation record stores the exact provider/model/seed/references and output hash.
7. Continuity review either accepts the take or rejects it.

## Asset maturity

- **planned**: specification exists but no canonical visual asset has been approved.
- **candidate**: one or more generated/designed references exist.
- **required-reference**: production shots must reference the approved asset.
- **locked**: changing the asset requires an explicit canon/production decision.

## UI rule

Readable interface text is deterministic artwork. Video/image generation may provide surfaces and lighting, but final UI text and critical diagrams are composited from the UI kit.

## Provider independence

Canon must never contain provider-specific prompt syntax. Provider adapters may add syntax or parameters, but provenance records preserve exactly what was sent.
