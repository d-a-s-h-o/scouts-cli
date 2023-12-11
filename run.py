import npyscreen
import json
import os

# Constants
JSON_FILE = 'scout_data.json'

# Data handling functions
def load_data():
    if not os.path.exists(JSON_FILE):
        return {}
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Scout Troop Management Application
class ScoutTroopApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.scoutData = load_data()
        self.addForm('MAIN', MainForm, name='Scout Troop Management')

# Main form for managing scouts
class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.name = self.add(npyscreen.TitleText, name='Name:')
        self.age = self.add(npyscreen.TitleText, name='Age:')
        self.add(npyscreen.ButtonPress, name='Save', when_pressed_function=self.save_scout)

    def save_scout(self):
        scout_info = {
            'name': self.name.value,
            'age': self.age.value
        }
        self.parentApp.scoutData.setdefault('scouts', []).append(scout_info)
        save_data(self.parentApp.scoutData)
        npyscreen.notify_confirm('Scout saved successfully!', title='Success')

if __name__ == '__main__':
    app = ScoutTroopApp()
    app.run()
