"""Django App config for course_modes"""


from django.apps import AppConfig


class CourseModesConfig(AppConfig):
    name = 'course_modes'
    verbose_name = "Course Modes"

    def ready(self):
        import course_modes.signals
