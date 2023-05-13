import pymongo

# Create a client object to interact with the database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database called 'credit_data'
db = client["credit_data"]

# Create a new collection called 'credit_applications'
collection = db["credit_applications"]

# Insert some sample data into the collection
data = [
  {"age": 25, "income": 50000, "debt": 10000, "savings": 20000, "credit_history": 2, "approved": 1},
  {"age": 35, "income": 75000, "debt": 5000, "savings": 5000, "credit_history": 5, "approved": 1},
  {"age": 45, "income": 100000, "debt": 25000, "savings": 10000, "credit_history": 8, "approved": 0}
]
collection.insert_many(data)

# Close the database connection
client.close()
