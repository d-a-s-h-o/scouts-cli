# This app is for managing scout troops

# All data is stored in the db.json file
# The data is stored in a dictionary with the following structure:
# At the top level there are these types of data: scouts, leaders, patrols, events, sections, troops, and badges
# Each of these types of data are stored in a list of dictionaries
# Each dictionary has a unique id and a name
# The id is used to link data together
# The name is used for display purposes
# The id is a string of the form "type of data id number"
# The type of data is one of the types listed above
# The id number is a unique number for that type of data
# For example, the first scout has an id of "scout 1"
# The second scout has an id of "scout 2"
# The first leader has an id of "leader 1"
# The first patrol has an id of "patrol 1"
# The first event has an id of "event 1"
# The first section has an id of "section 1"
# The first troop has an id of "troop 1"
# The first badge has an id of "badge 1"

# The scouts, leaders, patrols, events, sections, troops, and badges are stored in a list of dictionaries
import json
import os
import sys
import cmd

scouts = []
leaders = []
patrols = []
events = []
sections = []
troops = []
badges = []

# Load the data from the db.json file if it exists, otherwise create it

# Check if the db.json file exists
if os.path.exists("db.json"):
    # If it exists, load the data from it
    with open("db.json", "r") as f:
        data = json.load(f)
        # Check if the data is valid
        # Fix the data if it is invalid
        try :
            data["scouts"] = data["scouts"]
        except:
            data["scouts"] = []
            data["leaders"] = []
            data["patrols"] = []
            data["events"] = []
            data["sections"] = []
            data["troops"] = []
            data["badges"] = []

        # Load the data into the lists
        for scout in data["scouts"]:
            scouts.append(Scout(scout["id"], scout["name"], scout["dob"], scout["parents"], scout["paid"], scout["patrol"], scout["section"], scout["troop"], scout["badges"], scout["events"]))
        for leader in data["leaders"]:
            leaders.append(Leader(leader["id"], leader["name"], leader["phone"], leader["email"], leader["troop"], leader["section"]))
        for patrol in data["patrols"]:
            patrols.append(Patrol(patrol["id"], patrol["name"], patrol["troop"], patrol["section"], patrol["scouts"]))
        for event in data["events"]:
            events.append(Event(event["id"], event["name"], event["date"], event["location"], event["scouts"]))
        for section in data["sections"]:
            sections.append(Section(section["id"], section["name"], section["troop"], section["events"], section["scouts"], section["leaders"], section["patrols"]))
        for troop in data["troops"]:
            troops.append(Troop(troop["id"], troop["name"], troop["sections"], troop["events"], troop["scouts"], troop["leaders"]))
        for badge in data["badges"]:
            badges.append(Badge(badge["id"], badge["name"], badge["description"], badge["requirements"], badge["scouts"]))
else:
    # If it doesn't exist, create it
    with open("db.json", "w") as f:
        data = {"scouts": [], "leaders": [], "patrols": [], "events": [], "sections": [], "troops": [], "badges": []}
        json.dump(data, f)
    
def find_scout(id):
    for scout in scouts:
        if scout.get_id() == id:
            return scout
    return None

def find_leader(id):
    for leader in leaders:
        if leader.get_id() == id:
            return leader
    return None

def find_patrol(id):
    for patrol in patrols:
        if patrol.get_id() == id:
            return patrol
    return None

def find_event(id):
    for event in events:
        if event.get_id() == id:
            return event
    return None

def find_section(id):
    for section in sections:
        if section.get_id() == id:
            return section
    return None

def find_troop(id):
    for troop in troops:
        if troop.get_id() == id:
            return troop
    return None

def find_badge(id):
    for badge in badges:
        if badge.get_id() == id:
            return badge
    return None

def find_scouts(name):
    results = []
    for scout in scouts:
        # If the name is similar to the name of the scout, add it to the results
        if name in scout.get_name():
            results.append(scout)
    return results

def find_leaders(name):
    results = []
    for leader in leaders:
        # If the name is similar to the name of the leader, add it to the results
        if name in leader.get_name():
            results.append(leader)
    return results

def find_patrols(name):
    results = []
    for patrol in patrols:
        # If the name is similar to the name of the patrol, add it to the results
        if name in patrol.get_name():
            results.append(patrol)
    return results

def find_events(name):
    results = []
    for event in events:
        # If the name is similar to the name of the event, add it to the results
        if name in event.get_name():
            results.append(event)
    return results

def find_sections(name):
    results = []
    for section in sections:
        # If the name is similar to the name of the section, add it to the results
        if name in section.get_name():
            results.append(section)
    return results

