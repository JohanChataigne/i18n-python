from pathlib import Path

from icu import Locale

from message_manager import MessageManager


def main():
    french = Locale("fr_FR")

    manager = MessageManager(
        messages_directory=Path("."),
        default_locale=french,
    )

    print(
        manager.get(key="welcome", locale=french, name="Johan")
    )

    print(
        manager.get(key="files", locale=french, count=2)
    )

    print(
        manager.get(key="balance", locale=french, amount=1500.8)
    )


if __name__ == "__main__":
    main()
