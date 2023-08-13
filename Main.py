def main():
    notes_manager = NoteManager("notes")

    while True:
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите текст заметки: ")
            note = Note(title, content)
            notes_manager.save_note(note)
            print("Заметка сохранена.")

        elif choice == "2":
            notes = notes_manager.read_notes()
            if notes:
                print("Список заметок:")
                for index, note in enumerate(notes, start=1):
                    print(f"{index}. {note.title}")
                note_number = input("Выберите номер заметки для просмотра: ")
                try:
                    note_number = int(note_number)
                    if 1 <= note_number <= len(notes):
                        print(f"Заметка: {notes[note_number - 1].title}")
                        print(notes[note_number - 1].content)
                    else:
                        print("Неверный номер заметки.")
                except ValueError:
                    print("Неверный ввод номера заметки.")

            else:
                print("Список заметок пуст.")

        elif choice == "3":
            title = input("Введите заголовок заметки для редактирования: ")
            new_content = input("Введите новый текст заметки: ")
            if notes_manager.edit_note(title, new_content):
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка не найдена.")

        elif choice == "4":
            title = input("Введите заголовок заметки для удаления: ")
            if notes_manager.delete_note(title):
                print("Заметка успешно удалена.")
            else:
                print("Заметка не найдена.")

        elif choice == "5":
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
