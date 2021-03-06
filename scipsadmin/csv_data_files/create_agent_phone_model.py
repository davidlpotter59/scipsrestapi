from scipsadmin.models import Agent
from scipsadmin.models import AgentPhone
from scipsadmin.models import PhoneType

import csv, os

file_loc = '/Users/richl/dev/source/django_rest_api/scipsrestapi-project/scipsadmin/csv_data_files/agentphone.csv'
print (file_loc)
with open(file_loc, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        print(row['agent_no'],row['telephone_number'], row['phone_type'])
        agent_obj, created = Agent.objects.get_or_create(agent_no=row['agent_no'])
        phonetype_obj, created = PhoneType.objects.get_or_create(type = row['phone_type'])
        p = AgentPhone(agent_no = agent_obj,
            phone=row['telephone_number'],
            phone_type = phonetype_obj)
        p.save()