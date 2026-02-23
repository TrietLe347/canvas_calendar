
class Event:

    def __init__(self, uid,title, course, due, desc, url):
        self.uid = uid
        self.title = title
        self.course = course
        self.due_date = due
        self.desc = desc
        self.url = url

    def get_title(self):
        return self.title

    def get_course(self):
        return self.course

    def get_due_date(self):
        return self.due_date

    def get_desc(self):
        return self.desc
    
    def get_url(self):
        return self.url
    


