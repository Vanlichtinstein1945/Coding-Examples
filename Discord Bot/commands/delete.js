module.exports = {
	name: 'delete',
	description: 'Deletes a command from the current bot iteration',
	execute(message, args) {
		if (!args.length) return message.channel.send(`You do not specify a command to delete, ${message.author}.`);
		const commandName = args[0].toLowerCase();
		const command = message.client.commands.get(commandName)
			|| message.client.commands.find(cmd => cmd.aliases && cmd.aliases.includes(commandName));
		
		if (!command) return message.channel.send('I\'m sorry, this command isn\'t active for this bot.');
		
		delete require.cache[require.resolve(`./${commandName}.js`)];
		
		message.channel.send(`The command \'${commandName}\' was successfully removed!`);
	},
};