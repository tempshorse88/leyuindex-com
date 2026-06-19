from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    url: str
    summary: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self) -> str:
        parts = [
            f"Keyword: {self.keyword}",
            f"URL: {self.url}",
            f"Summary: {self.summary}",
            f"Tags: {', '.join(self.tags) if self.tags else 'None'}",
            f"Created: {self.created_at}",
        ]
        return "\n".join(parts)

@dataclass
class NotesCollection:
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if any(t.lower() == tag.lower() for t in n.tags)]

    def format_all(self, separator: str = "---") -> str:
        blocks = [note.display() for note in self.notes]
        return f"\n{separator}\n".join(blocks)

def create_leyu_notes() -> NotesCollection:
    collection = NotesCollection()

    note1 = KeywordNote(
        keyword="leyu",
        url="https://leyuindex.com",
        summary="Main entry for leyu resource index.",
        tags=["index", "resource"],
    )

    note2 = KeywordNote(
        keyword="leyu",
        url="https://leyuindex.com/about",
        summary="About page for the leyu index project.",
        tags=["about", "info"],
    )

    note3 = KeywordNote(
        keyword="leyu guide",
        url="https://leyuindex.com/guide",
        summary="Usage guide and documentation for leyu.",
        tags=["guide", "help", "documentation"],
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)
    return collection

def sample_demo() -> None:
    print("=== Keyword Notes Demo ===")
    notes = create_leyu_notes()

    print("\nAll notes:")
    print(notes.format_all())
    print()

    filtered = notes.filter_by_keyword("leyu")
    print(f"Filtered by keyword 'leyu': {len(filtered)} note(s)")
    print()

    tag_filtered = notes.filter_by_tag("guide")
    print(f"Filtered by tag 'guide': {len(tag_filtered)} note(s)")
    for n in tag_filtered:
        print(n.display())
        print()

if __name__ == "__main__":
    sample_demo()