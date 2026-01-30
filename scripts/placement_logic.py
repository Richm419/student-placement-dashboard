import pandas as pd

students = pd.read_csv("students.csv")
sites = pd.read_csv("sites.csv")

assignments = []
site_capacity = dict(zip(sites.site_id, sites.capacity))

for _, student in students.iterrows():
    if student["compliance_ready"] != "Yes":
        continue

    for _, site in sites.iterrows():
        if (
            site.region == student.preferred_region
            and site_capacity[site.site_id] > 0
        ):
            assignments.append([student.student_id, site.site_id])
            site_capacity[site.site_id] -= 1
            break

df = pd.DataFrame(assignments, columns=["student_id", "site_id"])
df.to_csv("placements.csv", index=False)

print("Placements generated successfully!")
