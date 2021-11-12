"""Classe qui établit les caractéristiques générales d'un environnement type. 
Ces caractéristiques seront reprises pour influencer les statistiques et les évênements qui apparaissent."""

class Environnement():
    def __init__(self, weather, temperature, daytime, environnement):
        self.weather = weather
        self.temperature = temperature
        self.daytime = daytime
        self.environnement = environnement

    #setters
    def set_weather(self, weather):
        self.weather = weather

    def get_temperature(self, temperature):
        self.temperature = temperature
    
    def get_daytime(self, daytime):
        self.daytime = daytime

    def get_environnement(self, environnement):
        self.environnement = environnement

    #getters
    def get_weather(self):
        return self.weather

    def get_temperature(self):
        return self.temperature
    
    def get_daytime(self):
        return self.daytime

    def get_environnement(self):
        return self.environnement

#Test du get
env_1 = Environnement("pluie", 14, "jour", "forêt")
print(env_1.get_weather())