from requests import get, post, delete
print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/5').json())
print(get('http://localhost:5000/api/v2/jobs/52').json())

print(post('http://localhost:5000/api/v2/jobs',
      json={"job": "creating application for DB"}).json())
print(post('http://localhost:5000/api/v2/jobs', json={'job': 'creating application for DB',
      'work_size': 12,  'team_leader': 9, 'collaborators': '6, 7', 'is_finished': True,
                                                      'category': 3}).json())

print(delete('http://localhost:5000/api/v2/jobs/999').json())
