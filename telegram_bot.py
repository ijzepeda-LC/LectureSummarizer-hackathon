#!/usr/bin/env python

import logging
from telegram import __version__ as TG_VER
import whisper
import os
import toml
import openai
TOKEN=toml.load('.streamlit/secrets.toml')['TELEGRAM_API_KEY']
openai.api_key = toml.load('.streamlit/secrets.toml')['OPENAI_API_KEY']#os.getenv("OPENAI_API_KEY")

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This bot is not compatible with your current PTB version {TG_VER}. Sorry!"
        
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

VOICE, AUDIO, TRANSLATE= range(3)
BOTNAME="StudyAssistantLC"
WHISPER_MODEL="small"
language="english"
user_data="user_data" #server folder

if not os.path.exists(os.path.join('./',(user_data))):
        print(f"Making a folder for {user_data}")
        os.makedirs(os.path.join('./',(user_data)))

try:
    model = whisper.load_model(WHISPER_MODEL, device='gpu')
    print("GPU Found,")
except:
    print("No GPU found, using CPU")
    model = whisper.load_model(WHISPER_MODEL, device='cpu')  


def get_transcript(audio_file):
    #Using whisper
    out = model.transcribe(audio_file)
    return out['text']  

def get_summary(prompt,model="text-ada-001",language="", verbose=False):
    model="text-davinci-003"
    tokens=int(1000) if int(len(prompt)/4)>250 else int(len(prompt)/4)
    augmented_prompt = f"summarize this text {language}: {prompt}"
    try:
        summary_text = openai.Completion.create( 
                model =  model,  
                prompt = augmented_prompt,
                temperature=.5,
                max_tokens= tokens,
            )['choices'][0]['text'].strip() 
    except Exception as e:
        error="There was an error", str(e) if verbose else ""
        print(error)
        summary_text=error
    return summary_text

##############
### COMMANDS
##############

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user to send a voicenote."""
   
    await update.message.reply_text(
        f"Hi! This is a {BOTNAME}. \nI will transcript your audios and provide a summary of it "
        "\nSend /cancel to stop talking to me.\n\n"
        "Start sending a VOICE NOTE",
    )

    return AUDIO


async def voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the audio."""
    await update.message.reply_text(
        "Got your voicenote, hold on...."
    )
    user = update.message.from_user
    #1
    # audio_file = update.message.voice.file_id
    # new_file = context.bot.get_file(update.message.voice.file_id)
    # new_file.download(f"./{user_data}/voice_note.ogg")
    #2
    audio_file = await update.message.voice.get_file()
    audio_path=f"./{user_data}/user_voice.ogg"
    
    if not os.path.exists(os.path.join('./',(user_data))):
        print(f"Making a folder for {user_data}")
        os.makedirs(os.path.join('./',(user_data)))


    await audio_file.download_to_drive(audio_path)
    logger.info("Audio of %s: %s", user.first_name, "user_voice.ogg")
    await update.message.reply_text(
        "Working on it..."
    )
    x=  get_transcript(audio_path)
    await update.message.reply_text(
        "Transcript:\n"+x
    )   
    y=  get_summary(x)
    await update.message.reply_text(
        "Summary:\n"+y
    )  

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the audio."""
    await update.message.reply_text(
        "Got your audio, hold on...."
    )
    user = update.message.from_user
    audio_file = await update.message.audio.get_file()
    audio_path=f"./{user_data}/user_audio.ogg"
    
    if not os.path.exists(os.path.join('./',(user_data))):
        print(f"Making a folder for {user_data}")
        os.makedirs(os.path.join('./',(user_data)))

    await audio_file.download_to_drive(audio_path)
    logger.info("Audio of %s: %s", user.first_name, "user_audio.ogg")
    await update.message.reply_text(
        "Working on it..."
    )
    x=  get_transcript(audio_path)
    await update.message.reply_text(
        "Transcript:\n"+x
    )   
    y=  get_summary(x)
    await update.message.reply_text(
        "Summary:\n"+y
    )  


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        f"Bye! Thank you for using the {BOTNAME}.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
        AUDIO: [
        MessageHandler(filters.VOICE, voice),
        MessageHandler(filters.AUDIO, audio),
                    # MessageHandler(filters.TEXT, summary)
                    ], 

        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()