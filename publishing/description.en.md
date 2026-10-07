# Nomad Autorefill

## At a glance

- 🟢 **Version 0.1.1** · Targets CK3 **1.20.0.4**.
- 🟢 **Standalone mod. Requires Khans of the Steppe.**
- 🟢 **Optional monthly reinforcement for your nomadic Men-at-Arms, paid with Herd or Gold.**
- 🟢 **Languages:** English, French, German, Japanese, Korean, Polish, Russian, Simplified Chinese and Spanish.
- 🔴 **Applies only to your personal, regular Men-at-Arms.** AI rulers keep their normal reinforcement rules.
- 🔴 **Changes the Army window.** Other mods replacing the same window require a compatibility patch.

## Keep the horde ready

Let your regiments recover over time without repeatedly opening the manual reinforcement interaction. Choose the resource you want to spend, then decide when automatic reinforcement should run.

## Monthly reinforcement, under your control

The Army window gains a **Monthly reinforcement** checkbox and a **Pay with: Herd / Gold** picker. Automation is off by default, with Herd selected.

When enabled, each eligible regiment recovers up to **10% of its maximum strength per month**, limited by its missing soldiers and the selected resource. The first activation schedules reinforcement one month later. Turning automation off and on before a pending monthly tick keeps that scheduled date; it never grants an immediate refill or creates an extra cycle. Only whole soldiers are restored, and you pay only for the soldiers actually added.

Costs use the normal nomadic reinforcement conversion rates, including their applicable Martial, difficulty and Gold-perk modifiers. If resources are scarce, fewer soldiers return. The mod never switches to the other resource automatically. Regular army upkeep remains unchanged.

Unraised regiments can refill. Raised regiments must be stationary on land controlled by your realm or an allied side, outside combat, raiding and bartering. If a regiment is split between armies, every part must meet these conditions.

Switching the checkbox off stops future automatic reinforcement and its payments. **Manual reinforcement remains available** whether automation is on or off.

## Getting started

1. Enable Nomad Autorefill and play a nomadic ruler with Khans of the Steppe.
2. Open the **Army** window.
3. Choose **Herd** or **Gold**, then enable **Monthly reinforcement**.
4. Keep the selected resource available. Eligible regiments begin refilling after one month.

## Compatibility and load order

No other mod is required. The feature is available to player-controlled nomadic rulers with a camp and the Khans of the Steppe expansion.

Nomad Autorefill replaces `gui/window_military.gui`. Another mod replacing that file can overwrite these controls or lose its own changes. Such combinations need a patch that includes both sets of changes; load order alone does not combine them.

The mod does not change AI reinforcement, levies, mercenaries or special troops.

## Saves and known limits

The feature can be enabled during an existing campaign. Preferences belong to each ruler and are saved with the campaign. A ruler without saved preferences starts with automation off and Herd selected; a successor does not inherit the previous ruler's choice. Returning to a ruler with saved preferences restores that ruler's choice.

Automatic reinforcement only operates while that ruler is player-controlled and nomadic. Changing government or leaving that character pauses their automation.

Before removing the mod, switch **Monthly reinforcement** off, advance at least **one in-game month**, then save. Remove the mod after saving so its pending timer has time to clear. Removing it before this cleanup, advancing and saving the campaign without it, then reinstalling can leave automation waiting on stale saved timer state.

Removing the mod removes its Army-window controls. Soldiers already restored and resources already spent are not rolled back.

## Feedback and support

For a reinforcement problem, include your CK3 version, other active mods, selected payment resource, regiment strength before and after a monthly tick, and whether the regiment was raised, moving or in combat.

- [Report an issue on GitHub](https://github.com/G4VV4KH/-CK3-Nomad-Autorefill/issues)
- Email: g4vv4kh@gmail.com

### [Want to support my work? Donate on Ko-fi 💛](https://ko-fi.com/g4vv4kh)

## Find this mod elsewhere

- [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3814793283)
- [Paradox Mods](https://mods.paradoxplaza.com/mods/162238/Any)
- [Nexus Mods](https://www.nexusmods.com/crusaderkings3/mods/409)
- [GitHub](https://github.com/G4VV4KH/-CK3-Nomad-Autorefill)

## My other mods

- [Parley: The Negotiating Table](https://steamcommunity.com/sharedfiles/filedetails/?id=3811090081) — negotiate diplomatic agreements.
- [Marriage Calculation Assistant](https://steamcommunity.com/sharedfiles/filedetails/?id=3811100163) — compare and sort marriage candidates.
- [Your Own Hegemony](https://steamcommunity.com/sharedfiles/filedetails/?id=3811201582) — found a custom hegemony.
- [Vassalization Extended](https://steamcommunity.com/sharedfiles/filedetails/?id=3813943691) — choose Forced Vassalization terms without a county limit.
- [Court Automation](https://steamcommunity.com/sharedfiles/filedetails/?id=3814028714) — automate court positions and recruit courtiers or knights.

These mods are optional.

## Credits

Cover artwork was generated with AI.
