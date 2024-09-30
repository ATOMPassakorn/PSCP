def ghost():
    """Phasmophobia"""
    find_evidence = set()
    for _ in range(3):
        evidence = input()
        find_evidence.add(evidence)
    ghosts = {
        "Banshee": {"EMF Level 5", "Fingerprints", "Freezing Temperatures"},
        "Demon": {"Ghost Writing", "Spirit Box", "Freezing Temperatures"},
        "Jinn": {"EMF Level 5", "Spirit Box", "Ghost Orb"},
        "Mare": {"Spirit Box", "Freezing Temperatures", "Ghost Orb"},
        "Oni": {"EMF Level 5", "Ghost Writing", "Spirit Box"},
        "Phantom": {"EMF Level 5", "Ghost Writing", "Spirit Box"},
        "Poltergeist": {"Fingerprints", "Spirit Box", "Ghost Orb"},
        "Revenant": {"EMF Level 5", "Ghost Writing", "Fingerprints"},
        "Shade": {"EMF Level 5", "Ghost Writing", "Ghost Orb"},
        "Spirit": {"Ghost Writing", "Fingerprints", "Freezing Temperatures"},
        "Wraith": {"Fingerprints", "Spirit Box", "Freezing Temperatures"},
        "Yurei": {"Ghost Writing", "Freezing Temperatures", "Ghost Orb"}
    }
    found_ghosts = []
    for ghost_name, evidence in ghosts.items():
        matching_evidence = find_evidence.intersection(evidence)
        if matching_evidence>=2:
            found_ghosts.append(ghost_name)
    if found_ghosts:
        print(found_ghosts)
    else:
        print("Not yet discovered")
ghost()
