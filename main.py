from icu import Locale

def main():
    locale = Locale("fr_FR")
    print(locale.getDisplayName())


if __name__ == "__main__":
    main()
