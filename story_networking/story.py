# story.py
# Choose-your-own-adventure story data and helpers.
# Requirements met:
# - More immersive text
# - At least 3 levels deep for EACH start option (logs/door/call)
# - EVERY non-ending scene has exactly 3 choices (A/B/C)

from typing import Dict, Any

STORY: Dict[str, Dict[str, Any]] = {
    # LEVEL 0 (Start)
    "start": {
        "text": (
            "Cold air bites your skin as you sit up on a concrete floor. The hum of servers surrounds you—"
            "a low, steady roar like an ocean made of electricity.\n\n"
            "A single monitor glows in the dark. On the screen: 'ACCESS GRANTED'.\n"
            "A timer in the corner ticks down from 03:00.\n\n"
            "Your mouth is dry. Your memory is worse.\n"
            "What do you do?"
        ),
        "choices": [
            {"key": "A", "label": "Check the monitor logs", "next": "logs_1"},
            {"key": "B", "label": "Try the exit door", "next": "door_1"},
            {"key": "C", "label": "Call for help", "next": "call_1"},
        ],
    },

    # =========================
    # PATH A: LOGS (3+ levels)
    # =========================

    # LEVEL 1A
    "logs_1": {
        "text": (
            "You step to the monitor. The keyboard is warm, like someone used it recently.\n"
            "A black terminal window scrolls with events.\n\n"
            "One entry repeats:\n"
            "  user=shadow_admin | action=privilege_escalation | status=SUCCESS\n\n"
            "A prompt flashes:\n"
            "  'Proceed with trace? (y/n)'\n\n"
            "You feel your pulse quicken. Whatever happened here… it’s still happening."
        ),
        "choices": [
            {"key": "A", "label": "Run a trace on 'shadow_admin'", "next": "logs_2_trace"},
            {"key": "B", "label": "Search logs for the last known location", "next": "logs_2_location"},
            {"key": "C", "label": "Kill the suspicious session immediately", "next": "logs_2_kill"},
        ],
    },

    # LEVEL 2A
    "logs_2_trace": {
        "text": (
            "You hit ENTER. The trace begins.\n"
            "Lines crawl across the screen: hops, ports, internal routes.\n\n"
            "Then it stops on a result that makes your stomach drop:\n"
            "  ORIGIN: INTERNAL - FLOOR 2 - SECURITY CLOSET\n\n"
            "Somewhere above you, a door latch clicks."
        ),
        "choices": [
            {"key": "A", "label": "Hide behind the server rack", "next": "logs_3_hide"},
            {"key": "B", "label": "Lock the server room from the inside", "next": "logs_3_lock"},
            {"key": "C", "label": "Grab the USB drive plugged into the monitor", "next": "logs_3_usb"},
        ],
    },

    "logs_2_location": {
        "text": (
            "You filter the logs for anything tied to physical access.\n"
            "Badge scans. Door events. Camera pings.\n\n"
            "One entry stands out:\n"
            "  badge_id=???? | door=SERVER_ROOM | status=DENIED | time=00:02 ago\n\n"
            "Someone tried to get in. Just now.\n"
            "You hear soft footsteps outside the door, slow and careful."
        ),
        "choices": [
            {"key": "A", "label": "Turn off the monitor to hide the glow", "next": "logs_3_dark"},
            {"key": "B", "label": "Call out: 'Who's there?'", "next": "logs_3_callout"},
            {"key": "C", "label": "Open the door suddenly and confront them", "next": "logs_3_confront"},
        ],
    },

    "logs_2_kill": {
        "text": (
            "Your fingers fly. You terminate the process.\n"
            "For a second, the room feels quieter—like the building exhaled.\n\n"
            "Then the monitor flickers red:\n"
            "  ALERT: FAILSAFE TRIGGERED\n"
            "  TIMER REDUCED: 00:45\n\n"
            "A hidden speaker crackles: 'UNAUTHORIZED ACTION DETECTED.'\n"
            "You don’t have much time."
        ),
        "choices": [
            {"key": "A", "label": "Undo the kill (restore session)", "next": "logs_3_restore"},
            {"key": "B", "label": "Rip out the network cable", "next": "logs_3_unplug"},
            {"key": "C", "label": "Sprint to the door and try to escape", "next": "logs_3_run"},
        ],
    },

    # LEVEL 3A (endings)
    "logs_3_hide": {
        "text": (
            "You duck behind the nearest rack, holding your breath.\n"
            "The door opens. A flashlight beam sweeps the room.\n\n"
            "A voice, calm and close, says: 'I know you're in here.'\n"
            "The beam stops on your shoes.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "logs_3_lock": {
        "text": (
            "You slam the door lock and shove a heavy chair under the handle.\n"
            "Someone rattles the knob. Hard. Then… silence.\n\n"
            "Your monitor flashes:\n"
            "  TRACE PACKAGE READY FOR EXPORT\n\n"
            "You send it to a secure address you recognize from your own muscle memory.\n"
            "Somewhere far away, help is now on the way.\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
    "logs_3_usb": {
        "text": (
            "You yank out the USB drive. It’s labeled in neat handwriting:\n"
            "  'FOR YOU'\n\n"
            "The moment it leaves the port, the timer pauses.\n"
            "The monitor changes to a single message:\n"
            "  'Smart. Now leave.'\n\n"
            "A hidden panel clicks open near the floor.\n\n"
            "END (Neutral Ending)"
        ),
        "choices": [],
    },
    "logs_3_dark": {
        "text": (
            "You turn off the monitor. The room becomes almost completely black.\n"
            "The footsteps outside stop.\n\n"
            "After a long moment, you hear a quiet laugh.\n"
            "Then the footsteps walk away.\n\n"
            "The timer hits 00:00.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "logs_3_callout": {
        "text": (
            "You call out, voice shaky: 'Who's there?'\n\n"
            "A pause.\n"
            "Then a familiar voice answers: 'Relax. I'm here to get you out.'\n\n"
            "The door opens slowly. It's the IT manager.\n"
            "They look surprised you're awake.\n\n"
            "END (Neutral Ending)"
        ),
        "choices": [],
    },
    "logs_3_confront": {
        "text": (
            "You swing the door open.\n"
            "Nobody is there.\n\n"
            "But the hallway lights flicker and die.\n"
            "Behind you, the server room door clicks shut by itself.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "logs_3_restore": {
        "text": (
            "You restore the process. The alarm stops.\n"
            "The timer resets to 03:00.\n\n"
            "A new line appears:\n"
            "  shadow_admin: 'Good. Follow the hatch.'\n\n"
            "You notice a maintenance hatch you didn't see before.\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
    "logs_3_unplug": {
        "text": (
            "You rip out the network cable.\n"
            "Instant silence—then the emergency lights snap on.\n\n"
            "A siren screams. The door locks.\n"
            "You see a message on the monitor:\n"
            "  'Offline = contained. Contained = eliminated.'\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "logs_3_run": {
        "text": (
            "You sprint to the door and yank it open.\n"
            "The hallway is empty, lit in harsh white.\n\n"
            "You run—no plan, just instinct.\n"
            "Behind you, the timer hits zero… and nothing happens.\n\n"
            "You made it out, but you have no idea why you were spared.\n\n"
            "END (Neutral Ending)"
        ),
        "choices": [],
    },

    # =========================
    # PATH B: DOOR (3+ levels)
    # =========================

    # LEVEL 1B
    "door_1": {
        "text": (
            "You try the exit door. Locked.\n"
            "A keypad glows faintly, waiting.\n\n"
            "On the wall beside it, a laminated note reads:\n"
            "  'DO NOT ATTEMPT MORE THAN ONCE. ALARM ARMED.'\n\n"
            "You glance back at the monitor timer. Still ticking."
        ),
        "choices": [
            {"key": "A", "label": "Enter a code and hope for the best", "next": "door_2_code"},
            {"key": "B", "label": "Search the room for clues", "next": "door_2_clues"},
            {"key": "C", "label": "Try to force the door (quietly)", "next": "door_2_force"},
        ],
    },

    # LEVEL 2B
    "door_2_code": {
        "text": (
            "You hover your fingers over the keypad.\n"
            "Four digits. One chance.\n\n"
            "Your mind offers three numbers like a reflex, as if you’ve typed them before."
        ),
        "choices": [
            {"key": "A", "label": "Type 1337", "next": "door_3_1337"},
            {"key": "B", "label": "Type 0420", "next": "door_3_0420"},
            {"key": "C", "label": "Type 0000", "next": "door_3_0000"},
        ],
    },

    "door_2_clues": {
        "text": (
            "You scan the room. Under a keyboard tray, you find a sticky note folded twice.\n"
            "Inside it says:\n"
            "  'Not the obvious one. Think like a technician.'\n\n"
            "Near the floor, there’s a small panel with scratches around the edge."
        ),
        "choices": [
            {"key": "A", "label": "Try the 'obvious' code anyway (1337)", "next": "door_3_1337"},
            {"key": "B", "label": "Check the panel near the floor", "next": "door_3_panel"},
            {"key": "C", "label": "Look for a badge or ID card in the room", "next": "door_3_badge"},
        ],
    },

    "door_2_force": {
        "text": (
            "You press your shoulder into the door.\n"
            "It doesn’t move. Not even a millimeter.\n\n"
            "But the keypad flashes yellow like it noticed.\n"
            "A quiet beep repeats, getting faster.\n\n"
            "You’re not sure how many warnings you get."
        ),
        "choices": [
            {"key": "A", "label": "Stop and enter a code (1337)", "next": "door_3_1337"},
            {"key": "B", "label": "Keep forcing it", "next": "door_3_alarm"},
            {"key": "C", "label": "Back off and search for another exit", "next": "door_3_panel"},
        ],
    },

    # LEVEL 3B (endings)
    "door_3_1337": {
        "text": (
            "You type 1-3-3-7.\n"
            "The keypad pauses… then beeps green.\n"
            "The lock clicks open.\n\n"
            "You pull the door and step into the hallway.\n"
            "The air outside feels warmer, safer.\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
    "door_3_0420": {
        "text": (
            "You type 0-4-2-0.\n"
            "Red light.\n"
            "A harsh buzzer blasts and the building alarms wake up.\n\n"
            "Somewhere nearby, running footsteps answer the sound.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "door_3_0000": {
        "text": (
            "You type 0-0-0-0.\n"
            "For a second, nothing happens.\n\n"
            "Then the keypad flashes:\n"
            "  'DEFAULT ACCEPTED'\n\n"
            "The door opens like it was never locked.\n"
            "That should make you feel relieved… but it doesn’t.\n\n"
            "END (Neutral Ending)"
        ),
        "choices": [],
    },
    "door_3_panel": {
        "text": (
            "You pry the panel open.\n"
            "Behind it is a maintenance crawlspace just wide enough to squeeze through.\n\n"
            "You crawl in, scraping your elbows, and follow a faint draft of fresh air.\n"
            "After what feels like forever, you drop into a quiet hallway.\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
    "door_3_badge": {
        "text": (
            "You search the room and find a lanyard tucked behind a server.\n"
            "The badge photo is you… but the name isn’t.\n\n"
            "Before you can process that, the door handle rattles from the other side.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "door_3_alarm": {
        "text": (
            "You force the door again.\n"
            "The keypad flashes red and screams.\n"
            "A metal shutter drops over the door from the ceiling.\n\n"
            "You are trapped.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },

    # =========================
    # PATH C: CALL (3+ levels)
    # =========================

    # LEVEL 1C
    "call_1": {
        "text": (
            "You pull your phone from your pocket. It’s there, somehow.\n"
            "No signal. No service. No emergency calls.\n\n"
            "The screen does light up, though.\n"
            "One contact is pinned at the top with a star: 'ODIXCITY OPS'.\n\n"
            "Behind the server racks, you notice a maintenance hatch and a dusty wall intercom."
        ),
        "choices": [
            {"key": "A", "label": "Try the wall intercom", "next": "call_2_intercom"},
            {"key": "B", "label": "Open the maintenance hatch", "next": "call_2_hatch"},
            {"key": "C", "label": "Shout for help and listen for an answer", "next": "call_2_shout"},
        ],
    },

    # LEVEL 2C
    "call_2_intercom": {
        "text": (
            "You press the intercom button. Static crackles.\n"
            "A quiet voice answers, distorted:\n"
            "  'Say the phrase.'\n\n"
            "You have no idea what phrase they mean."
        ),
        "choices": [
            {"key": "A", "label": "Say: 'Access granted'", "next": "call_3_phrase1"},
            {"key": "B", "label": "Say: 'I need help'", "next": "call_3_phrase2"},
            {"key": "C", "label": "Say nothing and listen", "next": "call_3_silence"},
        ],
    },

    "call_2_hatch": {
        "text": (
            "You pull the hatch open. Cold air rushes up from below.\n"
            "A ladder drops into darkness.\n\n"
            "From somewhere underneath, you hear a faint tapping—like someone knocking in code.\n"
            "Tap… tap-tap… tap…"
        ),
        "choices": [
            {"key": "A", "label": "Climb down carefully", "next": "call_3_down"},
            {"key": "B", "label": "Drop a tool to test the depth", "next": "call_3_drop"},
            {"key": "C", "label": "Close it and stay in the server room", "next": "call_3_stay"},
        ],
    },

    "call_2_shout": {
        "text": (
            "You shout, voice echoing off metal:\n"
            "  'HELLO?! IS ANYONE THERE?'\n\n"
            "At first, nothing.\n"
            "Then a reply from the hallway beyond the door:\n"
            "  'Wrong move.'\n\n"
            "The door handle rattles once. Twice."
        ),
        "choices": [
            {"key": "A", "label": "Go quiet and hide", "next": "call_3_hide"},
            {"key": "B", "label": "Talk through the door calmly", "next": "call_3_talk"},
            {"key": "C", "label": "Run to the hatch and escape", "next": "call_3_escape"},
        ],
    },

    # LEVEL 3C (endings)
    "call_3_phrase1": {
        "text": (
            "You say: 'Access granted.'\n\n"
            "The intercom clicks. A hidden lock releases somewhere in the room.\n"
            "A panel near the floor opens softly.\n"
            "The voice says: 'Good. Now move.'\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
    "call_3_phrase2": {
        "text": (
            "You say: 'I need help.'\n\n"
            "The voice laughs—short, mean.\n"
            "'Not the phrase,' it says.\n"
            "The intercom dies.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "call_3_silence": {
        "text": (
            "You stay silent.\n"
            "You listen.\n"
            "The static shifts, and you catch a second voice in the background:\n"
            "  'They’re awake.'\n\n"
            "The intercom shuts off.\n\n"
            "END (Neutral Ending)"
        ),
        "choices": [],
    },
    "call_3_down": {
        "text": (
            "You climb down rung by rung.\n"
            "Halfway down, the tapping stops.\n\n"
            "At the bottom, a dim hallway stretches left and right.\n"
            "A door at the end is slightly open, spilling warm light.\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
    "call_3_drop": {
        "text": (
            "You drop a tool.\n"
            "It hits with a loud clang.\n\n"
            "The tapping turns into fast footsteps coming toward the ladder.\n"
            "Something is coming up.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "call_3_stay": {
        "text": (
            "You close the hatch.\n"
            "You tell yourself staying put is safer.\n\n"
            "The timer on the monitor hits 00:00.\n"
            "The lights shut off.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "call_3_hide": {
        "text": (
            "You hide between racks, trying to stay still.\n"
            "The door opens slowly.\n"
            "A flashlight beam cuts the dark.\n\n"
            "The beam lands on your face.\n\n"
            "END (Bad Ending)"
        ),
        "choices": [],
    },
    "call_3_talk": {
        "text": (
            "You speak calmly through the door: 'I don't want trouble. I just want to leave.'\n\n"
            "Silence.\n"
            "Then the voice replies: 'Wrong building to wake up in.'\n\n"
            "The footsteps walk away.\n"
            "You’re still alive… for now.\n\n"
            "END (Neutral Ending)"
        ),
        "choices": [],
    },
    "call_3_escape": {
        "text": (
            "You sprint to the hatch and wrench it open.\n"
            "You climb down fast, hands shaking.\n\n"
            "Behind you, the server room door slams open.\n"
            "But you're already gone.\n\n"
            "END (Good Ending)"
        ),
        "choices": [],
    },
}


def get_scene(scene_id: str) -> Dict[str, Any]:
    """Return the scene dict for a given scene_id, or a fallback scene."""
    return STORY.get(scene_id, {
        "text": "Error: Scene not found. END",
        "choices": []
    })


def is_end_scene(scene_id: str) -> bool:
    """True if the scene has no choices."""
    return len(get_scene(scene_id).get("choices", [])) == 0


def validate_choice(scene_id: str, choice_key: str) -> str:
    """
    Validate user choice and return next scene_id.
    If invalid, return the same scene_id (no progress).
    """
    scene = get_scene(scene_id)
    for c in scene.get("choices", []):
        if c["key"].upper() == choice_key.upper():
            return c["next"]
    return scene_id
