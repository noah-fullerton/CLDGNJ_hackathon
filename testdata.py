import db_control

event1 = {
    "name": "TechFest 2023",
    "start_date": "2023-11-01",
    "end_date": "2023-11-03",
    "location": "Engineering Building, Room 101",
    "description": "A three-day event showcasing the latest technological innovations by students. Workshops, panels, and competitions included."
  }
event2 = {
    "name": "Art Showcase: Autumn Visions",
    "start_date": "2023-11-15",
    "end_date": "2023-11-20",
    "location": "Campus Art Gallery",
    "description": "An art exhibition featuring the works of budding artists, capturing the essence of autumn."
  }
event3 = {
    "name": "Eco Day Fair",
    "start_date": "2023-11-25",
    "end_date": "2023-11-25",
    "location": "Central Campus Lawn",
    "description": "Join us for a day of eco-friendly workshops, stalls, and talks. Learn how you can make a difference for our planet."
  }
event4 = {
    "name": "Winter Wonderland Ball",
    "start_date": "2023-12-10",
    "end_date": "2023-12-10",
    "location": "Campus Grand Hall",
    "description": "A magical night of dance, music, and winter-themed festivities. Formal attire required."
  }
event5 = {
    "name": "Entrepreneurship Pitch Night",
    "start_date": "2023-12-18",
    "end_date": "2023-12-18",
    "location": "Business Auditorium, Room 201",
    "description": "Witness the next generation of entrepreneurs as they pitch their innovative business ideas to a panel of industry experts."
  }

cont = db_control.Controller()
cont.insertEvents(event1)
cont.insertEvents(event2)
cont.insertEvents(event3)
cont.insertEvents(event4)
cont.insertEvents(event5)

