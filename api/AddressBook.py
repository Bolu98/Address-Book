from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Add the address book fields to a request parser object
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("First name", required=True, help="First name must be included")
parser.add_argument("Last name", required=True, help="Last name must be included")
parser.add_argument("Phone number")

# Initialise display arrays
addressList = []
sortedList = []
matchedList = []

# Welcome message to check correct setup
class Welcome(Resource):
    def get(self):
        return {"message": "Address Book API Run Success!"}


# Function to return all entries in the address book
class getAddressList(Resource):
    def get(self):
        return {"Address list": addressList}


# Function to return the sorted entries in the address book
class getSortedList(Resource):
    def get(self):
        return {"Sorted list": sortedList}


# Function to return the matching entries in the address book
class getMatchedList(Resource):
    def get(self):
        return {"Matched list": matchedList}


# Add a new entry to the address book and return the added entry or error to the console
class addEntry(Resource):
    def post(self):
        args = parser.parse_args()
        if not args["First name"] or not args["Last name"]:
            return {"Error": "First name and last name must be included"}, 401
        elif args["First name"] == " " or args["Last name"] == " ":
            return {"Error": "Fist name and last name cannot be blank"}, 401
        else:
            for entry in addressList:
                if (
                    args["First name"] == entry["First name"]
                    and args["Last name"] == entry["Last name"]
                    and args["Phone number"] == entry["Phone number"]
                ):
                    return {"Error": "The entry is already in the address book"}, 402
            addressList.append(args)
            return {"New entry": args}


# Remove an entry from the address book and return the removed entry or error to the console
class removeEntry(Resource):
    def post(self):
        args = parser.parse_args()
        if not args["First name"] or not args["Last name"]:
            return {"Error": "First name and last name must be included"}, 401
        elif args["First name"] == " " or args["Last name"] == " ":
            return {"Error": "Fist name and last name cannot be blank"}, 401
        else:
            for entry in addressList:
                if (
                    args["First name"] == entry["First name"]
                    and args["Last name"] == entry["Last name"]
                    and args["Phone number"] == entry["Phone number"]
                ):
                    addressList.remove(entry)
                    return {"Removed entry": args}
            return {"Error": "This entry does not exist in the address book"}, 402


# Sort list by first or last name and return sorted list or error to the console
class retrieveSortedList(Resource):
    def get(self, sortKey):
        sortedList.clear()
        if sortKey == "f":
            tmpList = sorted(addressList, key=lambda entry: entry["First name"])
            for item in tmpList:
                sortedList.append(item)
            return {"Address book sorted by first name": sortedList}
        elif sortKey == "l":
            tmpList = sorted(addressList, key=lambda entry: entry["Last name"])
            for item in tmpList:
                sortedList.append(item)
            return {"Address book sorted by first name": sortedList}
        else:
            return (
                {
                    "Error": "Invalid sort key entered (must be either 'f' for First name or 'l' for Last name)"
                },
                403,
            )


# Return the matches or an error if no matches present to the console
class retrieveMatches(Resource):
    def get(self, name):
        matchedList.clear()
        nameLen = len(name)
        name = name.lower()
        for entry in addressList:
            if (
                entry["First name"].lower()[:nameLen] == name
                or entry["Last name"].lower()[:nameLen] == name
            ):
                matchedList.append(entry)
        if matchedList:
            return {"Entries with exact or partial name matches": matchedList}
        else:
            return {"Error": "No exact or partial name matches present"}, 405


api.add_resource(Welcome, "/welcome")
api.add_resource(getAddressList, "/getAddressList")
api.add_resource(getSortedList, "/getSortedList")
api.add_resource(getMatchedList, "/getMatchedList")
api.add_resource(addEntry, "/addEntry")
api.add_resource(removeEntry, "/removeEntry")
api.add_resource(retrieveSortedList, "/retrieveSortedList/<sortKey>")
api.add_resource(retrieveMatches, "/retrieveMatches/<name>")

if __name__ == "__main__":
    app.run(debug=True)
