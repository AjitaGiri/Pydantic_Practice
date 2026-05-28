# Create Course model. Each course has modules.Each module has lessons.

from pydantic import BaseModel
from typing import List,Dict,Optional

class Lesson(BaseModel):
    lesson_id:int
    topic:str

class Modules(BaseModel):
    module_id:int
    lessons: List[Lesson]

class Course(BaseModel):
    course_id:int
    title:str
    modules: List[Modules]

lesson=Lesson(lesson_id=1,topic='Machine Learning')
module=Modules(module_id=101,lessons=[lesson])
course=Course(course_id=201,modules=[module])