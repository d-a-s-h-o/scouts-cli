import cmd
import os
import sys
import json

try:
    with open('db.json', 'r') as f:
        data = json.load(f)
except:
    with open('db.json', 'w') as f:
        f.write('{}')
    data = {
        'scouts': {},
        'patrols': {},
        'leaders': {},
        'sections': {},
        'troops': {},
        'events': {},
        'badges': {}
    }
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)

def make(function, *args):
    def id(type): # type = scout, patrol, leader, section, troop, event, badge
        if type == 'scout':
            return 'scout' + str(len(data['scouts']) + 1)
        elif type == 'patrol':
            return 'patrol' + str(len(data['patrols']) + 1)
        elif type == 'leader':
            return 'leader' + str(len(data['leaders']) + 1)
        elif type == 'section':
            return 'section' + str(len(data['sections']) + 1)
        elif type == 'troop':
            return 'troop' + str(len(data['troops']) + 1)
        elif type == 'event':
            return 'event' + str(len(data['events']) + 1)
        elif type == 'badge':
            return 'badge' + str(len(data['badges']) + 1)
        else:
            return None
        
    def scout(name):
        scout = Scout(name=name)
        return scout
    
    if function == 'id':
        return id(args[0])
    elif function == 'scout':
        return scout(args[0])

def validators():
    def scout(name: str):
        if name is not str:
            print('Error: Scout name must be a string')
        else:
            return True

    def patrol(name: str):
        if name is not str:
            print('Error: Patrol name must be a string')
        else:
            return True

    def leader(name: str):
        if name is not str:
            print('Error: Leader name must be a string')
        else:
            return True

    def section(name: str):
        if name is not str:
            print('Error: Section name must be a string')
        else:
            return True

    def troop(name: str):
        if name is not str:
            print('Error: Troop name must be a string')
        else:
            return True

    def event(name: str):
        if name is not str:
            print('Error: Event name must be a string')
        else:
            return True

    def badge(name: str):
        if name is not str:
            print('Error: Badge name must be a string')
        else:
            return True
        
    return {
        'scout': scout,
        'patrol': patrol,
        'leader': leader,
        'section': section,
        'troop': troop,
        'event': event,
        'badge': badge
    }

def test(function, *args):
    if function == 'make_id':
        return make('id', args[0])
    elif function == 'make_scout':
        return make('scout', args[0])

class Troop:
    def __init__(self,
                name: str,
                sections: list=[],
            ):
        self.name = name
        self.id = make('id', 'troop')
        self.sections = sections

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id

    def get_sections(self):
        return self.sections
    
    def add_section(self, section: str):
        self.sections.append(section)
        data['sections'][section]['troop'] = self.id

    def set_sections(self, sections: list):
        self.sections = sections
        for section in sections:
            if section in data['sections']:
                data['sections'][section]['troop'] = self.id

    def remove_section(self, section: str):
        self.sections.remove(section)
        data['sections'][section]['troop'] = ''

class Section:
    def __init__(self,
                name: str,
                leaders: list=[], # List of leader IDs
                scouts: list=[], # List of scout IDs
                patrols: list=[], # List of patrol IDs
                troop: str='' # Troop ID
            ):
        self.name = name
        self.id = make('id', 'section')
        self.leaders = leaders
        self.scouts = scouts
        self.patrols = patrols
        self.troop = troop

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id

    def get_leaders(self):
        return self.leaders
    
    def add_leader(self, leader: str):
        self.leaders.append(leader)
        data['leaders'][leader]['section'].append(self.id)

    def set_leaders(self, leaders: list):
        self.leaders = leaders

    def remove_leader(self, leader: str):
        self.leaders.remove(leader)

    def get_scouts(self):
        return self.scouts
    
    def add_scout(self, scout: str):
        self.scouts.append(scout)

    def set_scouts(self, scouts: list):
        self.scouts = scouts

    def remove_scout(self, scout: str):
        self.scouts.remove(scout)

    def get_patrols(self):
        return self.patrols
    
    def add_patrol(self, patrol: str):
        self.patrols.append(patrol)

    def set_patrols(self, patrols: list):
        self.patrols = patrols

    def remove_patrol(self, patrol: str):
        self.patrols.remove(patrol)

