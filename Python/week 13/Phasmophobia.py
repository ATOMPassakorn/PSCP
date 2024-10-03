"""Phasmophobia"""
def ghost():
    """Phasmophobia"""
    find_evidence = set()
    for _ in range(3):
        evidence = input()
        find_evidence.add(evidence)
    find_evidence.discard("No evidence")
    ghosts = {
        "Banshee": {"EMF Level 5", "Fingerprints", "Freezing Temperatures"},
        "Demon": {"Ghost Writing", "Spirit Box", "Freezing Temperatures"},
        "Jinn": {"EMF Level 5", "Spirit Box", "Ghost Orb"},
        "Mare": {"Spirit Box", "Freezing Temperatures", "Ghost Orb"},
        "Oni": {"EMF Level 5", "Ghost Writing", "Spirit Box"},
        "Phantom": {"EMF Level 5", "Freezing Temperatures", "Ghost Orb"},
        "Poltergeist": {"Fingerprints", "Spirit Box", "Ghost Orb"},
        "Revenant": {"EMF Level 5", "Ghost Writing", "Fingerprints"},
        "Shade": {"EMF Level 5", "Ghost Writing", "Ghost Orb"},
        "Spirit": {"Ghost Writing", "Fingerprints", "Spirit Box"},
        "Wraith": {"Fingerprints", "Spirit Box", "Freezing Temperatures"},
        "Yurei": {"Ghost Writing", "Freezing Temperatures", "Ghost Orb"}
    }
    found=False
    for ghost_name, evidence in ghosts.items():
        if find_evidence.issubset(evidence):
            found=True
            print(ghost_name)
    if not found:
        print("Not yet discovered")
ghost()
