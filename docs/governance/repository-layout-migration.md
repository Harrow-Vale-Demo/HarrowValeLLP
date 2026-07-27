# Repository Layout Migration

Implemented from [GitHub issue #2](https://github.com/f7-rage-gremlin/HarrowValeLLP/issues/2) as a one-time purpose-based refactor.

## Path mapping

| Previous path | Canonical path |
|---|---|
| `harrow-vale-skills/plugins/term-sheet-review/` | `releases/term-sheet-review/` |
| `harrow-vale-skills/README.md` | `releases/README.md` |
| `harrow-vale-skills/CONTRIBUTING.md` | `releases/CONTRIBUTING.md` |
| `assets/term-sheets/` | `assets/source/term-sheets/` |
| `assets/dd-checklist/` | `assets/source/dd-checklist/` |
| `assets/data-room-set/` | `assets/source/data-room/` |
| `DataRoomInfo/` | `assets/legacy-raw-import/` |
| `assets/DATA-ROOM-NOTES.md` | `docs/discovery/data-room-notes.md` |
| `harrow-vale-conversation-screenshots/` | `docs/discovery/conversation-screenshots/` |
| `Scenario-1-Harrow-Vale-Guide.md` | `docs/engagement/scenario-guide.md` |
| `evaluation.md` | `docs/governance/prototype-evaluation.md` |
| `notes` | `docs/discovery/client-call-notes.md` |
| `summary` | `docs/discovery/engagement-summary.md` |
| `docs/discovery/engagement-pack.md` | `docs/engagement/engagement-pack.md` |

The active plugin, harness, deliverables, demo, and presentation retained their component-owned paths.

## Contributor update

After this refactor merges, contributors with clean checkouts should run:

```powershell
git switch master
git pull --ff-only
```

Long-running branches should be rebased or merged with the new `master` before further work. Original non-Git personal folders should remain read-only until any genuinely missing work has been imported.

Active Git checkouts should be outside Google Drive or similar synchronisation folders; GitHub is the collaboration and backup layer.