class Leader:
    def __init__(self,
                name: str,
                sections: list=[], # List of section IDs
                phone: str='', # Leaders phone number
                email: str='', # Leaders email address
                address: str='' # Leaders home address
            ):
        self.name = name
        self.id = make('id', 'leader')
        self.sections = sections

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id

    def get_sections(self):
        return self.sections
    
    def add_section(self, section: str):
        self.sections.append(section)
        try:
            if section in data['sections']:
                data['sections'][section]['leaders'].append(self.id)
            else:
                print('Error: Section not found')
        except:
                print('Error: Something went wrong')
    
    def set_sections(self, sections: list):
        self.sections = sections
        try:
            for section in sections:
                if section in data['sections']:
                    data['sections'][section]['leaders'].append(self.id)
                else:
                    print('Error: Section not found')
        except:
            print('Error: Something went wrong')

    def get_troop(self):
        troop = data['sections'][self.section]['troop']
        return troop

class Scout:
    def __init__(self,
                name: str,
                points: int=0,
                rank: str='', # Rank ID
                patrol: str='', # Patrol ID
                section: str='', # Section ID
                events_attended: list=[], # List of event IDs
                badges_earned: list=[], # List of badge IDs
                badges_received: list=[], # List of badge IDs
                dob: str='', # Date of birth in format YYYY-MM-DD or dd/mm/yyyy
                scouts_phone: str='', # Scouts phone number
                parents: list=[
                    dict({
                        'name': str(''),
                        'phone': str(''),
                        'email': str(''),
                        'address': str('')
                    })
                ],
                medical: dict={
                    'allergies': str(''),
                    'medications': str(''),
                    'conditions': str(''),
                    'notes': str(''),
                    'doctor': dict({
                        'name': str(''),
                        'phone': str('')
                    })
                },
                payments: list=[
                    dict({
                        'date': str(''),
                        'amount': str(''),
                        'method': str(''),
                        'notes': str('')
                    })
                ]
            ):
        self.name= name
        self.id = make('id', 'scout')
        self.points = points
        self.rank = rank
        self.patrol = patrol
        self.section = section
        self.events_attended = events_attended
        self.badges_earned = badges_earned
        self.badges_received = badges_received
        self.dob = dob
        self.scouts_phone = scouts_phone
        self.parents = parents
        self.medical = medical
        self.payments = payments

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id

    def get_points(self):
        return self.points
    
    def add_points(self, points: int):
        self.points = self.points + points

    def set_points(self, points: int):
        self.points = points

    def get_rank(self):
        return self.rank
    
    def set_rank(self, rank: str):
        self.rank = rank

    def get_patrol(self):
        return self.patrol
    
    def set_patrol(self, patrol: str):
        if patrol not in data['sections'][self.section]['patrols']:
            print('Error: Patrol not found')
        else:
            self.patrol = patrol

    def get_section(self):
        return self.section
    
    def set_section(self, section: str):
        if section not in data['troops'][self.troop]['sections']:
            print('Error: Section not found')
        else:
            self.section = section

    def get_troop(self):
        troop = data['sections'][self.section]['troop']
        return troop

    def get_events_attended(self):
        return self.events_attended
    
    def add_event_attended(self, event: str):
        self.events_attended.append(event)
        data['events'][event]['attendance'].append(self.id)

    def remove_event_attended(self, event: str):
        self.events_attended.remove(event)
        data['events'][event]['attendance'].remove(self.id)

    def get_badges_earned(self):
        return self.badges_earned
    
    def add_badge_earned(self, badge: str):
        self.badges_earned.append(badge)
        data['badges'][badge]['scouts_earned'].append(self.id)

    def set_badges_earned(self, badges: list):
        self.badges_earned = badges
        for badge in badges:
            data['badges'][badge]['scouts_earned'].append(self.id)

    def remove_badge_earned(self, badge: str):
        self.badges_earned.remove(badge)
        data['badges'][badge]['scouts_earned'].remove(self.id)

    def get_badges_received(self):
        return self.badges_received
    
    def add_badge_received(self, badge: str):
        self.badges_received.append(badge)
        data['badges'][badge]['scouts_received'].append(self.id)

    def set_badges_received(self, badges: list):
        self.badges_received = badges
        for badge in badges:
            data['badges'][badge]['scouts_received'].append(self.id)

    def remove_badge_received(self, badge: str):
        self.badges_received.remove(badge)
        data['badges'][badge]['scouts_received'].remove(self.id)

    def get_dob(self):
        return self.dob
    
    def set_dob(self, dob: str):
        self.dob = dob

    def get_scouts_phone(self):
        return self.scouts_phone
    
    def set_scouts_phone(self, phone: str):
        self.scouts_phone = phone

    def get_parents(self):
        return self.parents
    
    def add_parent(self, parent: dict):
        try:
            if parent is not dict:
                print('Error: Parent object must be a dictionary')
            else:
                if parent['name'] is not str:
                    print('Error: Parent must have a name')
                else:
                    self.parents.append(parent)
        except:
            print('Error: Something went wrong')

    def remove_parent(self, parent: dict):
        self.parents.remove(parent)

    def get_medical(self):
        return self.medical
    
    def set_medical(self, medical: dict):
        self.medical = medical

    def get_payments(self):
        return self.payments
    
    def add_payment(self, payment: dict):
        self.payments.append(payment)

    def remove_payment(self, payment: dict):
        self.payments.remove(payment)

