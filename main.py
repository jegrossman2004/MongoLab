import pymongo
import pprint

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host_name = "localhost"
    port = "27017"
    atlas_cluster_name = "cluster0.xuibg2h"
    atlas_default_dbname = "sakila"
    atlas_user_name = "ds2002sp23"
    atlas_password = "uva1819"
    conn_str = {
        "local": f"mongodb://{host_name}:{port}/",
        "atlas": f"mongodb+srv://{atlas_user_name}:{atlas_password}@{atlas_cluster_name}"
                 f".mongodb.net/{atlas_default_dbname}"
    }
    client = pymongo.MongoClient(conn_str["atlas"])
    print("Exercise 1: ", client.list_database_names())
    db_name = "jeremy_class"
    db = client[db_name]
    print("")
    print("")
    print("Exercise 2: ", db.list_collection_names())
    # EXERCISE 3 PART 1
    students = db.students

    # EXERCISE 3 PART 2
    student = {"Name": "Jeremy Grossman",
               "GPA": 3.943,
               "Major": "Statistics and Computer Science Double Major",
               "GradYear": 2026,
               "Birthday": "11/12/2004"
               }
    students.insert_one(student)

    # EXERCISE 3 PART 3
    new_students = [{"Name": "John Johnson",
                     "GPA": 2.5,
                     "Major": "Economics",
                     "GradYear": 2025,
                     "Birthday": "12/25/2003"
                     },
                    {"Name": "Patrick Mahomes",
                     "GPA": 3.5,
                     "Major": "Finance",
                     "GradYear": 2017,
                     "Birthday": "09/17/1995"
                     },
                    {"Name": "Josh Allen",
                     "GPA": 3.3,
                     "Major": "Civil Engineering",
                     "GradYear": 2018,
                     "Birthday": "05/21/1996"
                     }
                    ]

    students.insert_many(new_students)
    print("")
    print("")
    print("Exercise 4 Part 1:")
    for student in students.find():
        pprint.pprint(student)

    print("")
    print("")
    print("Exercise 4 Part 2:")
    pprint.pprint(students.find_one({"Name": "Patrick Mahomes"}))
    print("")
    print("")

    print("Exercise 5:")
    students.update_one({"Name": "John Johnson"}, {"$set": {"Major": "Chemistry"}})
    students.update_many({"GradYear": {"$lt": 2020}}, {"$set": {"Major": "Football"}})
    for student in students.find():
        pprint.pprint(student)
    print("")
    print("")
    print("Exercise 6 Part 1:")
    students.delete_one({"Name": "John Johnson"})
    for student in students.find():
        pprint.pprint(student)

    print("")
    print("")

    print("Exercise 6 Part 2:")
    students.delete_many({"GPA": {"$lt": 3.9}})
    for student in students.find():
        pprint.pprint(student)

    db.drop_collection("students")  # to prevent duplicates from appearing when the code is run multiple times
