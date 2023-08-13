#  Напишите проект, содержащий функционал работы с заметками. 
# Программа должна уметь создавать заметку, сохранять её, 
# читать список заметок, редактировать заметку, удалять заметку.
import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self, notes_folder):
        self.notes_folder = notes_folder
        os.makedirs(notes_folder, exist_ok=True)

    def save_note(self, note):
        note_filename = os.path.join(self.notes_folder, f"{note.title}.txt")
        with open(note_filename, "w") as file:
            file.write(note.content)

    def read_notes(self):
        notes = []
        for filename in os.listdir(self.notes_folder):
            if filename.endswith(".txt"):
                title = filename[:-4]
                with open(os.path.join(self.notes_folder, filename), "r") as file:
                    content = file.read()
                notes.append(Note(title, content))
        return notes

    def edit_note(self, title, new_content):
        note_filename = os.path.join(self.notes_folder, f"{title}.txt")
        if os.path.exists(note_filename):
            with open(note_filename, "w") as file:
                file.write(new_content)
            return True
        return False

    def delete_note(self, title):
        note_filename = os.path.join(self.notes_folder, f"{title}.txt")
        if os.path.exists(note_filename):
            os.remove(note_filename)
            return True
        return False