class Patrol:
    def __init__(self,
                name: str,
                scouts: list=[], # List of scout IDs
                section: str='' # Section ID
            ):
        self.name = name
        self.id = make('id', 'patrol')
        self.scouts = scouts
        self.section = section

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id

    def get_scouts(self):
        return self.scouts
    
    def add_scout(self, scout: str):
        self.scouts.append(scout)

    def set_scouts(self, scouts: list):
        self.scouts = scouts

    def remove_scout(self, scout: str):
        self.scouts.remove(scout)

    def get_section(self):
        return self.section
    
    def set_section(self, section: str):
        self.section = section

    def get_troop(self):
        troop = data['sections'][self.section]['troop']
    
    def set_troop(self, troop: str):
        self.troop = troop

class Event:
    def __init__(self,
                name: str,
                date: str='', # Date of event in format YYYY-MM-DD or dd/mm/yyyy
                location: str='', # Location of event
                description: str='', # Description of event
                attendance: list=[], # List of scout IDs
            ):
        self.name = name
        self.id = make('id', 'event')
        self.date = date
        self.location = location
        self.description = description
        self.attendance = attendance

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        for scout in self.attendance:
            data['scouts'][scout]['events_attended'].remove(self.id)
        self.id = id
        for scout in self.attendance:
            data['scouts'][scout]['events_attended'].append(self.id)

    def get_date(self):
        return self.date
    
    def set_date(self, date: str):
        self.date = date

    def get_time(self):
        return self.time
    
    def set_time(self, time: str):
        self.time = time

    def get_location(self):
        return self.location
    
    def set_location(self, location: str):
        self.location = location

    def get_description(self):
        return self.description
    
    def set_description(self, description: str):
        self.description = description

    def get_attendance(self):
        return self.attendance
    
    def add_attendance(self, scout: str):
        self.attendance.append(scout)
        data['scouts'][scout]['events_attended'].append(self.id)

    def set_attendance(self, attendance: list):
        self.attendance = attendance
        for scout in attendance:
            data['scouts'][scout]['events_attended'].append(self.id)

    def remove_attendance(self, scout: str):
        self.attendance.remove(scout)
        data['scouts'][scout]['events_attended'].remove(self.id)

class Badge:
    def __init__(self,
                name: str,
                description: str='', # Description of badge
                requirements: list=[], # List of requirements
                scouts_earned: list=[], # List of scout IDs
                scouts_received: list=[], # List of scout IDs
            ):
        self.name = name
        self.id = make('id', 'badge')
        self.description = description
        self.requirements = requirements
        self.scouts_earned = scouts_earned
        self.scouts_received = scouts_received

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id
        for scout in self.scouts_earned:
            data['scouts'][scout]['badges_earned'].append(self.id)

    def get_description(self):
        return self.description
    
    def set_description(self, description: str):
        self.description = description

    def get_requirements(self):
        return self.requirements
    
    def set_requirements(self, requirements: list):
        self.requirements = requirements

    def get_scouts(self):
        return self.scouts
    
    def add_scout_earned(self, scout: str):
        self.scouts.append(scout)
        data['scouts'][scout]['badges_earned'].append(self.id)

    def set_scouts_earned(self, scouts: list):
        self.scouts = scouts
        for scout in scouts:
            data['scouts'][scout]['badges_earned'].append(self.id)

    def remove_scout_earned(self, scout: str):
        self.scouts.remove(scout)
        data['scouts'][scout]['badges_earned'].remove(self.id)

    def get_scouts_received(self):
        return self.scouts_received
    
    def add_scout_received(self, scout: str):
        self.scouts_received.append(scout)
        data['scouts'][scout]['badges_received'].append(self.id)

    def set_scouts_received(self, scouts: list):
        self.scouts_received = scouts
        for scout in scouts:
            data['scouts'][scout]['badges_received'].append(self.id)

    def remove_scout_received(self, scout: str):
        self.scouts_received.remove(scout)
        data['scouts'][scout]['badges_received'].remove(self.id)

