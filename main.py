from gtts import gTTS
import PyPDF2

def pdf_to_text(pdf_path):
    """
    Extract text from a PDF file.
    """
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_path='output.mp3'):
    """
    Convert text to speech and save it as an MP3 file using gTTS.
    """
    tts = gTTS(text=text, lang='en')  # Adjust the language if needed
    tts.save(output_path)

def main():
    pdf_path = '/Users/musumakas/Desktop/pdf_mp3/Hello .pdf'  # Replace with the path to your PDF file
    output_path = 'master.mp3'  # Output MP3 file path

    text = pdf_to_text(pdf_path)
    text_to_speech(text, output_path)

if __name__ == "__main__":
    main()


