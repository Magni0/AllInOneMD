from models.Document import Document
from functools import wraps
import os
# from main import create_app

# def remove_file_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)   
#     print(document)
#     os.remove(os.path.abspath(f"temp_file_storage/{document.docname}.pdf"))
#     return wrapper
