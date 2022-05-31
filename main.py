from gtts import gTTS
from art import tprint
from pathlib import Path
import pdfplumber
import docx2txt

def choose():
    print('For quit (-1)')
    c = input('File(0) or just text(1): ')
    if c == '0':
        file_path = input('File path: ')
        text = file_to_text(file_path=file_path)
    elif c == '1':
        text = input('Input text: ')
    elif c == '-1':
        print('Have good day!')
        exit()
    else:
        print('Error!\nTry again')
        choose()
    
    lang = input('Lang("ru" or "en"): ')
    result = text_to_mp3(text, lang)
    return result

def file_to_text(file_path):
    if Path(file_path).is_file():
        print('Wait pls...')
        text = ''
        try:
            # for txt file 
            if Path(file_path).suffix == '.txt':
                with open(file=file_path, mode='rb') as txt:
                    text = txt.readline().replace('\n', '')
            # for PDF file
            elif Path(file_path).suffix == '.pdf':
                with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
                    pages = [page.extract_text() for page in pdf.pages]
                text = "".join(pages)
                text = text.replace('\n', '')
            # for docx file
            elif Path(file_path).suffix == '.docx':
                text = (docx2txt.process(file_path)).replace('\n', '')
            # for other
            else:
                print('Error!\nFile is not supported')
        except ValueError as er:
            print('Check file and try again!')
            exit()

    else:
        print('Is not a file!\nTry again')
        choose()
    return text

def speed_of_text():
    speed = input('Speed: fast(0), slow(1): ')
    if speed == '0' or speed == '1':
        return int(speed) == 1
    elif speed == '-1':
        exit()
    else:
        print('Not good:/')
        speed_of_text()

def text_to_mp3(text, lang):
    try:
        return gTTS(text=text, lang=lang, slow=speed_of_text)
    except:
        return False

def create_mp3(result):
    if result:
        fileName = input('Input filename: ')
        if fileName == '-1':
            exit()
        result.save(f'{fileName}.mp3')         
        print('Have a nice day!!!')
    else:
        print('Hmmm...')
        print('Try again...')

def main():
    tprint('TEXT>>TO>>MP3')
    result = choose()
    create_mp3(result)

if __name__ == '__main__':
    main()

