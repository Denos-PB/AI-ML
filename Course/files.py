# import json
#
#
# def find(file, key):
#     def extract_values(data, target_key):
#         values = []
#
#         if isinstance(data, dict):
#             for k, v in data.items():
#                 if k == target_key:
#                     if isinstance(v, list):
#                         values.extend(v)
#                     else:
#                         values.append(v)
#                 else:
#                     values.extend(extract_values(v, target_key))
#         elif isinstance(data, list):
#             for item in data:
#                 values.extend(extract_values(item, target_key))
#
#         return values
#
#     with open(file, 'r') as f:
#         data = json.load(f)
#
#     all_values = extract_values(data, key)
#
#     unique_values = []
#     for value in all_values:
#         if value not in unique_values:
#             unique_values.append(value)
#
#     return unique_values
# import json
# import logging
#
#
# def parse_user(output_file, *input_files):
#     logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#     logger = logging.getLogger('root')
#
#     unique_users = []
#     seen_names = set()
#
#     for input_file in input_files:
#         try:
#             with open(input_file, 'r') as f:
#                 users = json.load(f)
#
#             for user in users:
#                 user_name = user.get('name')
#                 if user_name and user_name not in seen_names:
#                     unique_users.append(user)
#                     seen_names.add(user_name)
#
#         except json.JSONDecodeError as e:
#             logger.error(f"Error reading file {input_file}: {e}")
#             continue
#
#     with open(output_file, 'w') as f:
#         json.dump(unique_users, f, indent=4, ensure_ascii=False)
# import json
# from json import JSONEncoder
# import os
#
# class StudentEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return {
#                 'full_name': obj.full_name,
#                 'avg_rank': obj.avg_rank,
#                 'courses': obj.courses
#             }
#         return super().default(obj)
#
#
# class GroupEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Group):
#             return {
#                 'title': obj.title,
#                 'students': obj.students
#             }
#         elif isinstance(obj, Student):
#             return {
#                 'full_name': obj.full_name,
#                 'avg_rank': obj.avg_rank,
#                 'courses': obj.courses
#             }
#         return super().default(obj)
#
#
# class Student:
#     def __init__(self, full_name: str, avg_rank: float, courses: list):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses
#
#     @classmethod
#     def from_json(cls, json_file):
#         with open(json_file, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#         return cls(
#             full_name=data['full_name'],
#             avg_rank=data['avg_rank'],
#             courses=data['courses']
#         )
#
#     def serialize_to_json(self, filename):
#         with open(filename, 'w', encoding='utf-8') as f:
#             json.dump(self, f, cls=StudentEncoder, ensure_ascii=False)
#
#     def __str__(self):
#         return f"{self.full_name} ({self.avg_rank}): {self.courses}"
#
#     def __repr__(self):
#         return f"Student(full_name='{self.full_name}', avg_rank={self.avg_rank}, courses={self.courses})"
#
# class Group:
#     def __init__(self, title: str, students: list):
#         self.title = title
#         self.students = students if students else []
#
#     @classmethod
#     def serialize_to_json(cls, list_of_groups, filename):
#         with open(filename, 'w', encoding='utf-8') as f:
#             json.dump(list_of_groups, f, cls=GroupEncoder, ensure_ascii=False)
#
#     @classmethod
#     def create_group_from_file(cls, students_file):
#         title = os.path.splitext(os.path.basename(students_file))[0]
#
#         with open(students_file, 'r', encoding='utf-8') as f:
#             students_data = json.load(f)
#
#         students = []
#         if isinstance(students_data, list):
#             for student_data in students_data:
#                 student = Student(
#                     full_name=student_data['full_name'],
#                     avg_rank=student_data['avg_rank'],
#                     courses=student_data['courses']
#                 )
#                 students.append(student)
#         else:
#             student = Student(
#                 full_name=students_data['full_name'],
#                 avg_rank=students_data['avg_rank'],
#                 courses=students_data['courses']
#             )
#             students.append(student)
#
#         return cls(title, students)
#
#     def __str__(self):
#         student_strings = [str(student) for student in self.students]
#         return f"{self.title}: {student_strings}"
#
#     def __repr__(self):
#         return f"Group(title='{self.title}', students={len(self.students)} students)"

from enum import Enum
import json
import pickle

class FileType(Enum):
    JSON = 'json'
    BYTE = 'byte'

class SerializeManager:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def serialize(self, obj):
        if self.filetype == FileType.JSON:
            with open(self.filename, 'w') as f:
                json.dump(obj, f)
        elif self.filetype == FileType.BYTE:
            with open(self.filename, 'wb') as f:
                pickle.dump(obj, f)

def serialize(obj, filename, filetype):
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(obj)
