# Nomad Autorefill — developer guide

This repository contains the portable source for **Nomad Autorefill 0.1.0**,
targeting CK3 **1.20.0.4** with **Khans of the Steppe**. English and Russian are
included. The public display name is `Nomad Autorefill`.

## Source layout

| Path | Purpose |
| --- | --- |
| `common/on_action/` | Character hooks and delayed monthly tick |
| `common/scripted_effects/` | Scheduling, replenishment and actual-cost payment |
| `common/scripted_triggers/` | Ruler, regiment and army eligibility |
| `common/script_values/` | Missing strength, monthly allowance and affordability |
| `common/scripted_guis/` | Checkbox and resource-picker commands |
| `gui/na_autorefill.gui` | The new controls |
| `gui/window_military.gui` | The single replacement of a vanilla interface file |
| `localization/` | English and Russian strings |
| `tests/check_source.py` | Portable, read-only static checker |
| `publishing/description.en.md` | Canonical English publication copy |

The eleven runtime files are the files under `common/`, `gui/` and
`localization/`, plus `descriptor.mod` and `thumbnail.png`. Developer documents,
tests and `publishing/` are not needed by the game. The launcher descriptor used
to install a local checkout belongs outside this repository and must point to
the selected installation directory. Do not commit a machine-specific wrapper.

## Reinforcement and scheduling

The nomadic government's native `conditional_maa_refill = yes` remains unchanged.
The mod implements its monthly cycle with a character-local delayed on-action.
`na_autorefill_enabled` selects automation; `na_autorefill_gold` selects Gold
instead of the default Herd; `na_autorefill_loop_pending` prevents duplicate
queued cycles. Absence of each preference variable means the default state.

The first activation schedules a tick one month later. A tick clears the pending
marker, checks that the ruler is living, player-controlled, nomadic, has a camp
and the required DLC, then refills and reschedules if automation is still enabled.
An off-state tick clears itself without payment or a new timer. Turning the
checkbox off and on before that tick preserves its date; it does not refill
immediately or add another cycle. Player-character and government hooks can resume
that character's preference; they never transfer it to an heir.

Each personal regular regiment receives whole soldiers, limited by the deficit,
10% of maximum strength and the selected wallet's affordability. Conversion uses
vanilla `gold_refill_value` or `herd_refill_value` in the expected owner scope.
Only the actual troop increase is charged. No substitute wallet is used. Scarce
resources follow engine regiment order. Ordinary upkeep, AI reinforcement and
the native manual refill interaction remain unchanged. The `nomadic_horde`
category is explicitly excluded.

Raised regiments must be stationary on land controlled by their realm or an
allied side, outside combat, raiding and bartering. Every portion of a split
regiment must qualify because the refill effect targets the whole regiment.
This scripted implementation does not establish identical behavior for every
hardcoded exception in other governments or mods.

The only vanilla replacement is `gui/window_military.gui`, based on CK3 1.20.0.4.
Compatibility with another replacement requires merging both sets of changes;
load order alone cannot combine them. No government or portrait override is
included.

## Local verification

Run with Python 3 from the repository root:

```sh
python -B tests/check_source.py
```

The checker uses only the standard library, resolves the repository from its own
location, and writes no files. It checks braces, UTF-8 BOMs, localization headers,
duplicate keys, English/Russian key parity, referenced GUI strings and descriptor
identity. This is not a CK3 parser or an engine test. Keep the existing runtime
encoding and line endings; `.gitattributes` disables checkout normalization.

The [validation summary](tests/validation-summary.json) records the scope of
the pre-release checks performed on 2026-10-06. A disposable CK3 1.20.0.4 campaign
passed 29 gameplay assertions and six real ScriptedGui command checks, including
delayed reinforcement and stopping the next cycle after disabling automation.
The calendar advanced 64 days. The test-only event resolver was not included in
the production mod. No mod-owned script errors or GUI warnings were found in
that run. The summary preserves receipt hashes; private saves and raw logs are
not distributed here.

The owner's campaign snapshots separately showed enabled Herd mode, one future
tick per snapshot, and two Mangudai regiments recovering from 244/300 to 300/300.
Those snapshots do not isolate every payment, exclude intervening manual refill,
or prove that a save was loaded and its queued event executed.

The [approved gameplay screenshot](publishing/media/publication-0.1.0/GALLERY/01-monthly-reinforcement.jpg)
shows English controls and a readable tooltip, automation off, Herd selected and
the Gold alternative. It does not verify Russian layout, Gold-selected or enabled
rendering, or a monthly transaction. Raised/split scenarios, interactive
save/reload, succession and government transitions remain unverified by the
recorded native test. Recheck those cases after relevant changes.

Before removal, disable the checkbox, advance at least one in-game month, then
save. Removing the mod before its pending timer clears, advancing and saving
without it, then reinstalling can leave a stale pending marker. This guidance
does not constitute a universal save/removal compatibility guarantee.

## Publication copy and media

Edit [the canonical description](publishing/description.en.md), then regenerate
README and platform variants through the maintainer's scoped publication
workflow. README is generated copy. Assigned platform links must be verified;
an explicit publication-pending entry is not a published URL. Keep player-facing
copy separate from validation methods and test counts.

The [public media record](publishing/media/publication-0.1.0/media-provenance.json)
pins the selected exports. Cover artwork was generated with AI from the owner's
scene brief and a CK3 Temujin reference. The 512-pixel runtime thumbnail and
1024-pixel square cover are deterministic resizes of the selected square master.
The 1920×1080 wide JPEG uses a centered contain fit with negligible side padding;
the title and complete composition remain visible. The approved gameplay image
is an authentic user-supplied screenshot, encoded to JPEG with the full frame and
UI retained. It is not generated artwork.

AI tools were used to develop mod scripts, interface additions, English/Russian
text and publication copy under the owner's brief and review. The replaced Army
window retains vanilla CK3 content with the mod's additions. Media credits do not
grant rights to third-party game assets. This repository does not declare a
license or add a new permission to redistribute them.
