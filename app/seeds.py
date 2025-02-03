from db import session
import random
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

faker = Faker()


def main():
    try:
        logger.info("Generating groups")
        groups = [Group(name=f"Group {i+1}") for i in range(3)]
        session.add_all(groups)

        logger.info("Generating teachers")
        teachers = [Teacher(name=faker.name()) for _ in range(5)]
        session.add_all(teachers)

        logger.info("Generating subjects")
        subjects = [
            Subject(name=faker.word(), teacher=random.choice(teachers))
            for _ in range(8)
        ]
        session.add_all(subjects)

        logger.info("Generating students")
        students = [
            Student(name=faker.name(), group=random.choice(groups)) for _ in range(50)
        ]
        session.add_all(students)

        logger.info("Generating grades")
        grades = [
            Grade(
                student=random.choice(students),
                subject=random.choice(subjects),
                date_received=faker.date_this_year(),
                grade=random.uniform(1, 5),
            )
            for _ in range(1000)
        ]
        session.add_all(grades)

        session.commit()
        logger.info("Data has been successfully added")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    main()
