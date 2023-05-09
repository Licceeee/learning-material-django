from course.models import CourseUser


def create_course_to_user_and_redirect(user_id, course_id):
    obj, created = CourseUser.objects.get_or_create(user=user_id, course=course_id)
    if created:
        return created
    return obj