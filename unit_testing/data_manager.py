class User: 
    def __init__(self, id, fName, lName, statusCode):
        self.id = id
        self.first_name = fName
        self.last_name = lName
        self.status = "ACTIVE" if statusCode == 1 else "INACTIVE"

def _toUser(rawRecord):
    id, fName, lName, statusCode = map(lambda item: str(item).strip(), rawRecord.split(","))
    return User(id, fName, lName, statusCode)

class DataManager:
    def __init__(self, dataClient):
        self.dataClient = dataClient
    
    def retrieveUsers(self):
        rawUserRecords = self.dataClient.retrieve()
        return list(map(_toUser, rawUserRecords))
        
