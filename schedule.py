import requests, json

REST = "http://schedule.iitu.kz/rest/"

def errEmpty(inParantheses):
    return 'empty fields: ({})'.format(inParantheses)

def restRequest(data, url):
    response = requests.request("GET", REST + '/user' + url, params = data)
    return json.loads(response.text)

def restRequestTime(data, url):
    response = requests.request("GET", REST + '/time' + url, params = data)
    return json.loads(response.text)

def getCourses():
    return restRequest({}, '/get_course.php')

def getDepartments():
    return restRequest({}, '/get_department.php')

def getSpecialties(course = None):
    if course:
        return restRequest({'course': course}, '/get_specialty.php')
    else:
        return errEmpty('course_id')

def getGroups(course = None, specialty_id = None):
    if course and specialty_id:
        return restRequest({'course': course, 'specialty_id': specialty_id}, '/get_group.php')
    else:
        return errEmpty('course, specialty_id')

def getTeachers(department_id = None):
    if department_id:
        return restRequest({'department_id': department_id}, '/get_teacher.php')
    else:
        return errEmpty('department_id')

def getTimetableRoom(bundle_id):
    if bundle_id:
        return restRequest({'bundle_id': bundle_id}, '/get_timetable_room.php')
    else:
        return errEmpty('bundle_id')

def getTimetableGroup(group_id):
    if block_id:
        return restRequest({'block_id': group_id}, '/get_timetable_block.php')
    else:
        return errEmpty('block_id')

def getTimetableTeacher(teacher_id):
    if teacher_id:
        return restRequest({'teacher_id': teacher_id}, '/get_timetable_teacher.php')
    else:
        return errEmpty('teacher_id')

def search(query, count):
    if query and count:
        return restRequest({'query': query, 'count': count}, '/search.php')
    else:
        return errEmpty('query, count')

def getDays():
    return restRequestTime({}, '/get_day.php')

def getTimes():
    return restRequestTime({}, '/get_time.php')

def getCurrentTime():
    return restRequest({}, '/get_current_time.php')