class Shell(cmd.Cmd):
    intro = 'Welcome to the Scout Management System. Type help or ? to list commands.\n'
    prompt = '(scouts) '
    file = None

    def postcmd(self, stop, line):
        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)
        return stop
    
    def preloop(self):
        with open('db.json', 'r') as f:
            data = json.load(f)

    def do_exit(self, inp):
        'Exit the shell'
        print('Exiting...')
        return True
    
    def do_quit(self, inp):
        'Exit the shell'
        print('Exiting...')
        return True

    def do_EOF(self, inp):
        'Exit the shell'
        print('Exiting...')
        return True

    def do_scout(self, inp):
        'Create a new scout. Usage: scout <name> <section> <patrol> <dob> <scouts_phone> <medical_allergies> <medical_medications> <medical_conditions> <medical_notes> <medical_doctor_name> <medical_doctor_phone>'
        if inp == '':
            print('Error: Invalid arguments')
            return
        if inp.split(' ')[0] == 'help':
            print('Usage: scout <name> <section> <patrol> <dob> <scouts_phone> <medical_allergies> <medical_medications> <medical_conditions> <medical_notes> <medical_doctor_name> <medical_doctor_phone>')
            return
        if inp.split(' ')[0] == 'list':
            print('Scouts:')
            for scout in data['scouts']:
                print(scout['name'])
            return
        if inp.split(' ')[0] is str:
            scout_name = inp.split(' ')[0]
            
        # Prompt through the creation of a scout
        scout_name = input('Scout Name: ')
        scout_section = input('Scout Section: ')
        scout_patrol = input('Scout Patrol: ')
        scout_dob = input('Scout Date of Birth: ')
        scout_scouts_phone = input('Scout Phone Number: ')
        scout_medical_allergies = input('Scout Allergies: ')
        scout_medical_medications = input('Scout Medications: ')
        scout_medical_conditions = input('Scout Conditions: ')
        scout_medical_notes = input('Scout Medical Notes: ')
        scout_medical_doctor_name = input('Scout Doctor Name: ')
        scout_medical_doctor_phone = input('Scout Doctor Phone: ')
        scout_parents = []
        scout_payments = []
        scout = Scout(name=scout_name, section=scout_section, patrol=scout_patrol, dob=scout_dob, scouts_phone=scout_scouts_phone, medical={
            'allergies': scout_medical_allergies,
            'medications': scout_medical_medications,
            'conditions': scout_medical_conditions,
            'notes': scout_medical_notes,
            'doctor': {
                'name': scout_medical_doctor_name,
                'phone': scout_medical_doctor_phone
            }
        }, parents=scout_parents, payments=scout_payments)
        data['scouts'][scout.get_id()] = {
            'name': scout.get_name(),
            'points': scout.get_points(),
            'rank': scout.get_rank(),
            'patrol': scout.get_patrol(),
            'section': scout.get_section(),
            'events_attended': scout.get_events_attended(),
            'badges_earned': scout.get_badges_earned(),
            'badges_received': scout.get_badges_received(),
            'dob': scout.get_dob(),
            'scouts_phone': scout.get_scouts_phone(),
            'parents': scout.get_parents(),
            'medical': scout.get_medical(),
            'payments': scout.get_payments()
        }
        print('Scout created')
        print('Name:', scout.get_name())
        print('ID:', scout.get_id())
        print('Points:', scout.get_points())
        print('Rank:', scout.get_rank())
        print('Patrol:', scout.get_patrol())
        print('Section:', scout.get_section())
        print('Events Attended:', scout.get_events_attended())
        print('Badges Earned:', scout.get_badges_earned())
        print('Badges Received:', scout.get_badges_received())
        print('Date of Birth:', scout.get_dob())
        print('Scouts Phone:', scout.get_scouts_phone())
        print('Parents:', scout.get_parents())
        print('Medical:', scout.get_medical())
        print('Payments:', scout.get_payments())
    
    def do_patrol(self, inp):
        'Create a new patrol'
        patrol = Patrol(name=inp)
        data['patrols'][patrol.get_id()] = {
            'name': patrol.get_name(),
            'scouts': patrol.get_scouts(),
            'section': patrol.get_section()
        }
        print('Patrol created')
        print('Name:', patrol.get_name())
        print('ID:', patrol.get_id())
        print('Scouts:', patrol.get_scouts())
        print('Section:', patrol.get_section())

    def do_leader(self, inp):
        'Create a new leader'
        leader = Leader(name=inp)
        data['leaders'][leader.get_id()] = {
            'name': leader.get_name(),
            'sections': leader.get_sections()
        }
        print('Leader created')
        print('Name:', leader.get_name())
        print('ID:', leader.get_id())
        print('Sections:', leader.get_sections())

    def do_section(self, inp):
        'Create a new section'
        section = Section(name=inp)
        data['sections'][section.get_id()] = {
            'name': section.get_name(),
            'leaders': section.get_leaders(),
            'scouts': section.get_scouts(),
            'patrols': section.get_patrols(),
            'troop': section.get_troop()
        }
        print('Section created')
        print('Name:', section.get_name())
        print('ID:', section.get_id())
        print('Leaders:', section.get_leaders())
        print('Scouts:', section.get_scouts())
        print('Patrols:', section.get_patrols())
        print('Troop:', section.get_troop())

    def do_troop(self, inp):
        'Create a new troop'
        troop = Troop(name=inp)
        data['troops'][troop.get_id()] = {
            'name': troop.get_name(),
            'sections': troop.get_sections()
        }
        print('Troop created')
        print('Name:', troop.get_name())
        print('ID:', troop.get_id())
        print('Sections:', troop.get_sections())

    def do_event(self, inp):
        'Create a new event'
        event = Event(name=inp)
        data['events'][event.get_id()] = {
            'name': event.get_name(),
            'date': event.get_date(),
            'time': event.get_time(),
            'location': event.get_location(),
            'description': event.get_description(),
            'attendance': event.get_attendance()
        }
        print('Event created')
        print('Name:', event.get_name())
        print('ID:', event.get_id())
        print('Date:', event.get_date())
        print('Time:', event.get_time())
        print('Location:', event.get_location())
        print('Description:', event.get_description())
        print('Attendance:', event.get_attendance())

    def do_badge(self, inp):
        'Create a new badge'
        badge = Badge(name=inp)
        data['badges'][badge.get_id()] = {
            'name': badge.get_name(),
            'description': badge.get_description(),
            'requirements': badge.get_requirements(),
            'scouts_earned': badge.get_scouts_earned(),
            'scouts_received': badge.get_scouts_received()
        }
        print('Badge created')
        print('Name:', badge.get_name())
        print('ID:', badge.get_id())
        print('Description:', badge.get_description())
        print('Requirements:', badge.get_requirements())
        print('Scouts Earned:', badge.get_scouts_earned())
        print('Scouts Received:', badge.get_scouts_received())

    def do_get(self, inp):
        'Get a scout, patrol, leader, section, troop, event or badge'
        if inp.split(' ')[0] == 'scout':
            scout = data['scouts'][inp.split(' ')[1]]
            print('Scout found')
            print('Name:', scout['name'])
            print('ID:', inp.split(' ')[1])
            print('Points:', scout['points'])
            print('Rank:', scout['rank'])
            print('Patrol:', scout['patrol'])
            print('Section:', scout['section'])
            print('Events Attended:', scout['events_attended'])
            print('Badges Earned:', scout['badges_earned'])
            print('Badges Received:', scout['badges_received'])
            print('Date of Birth:', scout['dob'])
            print('Scouts Phone:', scout['scouts_phone'])
            print('Parents:', scout['parents'])
            print('Medical:', scout['medical'])
            print('Payments:', scout['payments'])
        elif inp.split(' ')[0] == 'patrol':
            patrol = data['patrols'][inp.split(' ')[1]]
            print('Patrol found')
            print('Name:', patrol['name'])
            print('ID:', inp.split(' ')[1])
            print('Scouts:', patrol['scouts'])
            print('Section:', patrol['section'])
        elif inp.split(' ')[0] == 'leader':
            leader = data['leaders'][inp.split(' ')[1]]
            print('Leader found')
            print('Name:', leader['name'])
            print('ID:', inp.split(' ')[1])
            print('Sections:', leader['sections'])
        elif inp.split(' ')[0] == 'section':
            section = data['sections'][inp.split(' ')[1]]
            print('Section found')
            print('Name:', section['name'])
            print('ID:', inp.split(' ')[1])
            print('Leaders:', section['leaders'])
            print('Scouts:', section['scouts'])
            print('Patrols:', section['patrols'])
            print('Troop:', section['troop'])
        elif inp.split(' ')[0] == 'troop':
            troop = data['troops'][inp.split(' ')[1]]
            print('Troop found')
            print('Name:', troop['name'])
            print('ID:', inp.split(' ')[1])
            print('Sections:', troop['sections'])
        elif inp.split(' ')[0] == 'event':
            event = data['events'][inp.split(' ')[1]]
            print('Event found')
            print('Name:', event['name'])
            print('ID:', inp.split(' ')[1])
            print('Date:', event['date'])
            print('Time:', event['time'])
            print('Location:', event['location'])
            print('Description:', event['description'])
            print('Attendance:', event['attendance'])
        elif inp.split(' ')[0] == 'badge':
            badge = data['badges'][inp.split(' ')[1]]
            print('Badge found')
            print('Name:', badge['name'])
            print('ID:', inp.split(' ')[1])
            print('Description:', badge['description'])
            print('Requirements:', badge['requirements'])
            print('Scouts Earned:', badge['scouts_earned'])
            print('Scouts Received:', badge['scouts_received'])
        else:
            print('Error: Invalid object')

    def do_set(self, inp):
        'Set a scout, patrol, leader, section, troop, event or badge'
        if inp.split(' ')[0] == 'scout':
            scout = data['scouts'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                scout['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'points':
                scout['points'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'rank':
                scout['rank'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'patrol':
                scout['patrol'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'section':
                scout['section'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'events_attended':
                scout['events_attended'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'badges_earned':
                scout['badges_earned'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'badges_received':
                scout['badges_received'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'dob':
                scout['dob'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts_phone':
                scout['scouts_phone'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'parents':
                scout['parents'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'medical':
                scout['medical'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'payments':
                scout['payments'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'patrol':
            patrol = data['patrols'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                patrol['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts':
                patrol['scouts'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'section':
                patrol['section'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'leader':
            leader = data['leaders'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                leader['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'sections':
                leader['sections'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'section':
            section = data['sections'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                section['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'leaders':
                section['leaders'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts':
                section['scouts'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'patrols':
                section['patrols'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'troop':
                section['troop'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'troop':
            troop = data['troops'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                troop['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'sections':
                troop['sections'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'event':
            event = data['events'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                event['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'date':
                event['date'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'time':
                event['time'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'location':
                event['location'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'description':
                event['description'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'attendance':
                event['attendance'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'badge':
            badge = data['badges'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                badge['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'description':
                badge['description'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'requirements':
                badge['requirements'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts_earned':
                badge['scouts_earned'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts_received':
                badge['scouts_received'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        else:
            print('Error: Invalid object')

    def do_add(self, inp):
        'Add a scout, patrol, leader, section, troop, event or badge'
        if inp.split(' ')[0] == 'scout':
            scout = data['scouts'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'points':
                scout['points'] = scout['points'] + int(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'events_attended':
                scout['events_attended'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'badges_earned':
                scout['badges_earned'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'badges_received':
                scout['badges_received'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'parents':
                scout['parents'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'payments':
                scout['payments'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'patrol':
            patrol = data['patrols'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'scouts':
                patrol['scouts'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'leader':
            leader = data['leaders'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'sections':
                leader['sections'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'section':
            section = data['sections'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'leaders':
                section['leaders'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'scouts':
                section['scouts'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'patrols':
                section['patrols'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'troop':
            troop = data['troops'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'sections':
                troop['sections'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'event':
            event = data['events'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'attendance':
                event['attendance'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'badge':
            badge = data['badges'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'scouts_earned':
                badge['scouts_earned'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'scouts_received':
                badge['scouts_received'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        else:
            print('Error: Invalid object')

    def do_remove(self, inp):
        'Remove a scout, patrol, leader, section, troop, event or badge'
        if inp.split(' ')[0] == 'scout':
            scout = data['scouts'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'events_attended':
                scout['events_attended'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'badges_earned':
                scout['badges_earned'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'badges_received':
                scout['badges_received'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'parents':
                scout['parents'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'payments':
                scout['payments'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'patrol':
            patrol = data['patrols'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'scouts':
                patrol['scouts'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'leader':
            leader = data['leaders'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'sections':
                leader['sections'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'section':
            section = data['sections'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'leaders':
                section['leaders'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'scouts':
                section['scouts'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'patrols':
                section['patrols'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'troop':
            troop = data['troops'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'sections':
                troop['sections'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'badge':
            badge = data['badges'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'scouts_earned':
                badge['scouts_earned'].remove(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'scouts_received':
                badge['scouts_received'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'event':
            event = data['events'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'attendance':
                event['attendance'].remove(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        else:
            print('Error: Invalid object')

    def do_delete(self, inp):
        'Delete a scout, patrol, leader, section, troop, event or badge'
        if inp.split(' ')[0] == 'scout':
            scout = data['scouts'][inp.split(' ')[1]]
            del data['scouts'][inp.split(' ')[1]]
        elif inp.split(' ')[0] == 'patrol':
            patrol = data['patrols'][inp.split(' ')[1]]
            del data['patrols'][inp.split(' ')[1]]
        elif inp.split(' ')[0] == 'leader':
            leader = data['leaders'][inp.split(' ')[1]]
            del data['leaders'][inp.split(' ')[1]]
        elif inp.split(' ')[0] == 'section':
            section = data['sections'][inp.split(' ')[1]]
            del data['sections'][inp.split(' ')[1]]
        elif inp.split(' ')[0] == 'troop':
            troop = data['troops'][inp.split(' ')[1]]
            del data['troops'][inp.split(' ')[1]]
        elif inp.split(' ')[0] == 'badge':
            badge = data['badges'][inp.split(' ')[1]]
            del data['badges'][inp.split(' ')[1]]
        elif inp.split(' ')[0] == 'event':
            event = data['events'][inp.split(' ')[1]]
            del data['events'][inp.split(' ')[1]]
        else:
            print('Error: Invalid object')

    def do_list(self, inp):
        'List scouts, patrols, leaders, sections, troops, events or badges'
        if inp == 'scouts':
            for scout in data['scouts']:
                print('Name:', data['scouts'][scout]['name'])
                print('ID:', scout)
                print('Points:', data['scouts'][scout]['points'])
                print('Rank:', data['scouts'][scout]['rank'])
                print('Patrol:', data['scouts'][scout]['patrol'])
                print('Section:', data['scouts'][scout]['section'])
                print('Events Attended:', data['scouts'][scout]['events_attended'])
                print('Badges Earned:', data['scouts'][scout]['badges_earned'])
                print('Badges Received:', data['scouts'][scout]['badges_received'])
                print('Date of Birth:', data['scouts'][scout]['dob'])
                print('Scouts Phone:', data['scouts'][scout]['scouts_phone'])
                print('Parents:', data['scouts'][scout]['parents'])
                print('Medical:', data['scouts'][scout]['medical'])
                print('Payments:', data['scouts'][scout]['payments'])
                print()
        elif inp == 'patrols':
            for patrol in data['patrols']:
                print('Name:', data['patrols'][patrol]['name'])
                print('ID:', patrol)
                print('Scouts:', data['patrols'][patrol]['scouts'])
                print('Section:', data['patrols'][patrol]['section'])
                print()
        elif inp == 'leaders':
            for leader in data['leaders']:
                print('Name:', data['leaders'][leader]['name'])
                print('ID:', leader)
                print('Sections:', data['leaders'][leader]['sections'])
                print()
        elif inp == 'sections':
            for section in data['sections']:
                print('Name:', data['sections'][section]['name'])
                print('ID:', section)
                print('Leaders:', data['sections'][section]['leaders'])
                print('Scouts:', data['sections'][section]['scouts'])
                print('Patrols:', data['sections'][section]['patrols'])
                print('Troop:', data['sections'][section]['troop'])
                print()
        elif inp == 'troops':
            for troop in data['troops']:
                print('Name:', data['troops'][troop]['name'])
                print('ID:', troop)
                print('Sections:', data['troops'][troop]['sections'])
                print()
        elif inp == 'events':
            for event in data['events']:
                print('Name:', data['events'][event]['name'])
                print('ID:', event)
                print('Date:', data['events'][event]['date'])
                print('Time:', data['events'][event]['time'])
                print('Location:', data['events'][event]['location'])
                print('Description:', data['events'][event]['description'])
                print('Attendance:', data['events'][event]['attendance'])
                print()
        elif inp == 'badges':
            for badge in data['badges']:
                print('Name:', data['badges'][badge]['name'])
                print('ID:', badge)
                print('Description:', data['badges'][badge]['description'])
                print('Requirements:', data['badges'][badge]['requirements'])
                print('Scouts Earned:', data['badges'][badge]['scouts_earned'])
                print('Scouts Received:', data['badges'][badge]['scouts_received'])
                print()
        else:
            print('Error: Invalid object')

    def do_save(self, inp):
        'Save the database'
        with open('scouts.json', 'w') as file:
            json.dump(data, file)
        print('Database saved')

    def do_load(self, inp):
        'Load the database'
        with open('scouts.json', 'r') as file:
            data = json.load(file)
        print('Database loaded')

    def do_reset(self, inp):
        'Reset the database'
        data = {
            'scouts': {},
            'patrols': {},
            'leaders': {},
            'sections': {},
            'troops': {},
            'events': {},
            'badges': {}
        }
        print('Database reset')

    def do_validate(self, inp):
        'Validate a scout, patrol, leader, section, troop, event or badge'
        if inp.split(' ')[0] == 'scout':
            scout = data['scouts'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['scout'](inp.split(' ')[3]):
                    scout['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'points':
                if validators['points'](inp.split(' ')[3]):
                    scout['points'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'rank':
                if validators['rank'](inp.split(' ')[3]):
                    scout['rank'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'patrol':
                if validators['patrol'](inp.split(' ')[3]):
                    scout['patrol'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'section':
                if validators['section'](inp.split(' ')[3]):
                    scout['section'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'events_attended':
                if validators['event'](inp.split(' ')[3]):
                    scout['events_attended'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'badges_earned':
                if validators['badge'](inp.split(' ')[3]):
                    scout['badges_earned'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'badges_received':
                if validators['badge'](inp.split(' ')[3]):
                    scout['badges_received'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'dob':
                if validators['dob'](inp.split(' ')[3]):
                    scout['dob'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts_phone':
                if validators['phone'](inp.split(' ')[3]):
                    scout['scouts_phone'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'parents':
                if validators['parents'](inp.split(' ')[3]):
                    scout['parents'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'medical':
                if validators['medical'](inp.split(' ')[3]):
                    scout['medical'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'payments':
                if validators['payments'](inp.split(' ')[3]):
                    scout['payments'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'patrol':
            patrol = data['patrols'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['patrol'](inp.split(' ')[3]):
                    patrol['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts':
                if validators['scout'](inp.split(' ')[3]):
                    patrol['scouts'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'section':
                if validators['section'](inp.split(' ')[3]):
                    patrol['section'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'leader':
            leader = data['leaders'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['leader'](inp.split(' ')[3]):
                    leader['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'sections':
                if validators['section'](inp.split(' ')[3]):
                    leader['sections'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'section':
            section = data['sections'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['section'](inp.split(' ')[3]):
                    section['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'leaders':
                if validators['leader'](inp.split(' ')[3]):
                    section['leaders'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'scouts':
                if validators['scout'](inp.split(' ')[3]):
                    section['scouts'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'patrols':
                if validators['patrol'](inp.split(' ')[3]):
                    section['patrols'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'troop':
                if validators['troop'](inp.split(' ')[3]):
                    section['troop'] = inp.split(' ')[3]
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'troop':
            troop = data['troops'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['troop'](inp.split(' ')[3]):
                    troop['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'sections':
                if validators['section'](inp.split(' ')[3]):
                    troop['sections'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'event':
            event = data['events'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['event'](inp.split(' ')[3]):
                    event['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'date':
                if validators['date'](inp.split(' ')[3]):
                    event['date'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'time':
                if validators['time'](inp.split(' ')[3]):
                    event['time'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'location':
                if validators['location'](inp.split(' ')[3]):
                    event['location'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'description':
                if validators['description'](inp.split(' ')[3]):
                    event['description'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'attendance':
                if validators['scout'](inp.split(' ')[3]):
                    event['attendance'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        elif inp.split(' ')[0] == 'badge':
            badge = data['badges'][inp.split(' ')[1]]
            if inp.split(' ')[2] == 'name':
                if validators['badge'](inp.split(' ')[3]):
                    badge['name'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'description':
                if validators['description'](inp.split(' ')[3]):
                    badge['description'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'requirements':
                if validators['requirements'](inp.split(' ')[3]):
                    badge['requirements'] = inp.split(' ')[3]
            elif inp.split(' ')[2] == 'scouts_earned':
                if validators['scout'](inp.split(' ')[3]):
                    badge['scouts_earned'].append(inp.split(' ')[3])
            elif inp.split(' ')[2] == 'scouts_received':
                if validators['scout'](inp.split(' ')[3]):
                    badge['scouts_received'].append(inp.split(' ')[3])
            else:
                print('Error: Invalid attribute')
        else:
            print('Error: Invalid object')

    def do_help(self, inp):
        'List available commands with "help" or detailed help with "help cmd".'
        cmd.Cmd.do_help(self, inp)

    def do_clear(self, inp):
        'Clear the screen'
        os.system('cls' if os.name == 'nt' else 'clear')

    def default(self, inp):
        if inp == 'exit' or inp == 'quit' or inp == 'EOF':
            return self.do_exit(inp)
        else:
            print('Error: Invalid command')

    def emptyline(self):
        pass

if __name__ == '__main__':
    Shell().cmdloop()