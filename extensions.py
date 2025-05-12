def main():
    # Prompt user for file name
    file_name = input("File name: ").strip().lower()

    # Get media type
    media_type = get_media_type(file_name)

    # Output the result
    print(media_type)


def get_media_type(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()