def find_troops(name):
    results = []
    for troop in troops:
        # If the name is similar to the name of the troop, add it to the results
        if name in troop.get_name():
            results.append(troop)
    return results

def find_badges(name):
    results = []
    for badge in badges:
        # If the name is similar to the name of the badge, add it to the results
        if name in badge.get_name():
            results.append(badge)
    return results

def find_scouts_by_badge(badge):
    results = []
    for scout in scouts:
        # If the scout has the badge, add it to the results
        if badge in scout.get_badges():
            results.append(scout)
    return results

def find_scouts_by_event(event):
    results = []
    for scout in scouts:
        # If the scout has attended the event, add it to the results
        if event in scout.get_events():
            results.append(scout)
    return results

def find_scouts_by_patrol(patrol):
    results = []
    for scout in scouts:
        # If the scout is in the patrol, add it to the results
        if patrol in scout.get_patrol():
            results.append(scout)
    return results

def find_scouts_by_section(section):
    results = []
    for scout in scouts:
        # If the scout is in the section, add it to the results
        if section in scout.get_section():
            results.append(scout)
    return results

def find_scouts_by_troop(troop):
    results = []
    for scout in scouts:
        # If the scout is in the troop, add it to the results
        if troop in scout.get_troop():
            results.append(scout)
    return results

def find_leaders_by_section(section):
    results = []
    for leader in leaders:
        # If the leader is in the section, add it to the results
        if section in leader.get_section():
            results.append(leader)
    return results

def find_leaders_by_troop(troop):
    results = []
    for leader in leaders:
        # If the leader is in the troop, add it to the results
        if troop in leader.get_troop():
            results.append(leader)
    return results

def find_patrols_by_section(section):
    results = []
    for patrol in patrols:
        # If the patrol is in the section, add it to the results
        if section in patrol.get_section():
            results.append(patrol)
    return results

def find_events_by_section(section):
    results = []
    for event in events:
        # If the event is in the section, add it to the results
        if section in event.get_section():
            results.append(event)
    return results

def find_events_by_troop(troop):
    results = []
    for event in events:
        # If the event is in the troop, add it to the results
        if troop in event.get_troop():
            results.append(event)
    return results

def find_sections_by_troop(troop):
    results = []
    for section in sections:
        # If the section is in the troop, add it to the results
        if troop in section.get_troop():
            results.append(section)
    return results


# Create a function to save the data to the db.json file
def save_data():
    for scout in scouts:
        scout = {"id": scout.get_id(), "name": scout.get_name(), "dob": scout.get_dob(), "parents": scout.get_parents(), "paid": scout.get_paid(), "patrol": scout.get_patrol(), "section": scout.get_section(), "troop": scout.get_troop(), "badges": scout.get_badges(), "events": scout.get_events()}
        print(scout)
    for leader in leaders:
        leader = {"id": leader.get_id(), "name": leader.get_name(), "phone": leader.get_phone(), "email": leader.get_email(), "troop": leader.get_troop(), "section": leader.get_section()}
    for patrol in patrols:
        patrol = {"id": patrol.get_id(), "name": patrol.get_name(), "troop": patrol.get_troop(), "section": patrol.get_section(), "scouts": patrol.get_scouts()}
    for event in events:
        event = {"id": event.get_id(), "name": event.get_name(), "date": event.get_date(), "location": event.get_location(), "scouts": event.get_scouts()}
    for section in sections:
        section = {"id": section.get_id(), "name": section.get_name(), "troop": section.get_troop(), "events": section.get_events(), "scouts": section.get_scouts(), "leaders": section.get_leaders(), "patrols": section.get_patrols()}
    for troop in troops:
        troop = {"id": troop.get_id(), "name": troop.get_name(), "sections": troop.get_sections(), "events": troop.get_events(), "scouts": troop.get_scouts(), "leaders": troop.get_leaders()}
    for badge in badges:
        badge = {"id": badge.get_id(), "name": badge.get_name(), "description": badge.get_description(), "requirements": badge.get_requirements(), "scouts": badge.get_scouts()}
    with open("db.json", "w") as f:
        data = {"scouts": scouts, "leaders": leaders, "patrols": patrols, "events": events, "sections": sections, "troops": troops, "badges": badges}
        json.dump(data, f)

def make_id(type):
    id = f"{type} {len(globals()[type]) + 1}"
    return id

def get_id(type, id):
    for item in globals()[type]:
        if item["id"] == id:
            return item
    return None

def prompt_for_parent():
    parent_name = input("Enter the name of the parent:\n > ")
    if parent_name == "":
        return("E: Name")
    parent_phone = input("Enter the phone number of the parent (optional):\n > ")
    parent_email = input("Enter the email address of the parent (optional):\n > ")
    parent = {"name": parent_name, "phone": parent_phone, "email": parent_email}
    return parent

