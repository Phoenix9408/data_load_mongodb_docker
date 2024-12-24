

Required_data_columns = ['Name','Age','Gender','Blood Type',
 'Medical Condition','Date of Admission',
 'Doctor','Hospital','Insurance Provider',
 'Billing Amount','Room Number','Admission Type',
 'Discharge Date','Medication','Test Results']

dtype_med_mapping = {
    "Name": "string",
    "Age": "int64",
    "Gender": "string",
    "Blood Type": "string",
    "Medical Condition": "string",
    "Doctor": "string",
    "Hospital": "string",
    "Insurance Provider": "string",
    "Billing Amount": "float64",
    "Room Number": "int64",
    "Admission Type": "string",
    "Medication": "string",
    "Test Results": "string"
}
columns_dates = ["Date of Admission", "Discharge Date"]