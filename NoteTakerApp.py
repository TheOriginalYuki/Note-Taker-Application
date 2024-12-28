import json
from datetime import datetime
import re

def load_notes(filename='StoreNotes.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes, filename='StoreNotes.json'):
     with open(filename, 'r') as file:
           json.dump(notes, file, indent=4)

def extract_tags(content):
    # Simple example: extract words longer than 3 characters as tags
    words = re.findall(r'\b\w{4,}\b', content)
    return list(set(words))

def add_note():
    title = input("Title:").strip().lower()
    content = input("Content:").strip().lower()
    tags = extract_tags(content)
    new_note = {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tags": tags
    }
    notes = load_notes()
    notes.append(new_note)
    save_notes(notes)
    print("Note added successfully!")

def view_notes():
    notes = load_notes()
    for note in enumerate(notes, start=1):
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")
        print("-" * 20)

def delete_note():
    title = input("Title:").lower().strip()
    notes = load_notes()
    notes = [note for note in notes if note['title'] != title]
    save_notes(notes)
    print("Note deleted successfully!")

def search_notes():
    keyword = input("Keyword:").lower().split()
    notes = load_notes()
    found_notes = [note for note in notes if keyword in note['title'] or keyword in note['content']]
    for index, note in enumerate(found_notes, start=1):
        print(f"{index}. Title: {note['title']}")
        print(f"Content: {note['content']}")
    print("-" * 20)

def main():
    while True:
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Search Notes")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            search_notes()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()