import selfcord as discord
from selfcord.ext import commands

bot = commands.Bot(command_prefix=";;;", self_bot=True)

# Function to check if a file is empty
def is_empty():
	try:
		with open('info.txt', 'r') as file:
			return not any(file)
	except FileNotFoundError:
		return True

# Function to write token to file if it's empty, or retrieve existing token
def process_data():
	data = ['','','','']
	file_path = "info.txt"
	with open(file_path, 'r') as file:  	 
		lines = file.readlines()


		data[0] = lines[0].split(":")[1].strip()
		data[1] = int(lines[1].split(":")[1].strip())
		data[2] = lines[2].split(":")[1].strip()
		data[3] = int(lines[3].split(":")[1].strip())



	return data

# attack!
@bot.event
async def on_ready():
	print("Bot initialised.")

@bot.event
async def on_message(message):
	data = process_data()
	if message.author.id == bot.user.id and message.content == "start":
		chatroom = bot.get_channel(data[1])
		for member in chatroom.recipients:
			if member.id == bot.user.id:
				pass
			else:
				index = 0
				try:
					while index < data[3]:
						await member.send(data[2])
						print(f"Sent message to {member.name}. Repetition {index}")
						index += 1
				except:
					pass
		print("JOB COMPLETE!")

	else:
		return



bot.run(token=process_data()[0])
