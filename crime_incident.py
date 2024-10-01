import json
import os

class CrimeIncident:
    def __init__(self, incident_id, description, location, date):
        self.incident_id = incident_id
        self.description = description
        self.location = location
        self.date = date

    def __str__(self):
        return f"ID: {self.incident_id}, Desc: {self.description}, Loc: {self.location}, Date: {self.date}"

    def to_dict(self):
        return {
            "incident_id": self.incident_id,
            "description": self.description,
            "location": self.location,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['incident_id'], data['description'], data['location'], data['date'])


class CrimeIncidentManager:
    def __init__(self, file_path='crime_data.json'):
        self.file_path = file_path
        self.incidents = self.load_data()

    def add_incident(self, incident):
        self.incidents.append(incident)
        self.save_data()

    def update_incident(self, incident_id, updated_incident):
        for i, incident in enumerate(self.incidents):
            if incident.incident_id == incident_id:
                self.incidents[i] = updated_incident
                self.save_data()
                return True
        return False

    def delete_incident(self, incident_id):
        for i, incident in enumerate(self.incidents):
            if incident.incident_id == incident_id:
                del self.incidents[i]
                self.save_data()
                return True
        return False

    def delete_all_incidents(self):
        self.incidents = []  # Clear the in-memory list
        self.save_data()  # Save the empty list to the JSON file

    def get_all_incidents(self):
        return self.incidents

    def get_incident_by_id(self, incident_id):
        for incident in self.incidents:
            if incident.incident_id == incident_id:
                return incident
        return None

    def save_data(self):
        """Saves the incident data to a JSON file."""
        with open(self.file_path, 'w') as file:
            data = [incident.to_dict() for incident in self.incidents]
            json.dump(data, file, indent=4)

    def load_data(self):
        """Loads the incident data from a JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [CrimeIncident.from_dict(incident) for incident in data]
        else:
            return []
