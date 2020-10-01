module.exports = {
	name: 'add',
	description: 'Adds a new command of the given name as long as the appropriate .js file is in the bot\'s directory',
	execute(message, args) {
		if (!args.length) return message.channel.send(`You didn\'t pass any commands to be added, ${message.author}!`);
		const commandName = args[0].toLowerCase();
		const command = message.client.commands.get(commandName)
			|| message.client.commands.find(cmd => cmd.aliases && cmd.aliases.includes(commandName));
			
		if (command) return message.channel.send('I\'m sorry, this command is already active for this bot.');
		
		try {
			const newCommand = require(`./${commandName}.js`);
			message.client.commands.set(newCommand.name, newCommand);
		} catch(error) {
			console.log(error);
			return message.channel.send(`There was an error while adding your command \'${commandName}\':\n\'${error.message}\'`);
		}
		
		message.channel.send(`The command \'${commandName}\' was successfully added!`);
	},
};