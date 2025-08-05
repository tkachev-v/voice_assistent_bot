import speech_recognition
from aiogram.types import Message
import os
from aiogram import Bot
from dotenv import load_dotenv
from app.generating import generating
from logger import logger
from prompts import prompt_voice


os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

from pydub import AudioSegment

load_dotenv()
token_tg = os.getenv("BOT_TOKEN")
# gigachat_api = os.getenv("API_GIGACHAT")

bot = Bot(token=token_tg)
AudioSegment.converter = "ffmpeg"
AudioSegment.ffprobe = "ffprobe"

async def handle_voice(message: Message):
    try:
        logger.info('Getting audio message')
        voice = await bot.get_file(message.voice.file_id)
        file_path = voice.file_path
        ogg_path = f"voice_{message.from_user.id}.ogg"
        wav_path = f"voice_{message.from_user.id}.wav"
        try:
            logger.info('Downloading audio file')
            await bot.download_file(file_path, destination=ogg_path)
            logger.info('Audio file downloaded')
            AudioSegment.from_file(ogg_path).export(wav_path, format="wav")
        except Exception as e:
            logger.error('Error downloading file: %s', e)

        with speech_recognition.AudioFile(wav_path) as source:
            sr = speech_recognition.Recognizer()
            sr.pause_threshold = 2.5
            try:
                sr.adjust_for_ambient_noise(source=source, duration=0.5)
                audio = sr.record(source)
                logger.info('Getting text from Google recognizer')
                query = sr.recognize_google(audio_data=audio, language='ru-RU')
            except speech_recognition.UnknownValueError:
                return "Не удалось распознать речь, попробуйте записать заново!"
            except Exception as e:
                logger.error('Error getting text from Google recognizer: %s', e)
        response = await generating(query, prompt_voice, message.from_user.id)
        return response
    except Exception as e:
         logger.error('Error getting file: %s', e)
    finally:
        for path in (ogg_path, wav_path):
            if os.path.exists(path):
                os.remove(path)
                logger.info('Deleted temporary file: %s', path)


