# iitu_schedule_python
IITU Schedule API wrapper on Python3

## Installation

- Get into your project folder and download the module
  ``` sh
    $ cd your-project
    $ git clone https://github.com/soundsnick/iitu_schedule_python
  ```
- add following line to your file
  ``` python
  from iitu_schedule_python import schedule
  ```
- That's it! Module is ready to work with.

## Usage
Example:
``` python
# example.py
from iitu_schedule_python import schedule

courses = schedule.getCourses()
print(courses)
```
``` sh
$ python3 example.py
{'status': 0, 'error_message': None, 'result': [1, 2, 3, 4]}
```

## API Documentation

#### Search
`schedule.search({query}, {count}):`
Parameters: query, count
Description: Search module

##### Courses
`schedule.getCourses()`
Parameters: no
Description: Returns all existing courses

##### Departments
`schedule.getDepartments()`
Parameters: no
Description: Returns all existing departments

##### Specialties of course
`schedule.getSpecialties({course})`
Parameters: course
Description: Returns all specialties of course

##### Group
`schedule.getGroups({course}, {specialty_id})`
Parameters: course, specialty_id
Description: Returns group info

##### Teachers of department
`schedule.getTeachers({department_id})`
Parameters: department_id
Description: Returns all teachers of the department

#### Timetables
##### Timetable of group
`schedule.getTimetableGroup({group_id})`
Parameters: group_id
Description: Returns timetable

##### Timetable of room
`schedule.getTimetableRoom({bundle_id})`
Parameters: bundle_id
Description: Returns timetable

##### Timetable of teacher
`schedule.getTimetableTeacher({teacher_id})`
Parameters: teacher_id
Description: Returns timetable

#### Times and days
Returns the list of week days in 3 langs, and times list of day
`schedule.getDays()`
`schedule.getTimes()`

##### Current time
`schedule.getCurrentTime()`
Used to find left time to lesson.

## Author
VK: [Yernazar Askarovich](https://vk.com/id308337291)
Gmail: [soundsnick@gmail.com](mailto:soundsnick@gmail.com)
