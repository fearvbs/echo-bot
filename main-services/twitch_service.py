from twitchio.ext import commands

class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(token='YOUR_TWITCH_TOKEN', prefix='!', initial_channels=['YOUR_CHANNEL'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return
        await self.handle_commands(message)

    @commands.command(name='ask')
    async def ask_command(self, ctx, *, question: str):
        # Логика для обработки вопроса
        answer = "Ответ на ваш вопрос"  # Замените на реальный ответ
        await ctx.send(answer)