dataset_name= "Lucas"
row_count = 10
processing_time = 0.314

rows_per_second = row_count / processing_time
print(f"Rows per second: {rows_per_second:.2f}")



source_name = input("Enter source name: ")
records_ingested = int(input("How many records ingested? "))
records_failed = int(input("How many records failed?"))

if total_records > 0:
    success_rate = (records_ingested / total_records) * 100
    print(f"Success rate: {success_rate:.2f}%")
else:
    print("No records processed.")

print(f"the success rate is {success_rate}")

user_number = int(input("Insert a random number:"))
if user_number > 1000:
    print(f"{user_number} is greater than 1000")
