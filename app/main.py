class OnlineCourse:
    # course_dict = {}
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        # OnlineCourse.course_dict["name"] = name
        # OnlineCourse.course_dict["description"] = description
        # OnlineCourse.course_dict["days"] = weeks * 7

    @staticmethod
    def days_to_weeks(days: int) -> None:
        if days < 7:
            return 1
        if days % 7 == 0:
            return days // 7
        return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"]),
        )
