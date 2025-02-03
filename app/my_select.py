from db import session
from sqlalchemy.sql import func, desc
from models import Student, Grade, Subject, Teacher, Group


def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    return (
        session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(subject_id: int):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    return (
        session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )


def select_3(subject_id: int):
    """Знайти середній бал у групах з певного предмета."""
    return (
        session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .order_by(desc("avg_grade"))
        .all()
    )


def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    return session.query(func.avg(Grade.grade).label("avg_grade")).scalar()


def select_5(teacher_id: int):
    """Знайти які курси читає певний викладач."""
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()


def select_6(group_id: int):
    """Знайти список студентів у певній групі."""
    return session.query(Student.name).filter(Student.group_id == group_id).all()


def select_7(group_id: int, subject_id: int):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    return (
        session.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )


def select_8(teacher_id: int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    return (
        session.query(func.avg(Grade.grade).label("avg_grade"))
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


def select_9(student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )


def select_10(student_id: int, teacher_id: int):
    """Список курсів, які певному студенту читає певний викладач."""
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
        .all()
    )


def print_result(result, counter=[1]):
    print(f"### Query {counter[0]}")
    print("```")
    print(result)
    print("```")
    counter[0] += 1

if __name__ == "__main__":
    print_result(select_1())
    print_result(select_2(1))
    print_result(select_3(1))
    print_result(select_4())
    print_result(select_5(1))
    print_result(select_6(1))
    print_result(select_7(1, 1))
    print_result(select_8(1))
    print_result(select_9(1))
    print_result(select_10(1, 1))