def prompt_for_scout():
    scout_name = input("Enter the name of the scout:\n > ")
    if scout_name == "":
        return("E: Name")
    scout_dob = input("Enter the date of birth of the scout (optional):\n > ")
    scout_parents = []
    keepGoing = False
    if input("Do you want to add a parent? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        parent = prompt_for_parent()
        if parent == "E: Name":
            add_parent()
        scout_parents.append(parent)
        if input("Do you want to add another parent? (y/n)\n > ") != "y":
            keepGoing = False
    scout_paid = input("Has the scout paid their dues? (y/n)\n > ")
    if scout_paid == "y":
        scout_paid = True
    elif scout_paid == "n":
        scout_paid = False
    else:
        scout_paid = None
    scout_section = input("Enter the id of the section the scout is in (optional):\n > ")
    tmp_section = find_section(scout_section)
    if tmp_section != None:
        tmp_section.add_scout(scout_id)
        tmp_troop = find_troop(tmp_section.get_troop())
        if tmp_troop != None:
            tmp_troop.add_scout(scout_id)
        else:
            scout_troop = None
    else:
        scout_section = None
        scout_troop = None
    scout_patrol = input("Enter the id of the patrol the scout is in (optional):\n > ")
    tmp_patrol = find_patrol(scout_patrol)
    if tmp_patrol != None:
        tmp_patrol.add_scout(scout_id)
    else:
        scout_patrol = None
    scout = {"name": scout_name, "dob": scout_dob, "parents": scout_parents, "paid": scout_paid, "section": scout_section, "patrol": scout_patrol, "troop": scout_troop, "badges": [], "events": []}
    return scout

def prompt_for_leader():
    leader_name = input("Enter the name of the leader:\n > ")
    if leader_name == "":
        return("E: Name")
    leader_phone = input("Enter the phone number of the leader (optional):\n > ")
    leader_email = input("Enter the email address of the leader (optional):\n > ")
    leader = {"name": leader_name, "phone": leader_phone, "email": leader_email}
    return leader

def prompt_for_patrol():
    patrol_name = input("Enter the name of the patrol:\n > ")
    if patrol_name == "":
        return("E: Name")
    patrol = {"name": patrol_name}
    return patrol

def prompt_for_event():
    event_name = input("Enter the name of the event:\n > ")
    if event_name == "":
        return("E: Name")
    event_date = input("Enter the date of the event (optional):\n > ")
    event_location = input("Enter the location of the event (optional):\n > ")
    event = {"name": event_name, "date": event_date, "location": event_location}
    return event

def prompt_for_section():
    section_name = input("Enter the name of the section:\n > ")
    if section_name == "":
        return("E: Name")
    section = {"name": section_name}
    return section

def prompt_for_troop():
    troop_name = input("Enter the name of the troop:\n > ")
    if troop_name == "":
        return("E: Name")
    troop = {"name": troop_name}
    return troop

def prompt_for_badge():
    badge_name = input("Enter the name of the badge:\n > ")
    if badge_name == "":
        return("E: Name")
    badge_description = input("Enter the description of the badge (optional):\n > ")
    badge_requirements = input("Enter the requirements of the badge (optional):\n > ")
    badge = {"name": badge_name, "description": badge_description, "requirements": badge_requirements}
    return badge

def prompt_for_scouts():
    scouts = []
    keepGoing = False
    if input("Do you want to add a scout? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        scout = prompt_for_scout()
        if scout == "E: Name":
            add_scout()
        scouts.append(scout)
        if input("Do you want to add another scout? (y/n)\n > ") != "y":
            keepGoing = False
    return scouts

def prompt_for_leaders():
    leaders = []
    keepGoing = False
    if input("Do you want to add a leader? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        leader = prompt_for_leader()
        if leader == "E: Name":
            add_leader()
        leaders.append(leader)
        if input("Do you want to add another leader? (y/n)\n > ") != "y":
            keepGoing = False
    return leaders

def prompt_for_patrols():
    patrols = []
    keepGoing = False
    if input("Do you want to add a patrol? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        patrol = prompt_for_patrol()
        if patrol == "E: Name":
            add_patrol()
        patrols.append(patrol)
        if input("Do you want to add another patrol? (y/n)\n > ") != "y":
            keepGoing = False
    return patrols

def prompt_for_events():
    events = []
    keepGoing = False
    if input("Do you want to add an event? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        event = prompt_for_event()
        if event == "E: Name":
            add_event()
        events.append(event)
        if input("Do you want to add another event? (y/n)\n > ") != "y":
            keepGoing = False
    return events

def prompt_for_sections():
    sections = []
    keepGoing = False
    if input("Do you want to add a section? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        section = prompt_for_section()
        if section == "E: Name":
            add_section()
        sections.append(section)
        if input("Do you want to add another section? (y/n)\n > ") != "y":
            keepGoing = False
    return sections

def prompt_for_troops():
    troops = []
    keepGoing = False
    if input("Do you want to add a troop? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        troop = prompt_for_troop()
        if troop == "E: Name":
            add_troop()
        troops.append(troop)
        if input("Do you want to add another troop? (y/n)\n > ") != "y":
            keepGoing = False
    return troops

def prompt_for_badges():
    badges = []
    leader = False
    if input("Do you want to add a badge? (y/n)\n > ") == "y":
        keepGoing = True
    while keepGoing:
        badge = prompt_for_badge()
        if badge == "E: Name":
            add_badge()
        badges.append(badge)
        if input("Do you want to add another badge? (y/n)\n > ") != "y":
            keepGoing = False
    return badges

def add_scout():
    scout = prompt_for_scout()
    if scout == "E: Name":
        add_scout()
    scout_id = make_id("scouts")
    scout["id"] = scout_id
    scout = Scout(scout_id, scout["name"], scout["dob"], scout["parents"], scout["paid"], scout["patrol"], scout["section"], scout["troop"], scout["badges"], scout["events"])
    scouts.append(scout)
    save_data()

def add_leader():
    leader = prompt_for_leader()
    if leader == "E: Name":
        add_leader()
    leader_id = make_id("leader")
    leader["id"] = leader_id
    leaders.append(leader)
    save_data()

def add_patrol():
    patrol = prompt_for_patrol()
    if patrol == "E: Name":
        add_patrol()
    patrol_id = make_id("patrol")
    patrol["id"] = patrol_id
    patrols.append(patrol)
    save_data()

def add_event():
    event = prompt_for_event()
    if event == "E: Name":
        add_event()
    event_id = make_id("event")
    event["id"] = event_id
    events.append(event)
    save_data()

def add_section():
    section = prompt_for_section()
    if section == "E: Name":
        add_section()
    section_id = make_id("section")
    section["id"] = section_id
    sections.append(section)
    save_data()

def add_troop():
    troop = prompt_for_troop()
    if troop == "E: Name":
        add_troop()
    troop_id = make_id("troop")
    troop["id"] = troop_id
    troops.append(troop)
    save_data()

def add_badge():
    badge = prompt_for_badge()
    if badge == "E: Name":
        add_badge()
    badge_id = make_id("badge")
    badge["id"] = badge_id
    badges.append(badge)
    save_data()

def add_scouts():
    scouts = prompt_for_scouts()
    for scout in scouts:
        scout_id = make_id("scout")
        scout["id"] = scout_id
        scouts.append(scout)
    save_data()

def add_leaders():
    leaders = prompt_for_leaders()
    for leader in leaders:
        leader_id = make_id("leader")
        leader["id"] = leader_id
        leaders.append(leader)
    save_data()

def add_patrols():
    patrols = prompt_for_patrols()
    for patrol in patrols:
        patrol_id = make_id("patrol")
        patrol["id"] = patrol_id
        patrols.append(patrol)
    save_data()

def add_events():
    events = prompt_for_events()
    for event in events:
        event_id = make_id("event")
        event["id"] = event_id
        events.append(event)
    save_data()

def add_sections():
    sections = prompt_for_sections()
    for section in sections:
        section_id = make_id("section")
        section["id"] = section_id
        sections.append(section)
    save_data()

def add_troops():
    troops = prompt_for_troops()
    for troop in troops:
        troop_id = make_id("troop")
        troop["id"] = troop_id
        troops.append(troop)
    save_data()

def add_badges():
    badges = prompt_for_badges()
    for badge in badges:
        badge_id = make_id("badge")
        badge["id"] = badge_id
        badges.append(badge)
    save_data()

def add_scout_to_patrol(scout_id, patrol_id):
    scout = find_scout(scout_id)
    patrol = find_patrol(patrol_id)
    scout.set_patrol(patrol_id)
    patrol.add_scout(scout_id)
    save_data()

def add_scout_to_section(scout_id, section_id):
    scout = find_scout(scout_id)
    section = find_section(section_id)
    scout.set_section(section_id)
    section.add_scout(scout_id)
    save_data()

def add_scout_to_troop(scout_id, troop_id):
    scout = find_scout(scout_id)
    troop = find_troop(troop_id)
    scout.set_troop(troop_id)
    troop.add_scout(scout_id)
    save_data()

def add_leader_to_section(leader_id, section_id):
    leader = find_leader(leader_id)
    section = find_section(section_id)
    troop = find_troop(section.get_troop())
    leader.set_section(section_id)
    section.add_leader(leader_id)
    troop.add_leader(leader_id)
    save_data()

def add_leader_to_troop(leader_id, troop_id):
    leader = find_leader(leader_id)
    troop = find_troop(troop_id)
    leader.set_troop(troop_id)
    save_data()

def add_patrol_to_section(patrol_id, section_id):
    patrol = find_patrol(patrol_id)
    section = find_section(section_id)
    patrol.set_section(section_id)
    section.add_patrol(patrol_id)
    save_data()

def add_event_to_section(event_id, section_id):
    event = find_event(event_id)
    section = find_section(section_id)
    troop = find_troop(section.get_troop())
    event.set_section(section_id)
    section.add_event(event_id)
    troop.add_event(event_id)
    save_data()

# Create a function to add a scout

# A scout has the following attributes:
# id: The id of the scout
# name: The name of the scout
# dob: The date of birth of the scout (optional)
# parents: The parents of the scout (optional)
#   Each parent has the following attributes:
#   name: The name of the parent
#   phone: The phone number of the parent (optional)
#   email: The email address of the parent (optional)
#     There can be multiple parents
# paid: Whether the scout has paid their dues (optional)
#   If the scout has paid their dues, this is True
#   If not, then there can be a partial payment (Number) or no payment (False)
# patrol: The patrol the scout is in (optional), this is the id of the patrol
# section: The section the scout is in (optional), this is the id of the section
# troop: The troop the scout is in (optional), this is the id of the troop
# badges: The badges the scout has earned (optional), this is a list of badge ids
# events: The events the scout has attended (optional), this is a list of event ids

class Scout:
    def __init__(self, id, name, dob=None, parents=None, paid=None, patrol=None, section=None, troop=None, badges=None, events=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.parents = parents
        self.paid = paid
        self.patrol = patrol
        self.section = section
        self.troop = troop
        self.badges = badges
        self.events = events

    def __str__(self):
        return f"Scout: {self.name}"

    def __repr__(self):
        return f"Scout: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        # update the id of the patrol
        if self.patrol != None:
            self.patrol.sadd_scout(self.id)
        # update the id of the section
        if self.section != None:
            self.section.add_scout(self.id)
        # update the id of the troop
        if self.troop != None:
            self.troop.add_scout(self.id)
        # update the id of the badges
        for badge in self.badges:
            badge.add_scout(self.id)
        # update the id of the events
        for event in self.events:
            event.add_scout(self.id)
        save_data()


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        save_data()

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        # make sure dob is a valid date in the format dd/mm/yyyy, or yyyy-mm-dd
        # if it is, set self.dob to dob
        # if not, raise an error
        if dob == None:
            self.dob = dob
        else:
            try:
                dob = dob.split("/")
                day = int(dob[0])
                month = int(dob[1])
                year = int(dob[2])
                self.dob = f"{day}/{month}/{year}"
            except:
                try:
                    dob = dob.split("-")
                    year = int(dob[0])
                    month = int(dob[1])
                    day = int(dob[2])
                    self.dob = f"{day}/{month}/{year}"
                except:
                    raise ValueError("Invalid date of birth")
        save_data()

    def get_parents(self):
        return self.parents

    def add_parent(self):
        parent = prompt_for_parent()
        if parent == "E: Name":
            add_parent()
        self.parents.append(parent)
        save_data()

    def set_parents(self, parents):
        # make sure parents is a list of dictionaries
        for parent in parents:
            if type(parent) != dict:
                raise TypeError("Parents must be a list of dictionaries")
            if "name" not in parent:
                raise ValueError("Parents must have a name")
        self.parents = parents
        save_data()

    def get_paid(self):
        return self.paid

    def set_paid(self, paid):
        self.paid = paid
        save_data()

    def get_patrol(self):
        return self.patrol

    def set_patrol(self, patrol):
        self.patrol = patrol
        # add the scout to the patrol's scouts
        patrol.add_scout(self.id)
        save_data()

    def get_section(self):
        return self.section

    def set_section(self, section):
        self.section = section
        # add the scout to the section's scouts
        section.add_scout(self.id)
        save_data()

    def get_troop(self):
        return self.troop

    def set_troop(self, troop):
        self.troop = troop
        # add the scout to the troop's scouts
        troop.add_scout(self.id)
        save_data()

    def get_badges(self):
        return self.badges

    def add_badge(self, badge):
        self.badges.append(badge)
        # add the scout to the badge's scouts
        badge.add_scout(self.id)
        save_data()

    def set_badges(self, badges):
        self.badges = badges
        # add the scout to the badge's scouts
        for badge in badges:
            badge.add_scout(self.id)
        save_data()

    def get_events(self):
        return self.events

    def add_event(self, event):
        self.events.append(event)
        # add the scout to the event's scouts
        event.add_scout(self.id)
        save_data()

    def set_events(self, events):
        self.events = events
        # add the scout to the event's scouts
        for event in events:
            event.add_scout(self.id)
        save_data()

class Leader:
    def __init__(self, id, name, phone=None, email=None, troop=None, section=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.troop = troop
        self.section = section

    def __str__(self):
        return f"Leader: {self.name}"

    def __repr__(self):
        return f"Leader: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        # update the id of the troop
        if self.troop != None:
            self.troop.add_leader(self.id)
        # update the id of the section
        if self.section != None:
            self.section.add_leader(self.id)
        save_data()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        save_data()

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone
        save_data()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        save_data()

    def get_troop(self):
        return self.troop

    def set_troop(self, troop):
        self.troop = troop
        # add the leader to the troop's leaders
        troop.add_leader(self.id)
        save_data()

    def get_section(self):
        return self.section

    def set_section(self, section):
        self.section = section
        # add the leader to the section's leaders
        section.add_leader(self.id)
        save_data()

class Patrol:
    def __init__(self, id, name, troop=None, section=None, scouts=None):
        self.id = id
        self.name = name
        self.troop = troop
        self.section = section
        self.scouts = scouts

    def __str__(self):
        return f"Patrol: {self.name}"

    def __repr__(self):
        return f"Patrol: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        # update the id of the troop
        if self.troop != None:
            self.troop.add_patrol(self.id)
        # update the id of the section
        if self.section != None:
            self.section.add_patrol(self.id)
        # update the id of the scouts
        for scout in self.scouts:
            scout.set_patrol(self.id)
        save_data()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        save_data()

    def get_troop(self):
        return self.troop

    def set_troop(self, troop):
        self.troop = troop
        # add the patrol to the troop's patrols
        troop.add_patrol(self.id)
        save_data()

    def get_section(self):
        return self.section

    def set_section(self, section):
        self.section = section
        # add the patrol to the section's patrols
        section.add_patrol(self.id)
        save_data()

    def remove_section(self):
        self.section = None
        save_data()

    def get_scouts(self):
        return self.scouts

    def add_scout(self, scout):
        self.scouts.append(scout)
        # add the patrol to the scout's patrol
        scout.set_patrol(self.id)
        save_data()

    def remove_scout(self, scout):
        self.scouts.remove(scout)
        # remove the patrol from the scout's patrol
        scout.set_patrol(None)
        save_data()

    def set_scouts(self, scouts):
        self.scouts = scouts
        # add the patrol to the scout's patrol
        for scout in scouts:
            scout.set_patrol(self.id)
        save_data()

    def delete(self):
        # remove the patrol from the troop's patrols
        self.troop.remove_patrol(self.id)
        # remove the patrol from the section's patrols
        self.section.remove_patrol(self.id)
        # remove the patrol from the scouts' patrols
        for scout in self.scouts:
            scout.remove_patrol(self.id)
        # remove the patrol from the list of patrols
        patrols.remove(self)
        save_data()

class Event:
    def __init__(self, id, name, date=None, location=None, scouts=None):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.scouts = scouts

    def __str__(self):
        return f"Event: {self.name}"

    def __repr__(self):
        return f"Event: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_scouts(self):
        return self.scouts

    def add_scout(self, scout):
        self.scouts.append(scout)

    def set_scouts(self, scouts):
        self.scouts = scouts

class Section:
    def __init__(self, id, name, troop=None, events=None, scouts=None, leaders=None, patrols=None):
        self.id = id
        self.name = name
        self.troop = troop
        self.events = events
        self.scouts = scouts
        self.leaders = leaders
        self.patrols = patrols

    def __str__(self):
        return f"Section: {self.name}"

    def __repr__(self):
        return f"Section: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_troop(self):
        return self.troop

    def set_troop(self, troop):
        self.troop = troop

    def get_events(self):
        return self.events

    def add_event(self, event):
        self.events.append(event)

    def set_events(self, events):
        self.events = events

    def get_scouts(self):
        return self.scouts

    def add_scout(self, scout):
        self.scouts.append(scout)

    def set_scouts(self, scouts):
        self.scouts = scouts

    def get_leaders(self):
        return self.leaders

    def add_leader(self, leader):
        self.leaders.append(leader)

    def set_leaders(self, leaders):
        self.leaders = leaders

    def get_patrols(self):
        return self.patrols

    def add_patrol(self, patrol):
        self.patrols.append(patrol)

    def set_patrols(self, patrols):
        self.patrols = patrols

class Troop:
    def __init__(self, id, name, sections=None, events=None, scouts=None, leaders=None):
        self.id = id
        self.name = name
        self.sections = sections
        self.events = events
        self.scouts = scouts
        self.leaders = leaders

    def __str__(self):
        return f"Troop: {self.name}"

    def __repr__(self):
        return f"Troop: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        # update the id of the sections
        for section in self.sections:
            section.set_troop(self.id)
        # update the id of the scouts
        for scout in self.scouts:
            scout.set_troop(self.id)
        # update the id of the leaders
        for leader in self.leaders:
            leader.set_troop(self.id)
        save_data()
        

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        save_data()

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)
        # add the troop to the section's troop
        section.set_troop(self.id)
        save_data()

    def set_sections(self, sections):
        self.sections = sections
        # add the troop to the section's troop
        for section in sections:
            section.set_troop(self.id)
        save_data()

    def get_events(self):
        return self.events

    def add_event(self, event):
        self.events.append(event)
        save_data()

    def set_events(self, events):
        self.events = events
        save_data()

    def get_scouts(self):
        return self.scouts

    def add_scout(self, scout):
        self.scouts.append(scout)
        # add the troop to the scout's troop
        scout.set_troop(self.id)
        save_data()

    def set_scouts(self, scouts):
        self.scouts = scouts
        # add the troop to the scout's troop
        for scout in scouts:
            scout.set_troop(self.id)
        save_data()

    def get_leaders(self):
        return self.leaders

    def add_leader(self, leader):
        self.leaders.append(leader)
        # add the troop to the leader's troop
        leader.set_troop(self.id)
        save_data()

    def set_leaders(self, leaders):
        self.leaders = get_leaders
        # add the troop to the leader's troop
        for leader in leaders:
            leader.set_troop(self.id)
        save_data()

class Badge:
    def __init__(self, id, name, description=None, requirements=None, scouts=None):
        self.id = id
        self.name = name
        self.description = description
        self.requirements = requirements
        self.scouts = scouts

    def __str__(self):
        return f"Badge: {self.name}"

    def __repr__(self):
        return f"Badge: {self.name}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        # update the id of the scouts
        for scout in self.scouts:
            scout.add_badge(self.id)
        save_data()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        save_data()

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
        save_data()

    def get_requirements(self):
        return self.requirements

    def set_requirements(self, requirements):
        self.requirements = requirements
        save_data()

    def get_scouts(self):
        return self.scouts

    def add_scout(self, scout):
        self.scouts.append(scout)
        # add the badge to the scout's badges
        scout.add_badge(self.id)
        save_data()

    def set_scouts(self, scouts):
        self.scouts = scouts
        # add the badge to the scout's badges
        for scout in scouts:
            scout.add_badge(self.id)
        save_data()

class Shell(cmd.Cmd):
    intro = "Welcome to the Scout Management System. Type help or ? to list commands.\n"
    prompt = "(scout) "
    file = None

    def do_add(self, arg):
        "Add a scout, leader, patrol, event, section, troop or badge"
        if arg == "scout":
            add_scout()
        elif arg == "leader":
            add_leader()
        elif arg == "patrol":
            add_patrol()
        elif arg == "event":
            add_event()
        elif arg == "section":
            add_section()
        elif arg == "troop":
            add_troop()
        elif arg == "badge":
            add_badge()
        else:
            print("Invalid argument")

    def do_add_all(self, arg):
        "Add scouts, leaders, patrols, events, sections, troops or badges"
        if arg == "scouts":
            add_scouts()
        elif arg == "leaders":
            add_leaders()
        elif arg == "patrols":
            add_patrols()
        elif arg == "events":
            add_events()
        elif arg == "sections":
            add_sections()
        elif arg == "troops":
            add_troops()
        elif arg == "badges":
            add_badges()
        else:
            print("Invalid argument")

    def do_add_scout_to_patrol(self, arg):
        "Add a scout to a patrol"
        args = arg.split(" ")
        if len(args) == 2:
            add_scout_to_patrol(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_add_scout_to_section(self, arg):
        "Add a scout to a section"
        args = arg.split(" ")
        if len(args) == 2:
            add_scout_to_section(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_add_scout_to_troop(self, arg):
        "Add a scout to a troop"
        args = arg.split(" ")
        if len(args) == 2:
            add_scout_to_troop(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_add_leader_to_section(self, arg):
        "Add a leader to a section"
        args = arg.split(" ")
        if len(args) == 2:
            add_leader_to_section(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_add_leader_to_troop(self, arg):
        "Add a leader to a troop"
        args = arg.split(" ")
        if len(args) == 2:
            add_leader_to_troop(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_add_patrol_to_section(self, arg):
        "Add a patrol to a section"
        args = arg.split(" ")
        if len(args) == 2:
            add_patrol_to_section(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_add_event_to_section(self, arg):
        "Add an event to a section"
        args = arg.split(" ")
        if len(args) == 2:
            add_event_to_section(args[0], args[1])
        else:
            print("Invalid arguments")

    def do_list(self, arg):
        "List scouts, leaders, patrols, events, sections, troops or badges"
        if arg == "scouts":
            print(scouts)
        elif arg == "leaders":
            print(leaders)
        elif arg == "patrols":
            print(patrols)
        elif arg == "events":
            print(events)
        elif arg == "sections":
            print(sections)
        elif arg == "troops":
            print(troops)
        elif arg == "badges":
            print(badges)
        else:
            print("Invalid argument")

    def do_find(self, arg):
        "Find a scout, leader, patrol, event, section, troop or badge"
        args = arg.split(" ")
        if len(args) == 2:
            if args[0] == "scout":
                print(find_scout(args[1]))
            elif args[0] == "leader":
                print(find_leader(args[1]))
            elif args[0] == "patrol":
                print(find_patrol(args[1]))
            elif args[0] == "event":
                print(find_event(args[1]))
            elif args[0] == "section":
                print(find_section(args[1]))
            elif args[0] == "troop":
                print(find_troop(args[1]))
            elif args[0] == "badge":
                print(find_badge(args[1]))
            else:
                print("Invalid argument")
        else:
            print("Invalid arguments")

    def do_edit(self, arg):
        "Edit a scout, leader, patrol, event, section, troop or badge"
        args = arg.split(" ")
        if len(args) == 2:
            if args[0] == "scout":
                scout = find_scout(args[1])
                if scout != None:
                    edit_scout(scout)
                else:
                    print("Scout not found")
            elif args[0] == "leader":
                leader = find_leader(args[1])
                if leader != None:
                    edit_leader(leader)
                else:
                    print("Leader not found")
            elif args[0] == "patrol":
                patrol = find_patrol(args[1])
                if patrol != None:
                    edit_patrol(patrol)
                else:
                    print("Patrol not found")
            elif args[0] == "event":
                event = find_event(args[1])
                if event != None:
                    edit_event(event)
                else:
                    print("Event not found")
            elif args[0] == "section":
                section = find_section(args[1])
                if section != None:
                    edit_section(section)
                else:
                    print("Section not found")
            elif args[0] == "troop":
                troop = find_troop(args[1])
                if troop != None:
                    edit_troop(troop)
                else:
                    print("Troop not found")
            elif args[0] == "badge":
                badge = find_badge(args[1])
                if badge != None:
                    edit_badge(badge)
                else:
                    print("Badge not found")
            else:
                print("Invalid argument")
        else:
            print("Invalid arguments")

    def do_delete(self, arg):
        "Delete a scout, leader, patrol, event, section, troop or badge"
        args = arg.split(" ")
        if len(args) == 2:
            if args[0] == "scout":
                scout = find_scout(args[1])
                if scout != None:
                    scout.delete()
                else:
                    print("Scout not found")
            elif args[0] == "leader":
                leader = find_leader(args[1])
                if leader != None:
                    leader.delete()
                else:
                    print("Leader not found")
            elif args[0] == "patrol":
                patrol = find_patrol(args[1])
                if patrol != None:
                    patrol.delete()
                else:
                    print("Patrol not found")
            elif args[0] == "event":
                event = find_event(args[1])
                if event != None:
                    event.delete()
                else:
                    print("Event not found")
            elif args[0] == "section":
                section = find_section(args[1])
                if section != None:
                    section.delete()
                else:
                    print("Section not found")
            elif args[0] == "troop":
                troop = find_troop(args[1])
                if troop != None:
                    troop.delete()
                else:
                    print("Troop not found")
            elif args[0] == "badge":
                badge = find_badge(args[1])
                if badge != None:
                    badge.delete()
                else:
                    print("Badge not found")
            else:
                print("Invalid argument")
        else:
            print("Invalid arguments")

    def do_exit(self, arg):
        "Exit the program"
        print("Exiting...")
        return True

    def do_quit(self, arg):
        "Exit the program"
        print("Exiting...")
        return True

def main():
    # Load the data from the db.json file
    # Create a fancy shell
    shell = Shell()
    # Run the shell
    shell.cmdloop()

main()