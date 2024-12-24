// ADMIN 
db.createUser({
  user: "admin_ocr",
  pwd: "admin_ocr", 
  roles: [
    { role: "root", db: "admin" } // 
  ]
});

db.createUser({
  user: "ocr"
  pwd: "ocr"
  roles: [
    { role: "root", db: "admin" } // 
  ]
});

// Process Creation Index
db = db.getSiblingDB("ocr")

db.Medical.createIndex({  "Doctor": 1, 
                           "Medical Condition": 1,
						   "Hospital": 1,
						   "Admission Type": 1 
					    });