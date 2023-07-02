import discord
import openai

intents = discord.Intents.default()
intents.message_content = True  # Включаем получение содержимого сообщений

bot = discord.Client(intents=intents)

openai.api_key = 'токен чата gpt'  # Замените на свой API-ключ OpenAI

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):  # Проверяем, было ли упоминание бота в сообщении
        if message.author == bot.user:  # Игнорируем собственные сообщения бота
            return

        user_input = message.content.replace(f'<@!{bot.user.id}>', '')  # Удаляем упоминание бота из сообщения

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.7
        )

        generated_text = response.choices[0].text.strip()
        await message.channel.send(generated_text)  # Отправляем ответное сообщение

bot.run('токен дс бота')
