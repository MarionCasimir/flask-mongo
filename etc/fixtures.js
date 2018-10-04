//db.createUser({"user": "kim", "pwd": "kim"})

db.users.insert([
  {
    "_id": NumberInt(000),
    "name": "Kim"
  },
  {
    "_id": NumberInt(123),
    "name": "Marion"
  },
  {
    "_id": NumberInt(456),
    "name": "Kelly"
  },
  {
    "_id": NumberInt(789),
    "name": "Wako"
  }
])

db.stores.insert([
  {
    "_id": NumberInt(1),
    "name": "Target"
  },
  {
    "_id": NumberInt(2),
    "name": "Amazon"
  },
  {
    "_id": NumberInt(3),
    "name": "Walmart"
  }
])
