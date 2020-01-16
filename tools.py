import chardet


# detect encoding
def detect_encoding(file_path):
    detector = chardet.UniversalDetector()
    for line in open(file_path, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()

    return detector.result['encoding']

