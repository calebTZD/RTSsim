from pymongo import MongoClient, ASCENDING

class DBaccess:
    def __init__(self):
        # self.client = MongoClient("mongodb://localhost:27017/admin")
        # self.client = MongoClient("mongodb+srv://DayleyCoders:ForgeScale9@caltrops1.u2ypo.mongodb.net/RTSDB?retryWrites=true&w=majority")

        self.client = MongoClient("mongodb+srv://DayleyCoders:ForgeScale9@caltrops1.u2ypo.mongodb.net/RTSDB?retryWrites=true&w=majority")
        self.villageDB = self.client.RTSDB

        # self.villageDB = self.client["RTSDB"]
        self.SimCol = self.villageDB["Sims"]
        self.VillageCol = self.villageDB["Villages"]
        self.StatsCol = self.villageDB["Stats"]

    def initSimCollection(self):
        self.SimCol.drop()
        self.SimCol.create_index("name", unique=True)
    
    def initVillagesCollection(self):
        self.VillageCol.drop()
        self.VillageCol.create_index([("name", ASCENDING), ("simulationName", ASCENDING)], unique=True)

    def initStatsCollection(self):
        self.StatsCol.drop()
        self.StatsCol.create_index("simName")
        
DB = DBaccess()
