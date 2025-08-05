import speech_recognition
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from aiogram.types import Message
from aiogram.enums import ContentType
# import os
# os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"
# from pydub import AudioSegment

# bot = Bot(token="7290155255:AAELJztaxDO5TRjyPedQ_-LhYwklg07nsmU")
# dp = Dispatcher(storage=MemoryStorage())


# AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"
# AudioSegment.ffprobe = "/opt/homebrew/bin/ffprobe"


#@dp.message(F.voice)
# async def handle_voice(message: Message):
#     # Скачиваем файл
#     voice = await bot.get_file(message.voice.file_id)
#     file_path = voice.file_path
#     ogg_path = f"voice_{message.from_user.id}.ogg"
#     wav_path = f"voice_{message.from_user.id}.wav"
#
#     await bot.download_file(file_path, destination=ogg_path)
#
#     # Конвертируем ogg → wav
#     AudioSegment.from_file(ogg_path).export(wav_path, format="wav")
#
#     sr = speech_recognition.Recognizer()
#     sr.pause_threshold = 2.5
#
#     with speech_recognition.AudioFile(wav_path) as source:
#         sr.adjust_for_ambient_noise(source=source, duration=0.5)
#         audio = sr.record(source)
#         query = sr.recognize_google(audio_data = audio, language = 'ru-Ru')
#
#     giga = GigaChat(
#         # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
#         credentials="YzFjZDBlOTItN2YwZi00NmZlLTlhYTYtNjMyNjQ1YTQyMmM0OjA0MjM4NDE3LWNmMzgtNDY2ZS1hMWM1LTViNjAyZjNlNDE3NQ==",
#         verify_ssl_certs=False,
#     )
#
#     messages = [
#         SystemMessage(
#             content = "Ты бот-ассистент председателя банка, который суммаризирует текст и в итоге создает проект поручений в виде: Задача: "
#                       "Ответственные люди:"
#                       "В какой срок нужно выполнить:"
#                       "Если ты не получаешь информации по пунктам уточняешь, пишешь неизвестно"
#
#         )
#     ]
#
#     messages.append(HumanMessage(content=query))
#     res = giga.invoke(messages)
#     messages.append(res)
#     await message.answer(res.content)
    #print("GigaChat: ", res.content)
from pydub import AudioSegment
import os
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"
# Укажи путь к ffmpeg, если он не в PATH
AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"
AudioSegment.ffprobe = "/opt/homebrew/bin/ffprobe"


# Загружаем исходный файл
audio = AudioSegment.from_file("/Users/tkachevvladislav/Desktop/viper.ogg", format="ogg")

# Обрезаем: от 10-й до 30-й секунды (в миллисекундах)
cropped = audio[9000:88000]

# Сохраняем результат
cropped.export("/Users/tkachevvladislav/Desktop/вайпер дабларр.mp3", format="mp3")

try:
    logger.info('Starting generating process')
    messages = [SystemMessage(
        content=prompt
    ),
        HumanMessage(content=text)]
    res = agent.invoke(messages)
    return res.content
except Exception as e:
    logger.error('Error in generating process: %s', e)
except Exception as e:
    logger.error('Error in connecting to gigachat API: %s', e)