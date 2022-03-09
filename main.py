course_units = {
  'Unit 1, Information Technology Systems': {'glh': 120, 'type': 'external'},
  'Unit 2, Creating Systems to Manage Information': {'glh': 90, 'type': 'external'},
  'Unit 3, Using Social Media in Business': {'glh': 90, 'type': 'internal'},
  'Unit 4, Programming': {'glh': 90, 'type': 'internal'},
  'Unit 5, Data Modelling': {'glh': 60, 'type': 'internal'},
  'Unit 6, Website Development': {'glh': 60, 'type': 'internal'},
  'Unit 8, Computer Games Development': {'glh': 60, 'type': 'internal'},
  'Unit 9, IT Project Management': {'glh': 90, 'type': 'internal'},
  'Unit 11, Cyber Security and Incident Management': {'glh': 120, 'type': 'external'},
  'Unit 13, Software Testing': {'glh': 60, 'type': 'internal'},
  'Unit 14, IT Service Delivery': {'glh': 120, 'type': 'external'},
  'Unit 16, Cloud Storage and Collaboration Devices': {'glh': 60, 'type': 'internal'},
  'Unit 17, Digital 2D and 3D Graphics': {'glh': 60, 'type': 'internal'}
}

unit_points = {
  'internal': {
    60: {
      'U': 0,
      'P': 6,
      'M': 10,
      'D': 16
    },
    90: {
      'U': 0,
      'P': 9,
      'M': 15,
      'D': 24
    }
  },
  'external': {
    90: {
      'U': 0,
      'NP': 6,
      'P': 9,
      'M': 15,
      'D': 24
    },
    120: {
      'U': 0,
      'NP': 8,
      'P': 12,
      'M': 20,
      'D': 32 
    }
  }
}

grade_dict = {
  0: 'U',
  108: 'PPP',
  124: 'MPP',
  140: 'MMP',
  156: 'MMM',
  176: 'DMM',
  196: 'DDM',
  216: 'DDD',
  234: 'D*DD',
  252: 'D*D*D',
  270: 'D*D*D*',
}

current_points = 0
print("IT BTEC Grade Calculator")

for unit, _dict in course_units.items():
  user_input = input(f"Enter the grade you got for {unit}: ")
  _type = _dict.get('type')
  glh = _dict.get('glh') #

  while True:
    if user_input.upper() in unit_points[_type][glh].keys():
      current_points += unit_points[_type][glh].get(user_input.upper())
      break

    else:
      user_input = input(f"Incorrect grade, try again: ({', '.join(unit_points[_type][glh].keys())})")
      

previous_grade = None

for points, grade in grade_dict.items():
  if current_points < points:
    break

  previous_grade = grade

print(f"You got {previous_grade}!")


  
